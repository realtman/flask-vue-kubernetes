import os
import time
from lp_optimize import ModelLP, ModelLPA
from datetime import datetime
# from urllib.parse import urlparse

from sqlalchemy import create_engine  
from sqlalchemy import Column, DateTime, Integer, Float 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.dialects.postgresql import ARRAY

from celery import Celery, Task


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'pyamqp://admin:pass@localhost:5672//')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'rpc://')
DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@db:5432/postgres')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

Base = declarative_base()


class DBTask(Task):
    _engine = None
    _Session = None

    def after_return(self, *args, **kwargs):
        if self._Session is not None:
            self._Session.remove()

    @property
    def engine(self):
        if self._engine is None:
            self._engine = create_engine(DATABASE_URL)
        return self._engine

    @property
    def Session(self):
        if self._Session is None:
            self._Session = scoped_session(sessionmaker(bind=self.engine))
            Base.metadata.create_all(self.engine)
        return self._Session


class Model(Base):  
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime)
    status = Column(Integer)
    starting_supply = Column(Float)
    price = Column(Float)
    shortage = Column(Float)
    salvage = Column(Float)
    planting_cost_na = Column(Float)
    processing_cost_na = Column(Float)
    planting_cost_sa = Column(Float)
    processing_cost_sa = Column(Float)
    yield_dist_na = Column(ARRAY(Float))
    yield_na = Column(ARRAY(Float))
    yield_dist_sa = Column(ARRAY(Float))
    yield_sa = Column(ARRAY(Float))
    demand_dist = Column(ARRAY(Float))
    demand = Column(ARRAY(Float))
    gross_margin = Column(Float)
    acres_na = Column(Float)
    acres_sa = Column(Float)
    revenue = Column(Float)
    finished_inventory = Column(Float)


@celery.task(name='tasks.add')
def add(x: int, y: int):
    time.sleep(5)
    result = {
        "x": x,
        "y": y,
        "sum": x+y
    }
    return result

@celery.task(name='tasks.optimize')
def optimize(**args):
    for k in args:
        if k == 'n_intervals':
            args[k] = int(args[k]) 
        else:
            args[k] = float(args[k])
    problem = ModelLP(**args)
    status = problem.solve()
    result = problem.expected_result()
    result.update({"status": status})
    return result

@celery.task(base=DBTask, bind=True, name='tasks.optimizeA')
def optimizeA(self, **args):
    for k in args:
        if isinstance(args[k], list):
            for i in range(len(args[k])):
                args[k][i] = float(args[k][i])
        else:
            args[k] = float(args[k])
    problem = ModelLPA(**args)
    status = problem.solve()
    result = problem.expected_result()
    result.update({"status": status})

    args_result = args.copy()
    args_result.update(result)

    # for k in args_result:
    #     if isinstance(args_result[k], np.ndarray):
    #         args_result[k] = args_result[k].tolist()

    new_model = Model(**args_result)

    session = self.Session()
    session.add(new_model) 
    session.commit()

    return result
    # return args
