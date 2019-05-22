import datetime

from flask import current_app
from sqlalchemy.sql import func

from project import db


class SupplyModel(db.Model):

    __tablename__ = 'models'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(255))
    created_date = db.Column(db.DateTime)
    starting_inventory = db.Column(db.Float)
    price = db.Column(db.Float)
    shortage = db.Column(db.Float)
    salvage = db.Column(db.Float)
    production_na = db.Column(db.Float)
    processing_na = db.Column(db.Float)
    production_sa = db.Column(db.Float)
    processing_sa = db.Column(db.Float)
    yield_prob_na = db.Column(db.ARRAY(db.Float))
    yield_na = db.Column(db.ARRAY(db.Float))
    yield_prob_sa = db.Column(db.ARRAY(db.Float))
    yield_sa = db.Column(db.ARRAY(db.Float))
    demand_prob = db.Column(db.ARRAY(db.Float))
    demand = db.Column(db.ARRAY(db.Float))
    status = db.Column(db.Integer)
    gross_margin = db.Column(db.Float)
    acres_na = db.Column(db.Float)
    acres_sa = db.Column(db.Float)
    revenue = db.Column(db.Float)
    finished_inventory = db.Column(db.Float)

    def __init__(self, **kwargs):
        for k in kwargs:
            self.__dict__[k] = kwargs[k]

    def to_json(self):
        json_data = {k: self.__dict__[k] for k in self.__dict__ if k[0] != '_'}
        return json_data
