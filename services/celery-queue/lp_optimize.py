import numpy as np
import pandas as pd
import pulp
from scipy.stats import norm
from multiprocessing import cpu_count
from subprocess import check_output


class ModelLP(pulp.LpProblem):
    COIN_SOLVER = pulp.solvers.COIN_CMD(check_output(["which", "cbc"]).rstrip().decode(),
                                    threads=cpu_count(),
                                    msg=1,
                                    fracGap=0.01)
    def __init__(self, name='seed_supply', filename='/seed_supply.lp', **args):
        # Set parameters
        self.filename = filename

        # Initialize LpProblem
        super(ModelLP, self).__init__(name, pulp.LpMaximize)

        paramsLP = ['n_intervals',
                    'starting_supply',
                    'price',
                    'shortage',
                    'salvage',
                    'planting_cost_na',
                    'planting_cost_sa',
                    'processing_cost_na',
                    'processing_cost_sa',
                    'yield_mean_na',
                    'yield_mean_sa',
                    'demand_mean']

        # Check for existence of LP parameters
        for param in paramsLP:
            if not param in args:
                raise ValueError(f"Parameter {param} must be specified.")

            self.__dict__[param] = args[param]

        # Initialize model
        self.set_vars()
        self.set_coeffs()
        self.initialize_model()

    def set_vars(self):
        n = self.n_intervals
        N = n**3

        # Initialize variables
        self.vars = pulp.LpVariable.dicts("x", range(N+n+1), lowBound=0, upBound=None, cat=pulp.LpContinuous)

    def set_coeffs(self):    
        n = self.n_intervals
        N = n**3

        # Initialize yield and demand distributions
        self.yield_dist_na, self.yield_na = dist(self.yield_mean_na, rsd=0.1, n_intervals=self.n_intervals).values.T
        self.yield_dist_sa, self.yield_sa = dist(self.yield_mean_sa, rsd=0.1, n_intervals=self.n_intervals).values.T
        self.demand_dist, self.demand = dist(self.demand_mean, rsd=0.1, n_intervals=self.n_intervals).values.T

        profit_bound_na = (self.planting_cost_na/self.yield_dist_na.dot(self.yield_na)) + self.processing_cost_na >= self.salvage
        profit_bound_sa = (self.planting_cost_sa/self.yield_dist_sa.dot(self.yield_sa)) + self.processing_cost_sa >= self.salvage
        produce_bound_na = self.price + self.shortage >= (self.planting_cost_na/self.yield_dist_na.dot(self.yield_na)) + self.processing_cost_na
        produce_bound_sa = self.price + self.shortage >= (self.planting_cost_sa/self.yield_dist_sa.dot(self.yield_sa)) + self.processing_cost_sa

        if not (profit_bound_na and profit_bound_sa):
            raise ValueError("Salvage value outweighs total cost: profit is unbounded.")

        if not (produce_bound_na or produce_bound_sa):
            raise ValueError("Total cost outweighs gain: production should be discontinued.")

        # Define objective function c@x, and upper bound constraints A_ub@x<=b_ub
        self.objective_coeffs = np.zeros(N+n+1)
        self.constraint_A_ub_coeffs = np.zeros((2*N,N+n+1))
        self.constraint_b_ub_coeffs = np.zeros(2*N)
        self.objective_coeffs[0] = -(self.planting_cost_na + self.processing_cost_na * self.yield_dist_na.dot(self.yield_na))
        self.objective_coeffs[1:n+1] = -(self.planting_cost_sa + self.processing_cost_sa * self.yield_dist_sa.dot(self.yield_sa)) * self.yield_dist_na
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    ind = i*n*n+j*n+k
                    self.objective_coeffs[ind+n+1] = self.yield_dist_na[i]*self.yield_dist_sa[j]*self.demand_dist[k]
                    self.constraint_A_ub_coeffs[ind,0] = -(self.price + self.shortage)*self.yield_na[i]
                    self.constraint_A_ub_coeffs[ind,i+1] = -(self.price + self.shortage)*self.yield_sa[j]
                    self.constraint_A_ub_coeffs[ind,ind+n+1] = 1
                    self.constraint_b_ub_coeffs[ind] = (self.price + self.shortage)*self.starting_supply - self.shortage*self.demand[k]
                    self.constraint_A_ub_coeffs[N+ind,0] = -self.salvage*self.yield_na[i]
                    self.constraint_A_ub_coeffs[N+ind,i+1] = -self.salvage*self.yield_sa[j]
                    self.constraint_A_ub_coeffs[N+ind,ind+n+1] = 1
                    self.constraint_b_ub_coeffs[N+ind] = self.salvage*self.starting_supply + (self.price - self.salvage)*self.demand[k]

    def initialize_model(self):
        self += pulp.lpSum(self.objective_coeffs[i]*self.vars[i] for i in self.vars)
        # man = Manager()
        # man_x = man.dict(self.vars)
        # A_shape = self.constraint_A_ub_coeffs.shape
        # man_A_ub = RawArray('d', self.constraint_A_ub_coeffs.reshape((A_shape[0]*A_shape[1],)))
        # man_b_ub = RawArray('d', self.constraint_b_ub_coeffs)
        # with Pool(processes=cpu_count()-1, initializer=init_worker, initargs=(man_x, man_A_ub, man_b_ub)) as pool:
        #     constraints = pool.map(set_constraint, range(len(self.constraint_b_ub_coeffs)))
        # self.extend(constraints)
        for i in range(len(self.constraint_b_ub_coeffs)):
            constraint = pulp.lpSum(self.constraint_A_ub_coeffs[i,j]*self.vars[j] for j in self.vars if self.constraint_A_ub_coeffs[i,j]) <= self.constraint_b_ub_coeffs[i]
            self += constraint
        self.writeLP(self.filename)

    def solve(self, solver=None):
        if solver is None:
            solver = self.COIN_SOLVER
        status = super(ModelLP, self).solve(solver)
        return status

    def expected_result(self):
        n = self.n_intervals
        gross_margin = pulp.value(self.objective)
        acres_na = self.vars[0].varValue
        acres_sa = np.array([self.vars[i].varValue for i in range(1, n+1)])
        revenue = np.array([self.vars[i].varValue for i in range(n+1, len(self.vars))])
        coeffs_acres_na = self.objective_coeffs[0]
        coeffs_acres_sa = self.objective_coeffs[1:n+1]
        coeffs_revenue = self.objective_coeffs[n+1:]

        exp_acres_sa = self.yield_dist_na.dot(acres_sa)
        exp_revenue = coeffs_revenue.dot(revenue)
        exp_finished_inventory = self.starting_supply + self.yield_dist_na.dot(self.yield_na)*acres_na + self.yield_dist_sa.dot(self.yield_sa)*exp_acres_sa - self.demand_dist.dot(self.demand)

        result = {
            "gross_margin": gross_margin,
            "acres_na": acres_na,
            "acres_sa": exp_acres_sa,
            "revenue": exp_revenue,
            "finished_inventory": exp_finished_inventory
        }
        return result


class ModelLPA(pulp.LpProblem):
    COIN_SOLVER = pulp.solvers.COIN_CMD(check_output(["which", "cbc"]).rstrip().decode(),
                                    threads=cpu_count(),
                                    msg=1,
                                    fracGap=0.01)
    def __init__(self, name='seed_supply', filename='/seed_supply.lp', **args):
        # Set parameters
        self.filename = filename

        # Initialize LpProblem
        super(ModelLPA, self).__init__(name, pulp.LpMaximize)

        paramsLP = ['starting_supply',
                    'price',
                    'shortage',
                    'salvage',
                    'planting_cost_na',
                    'planting_cost_sa',
                    'processing_cost_na',
                    'processing_cost_sa',
                    'yield_dist_na',
                    'yield_na',
                    'yield_dist_sa',
                    'yield_sa',
                    'demand_dist',
                    'demand']

        # Check for existence of LP parameters
        for param in paramsLP:
            if not param in args:
                raise ValueError(f"Parameter {param} must be specified.")
            self.__dict__[param] = args[param]

        # Initialize model
        self.set_vars()
        self.set_coeffs()
        self.initialize_model()

    def set_vars(self):
        n_i = len(self.yield_na)
        n_j = len(self.yield_sa)
        n_k = len(self.demand)
        N = n_i * n_j * n_k

        # Initialize variables
        self.vars = pulp.LpVariable.dicts("x", range(N+n_i+1), lowBound=0, upBound=None, cat=pulp.LpContinuous)

    def set_coeffs(self):    
        n_i = len(self.yield_na)
        n_j = len(self.yield_sa)
        n_k = len(self.demand)
        N = n_i * n_j * n_k

        # Initialize yield and demand distributions
        self.yield_dist_na, self.yield_na = np.array(self.yield_dist_na), np.array(self.yield_na)
        self.yield_dist_sa, self.yield_sa = np.array(self.yield_dist_sa), np.array(self.yield_sa)
        self.demand_dist, self.demand = np.array(self.demand_dist), np.array(self.demand)

        profit_bound_na = (self.planting_cost_na/self.yield_dist_na.dot(self.yield_na)) + self.processing_cost_na >= self.salvage
        profit_bound_sa = (self.planting_cost_sa/self.yield_dist_sa.dot(self.yield_sa)) + self.processing_cost_sa >= self.salvage
        produce_bound_na = self.price + self.shortage >= (self.planting_cost_na/self.yield_dist_na.dot(self.yield_na)) + self.processing_cost_na
        produce_bound_sa = self.price + self.shortage >= (self.planting_cost_sa/self.yield_dist_sa.dot(self.yield_sa)) + self.processing_cost_sa

        if not (profit_bound_na and profit_bound_sa):
            raise ValueError("Salvage value outweighs total cost: profit is unbounded.")

        if not (produce_bound_na or produce_bound_sa):
            raise ValueError("Total cost outweighs gain: production should be discontinued.")

        # Define objective function c@x, and upper bound constraints A_ub@x<=b_ub
        self.objective_coeffs = np.zeros(N+n_i+1)
        self.constraint_A_ub_coeffs = np.zeros((2*N,N+n_i+1))
        self.constraint_b_ub_coeffs = np.zeros(2*N)
        self.objective_coeffs[0] = -(self.planting_cost_na + self.processing_cost_na * self.yield_dist_na.dot(self.yield_na))
        self.objective_coeffs[1:n_i+1] = -(self.planting_cost_sa + self.processing_cost_sa * self.yield_dist_sa.dot(self.yield_sa)) * self.yield_dist_na
        for i in range(n_i):
            for j in range(n_j):
                for k in range(n_k):
                    ind = i*n_j*n_k+j*n_k+k
                    self.objective_coeffs[ind+n_i+1] = self.yield_dist_na[i]*self.yield_dist_sa[j]*self.demand_dist[k]
                    self.constraint_A_ub_coeffs[ind,0] = -(self.price + self.shortage)*self.yield_na[i]
                    self.constraint_A_ub_coeffs[ind,i+1] = -(self.price + self.shortage)*self.yield_sa[j]
                    self.constraint_A_ub_coeffs[ind,ind+n_i+1] = 1
                    self.constraint_b_ub_coeffs[ind] = (self.price + self.shortage)*self.starting_supply - self.shortage*self.demand[k]
                    self.constraint_A_ub_coeffs[N+ind,0] = -self.salvage*self.yield_na[i]
                    self.constraint_A_ub_coeffs[N+ind,i+1] = -self.salvage*self.yield_sa[j]
                    self.constraint_A_ub_coeffs[N+ind,ind+n_i+1] = 1
                    self.constraint_b_ub_coeffs[N+ind] = self.salvage*self.starting_supply + (self.price - self.salvage)*self.demand[k]

    def initialize_model(self):
        self += pulp.lpSum(self.objective_coeffs[i]*self.vars[i] for i in self.vars)
        # man = Manager()
        # man_x = man.dict(self.vars)
        # A_shape = self.constraint_A_ub_coeffs.shape
        # man_A_ub = RawArray('d', self.constraint_A_ub_coeffs.reshape((A_shape[0]*A_shape[1],)))
        # man_b_ub = RawArray('d', self.constraint_b_ub_coeffs)
        # with Pool(processes=cpu_count()-1, initializer=init_worker, initargs=(man_x, man_A_ub, man_b_ub)) as pool:
        #     constraints = pool.map(set_constraint, range(len(self.constraint_b_ub_coeffs)))
        # self.extend(constraints)
        for i in range(len(self.constraint_b_ub_coeffs)):
            constraint = pulp.lpSum(self.constraint_A_ub_coeffs[i,j]*self.vars[j] for j in self.vars if self.constraint_A_ub_coeffs[i,j]) <= self.constraint_b_ub_coeffs[i]
            self += constraint
        self.writeLP(self.filename)

    def solve(self, solver=None):
        if solver is None:
            solver = self.COIN_SOLVER
        status = super(ModelLPA, self).solve(solver)
        return status

    def expected_result(self):
        n_i = len(self.yield_na)
        gross_margin = pulp.value(self.objective)
        acres_na = self.vars[0].varValue
        acres_sa = np.array([self.vars[i].varValue for i in range(1, n_i+1)])
        revenue = np.array([self.vars[i].varValue for i in range(n_i+1, len(self.vars))])
        coeffs_acres_na = self.objective_coeffs[0]
        coeffs_acres_sa = self.objective_coeffs[1:n_i+1]
        coeffs_revenue = self.objective_coeffs[n_i+1:]

        exp_acres_sa = self.yield_dist_na.dot(acres_sa)
        exp_revenue = coeffs_revenue.dot(revenue)
        exp_finished_inventory = self.starting_supply + self.yield_dist_na.dot(self.yield_na)*acres_na + self.yield_dist_sa.dot(self.yield_sa)*exp_acres_sa - self.demand_dist.dot(self.demand)

        result = {
            "gross_margin": gross_margin,
            "acres_na": acres_na,
            "acres_sa": exp_acres_sa,
            "revenue": exp_revenue,
            "finished_inventory": exp_finished_inventory
        }
        return result


def dist(exp_val, rsd=0.1, n_intervals=25):
    X = np.linspace(exp_val*(1-3*rsd/2), exp_val*(1+3*rsd/2), n_intervals)
    P = np.array([norm.pdf(y, loc=exp_val, scale=exp_val*rsd/2) for y in X])
    P /= P.sum()
    return pd.DataFrame({"Prob(Xi)": P, "Xi": X})