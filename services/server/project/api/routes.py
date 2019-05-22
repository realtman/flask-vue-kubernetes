import os

from flask import Blueprint, jsonify, request

from project.api.models import SupplyModel
from project import db


route_blueprint = Blueprint('models', __name__)


@route_blueprint.route('/models', methods=['GET', 'POST'])
def all_models():
    response_object = {
        'status': 'success',
        'container_id': os.uname()[1]
    }
    if request.method == 'POST':
        post_data = request.get_json()
        db.session.add(SupplyModel(**post_data))
        db.session.commit()
        response_object['message'] = 'Model added!'
    else:
        response_object['models'] = [model.to_json() for model in SupplyModel.query.all()]
    return jsonify(response_object)


@route_blueprint.route('/models/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    })


@route_blueprint.route('/models/<model_id>', methods=['PUT', 'DELETE'])
def single_model(model_id):
    response_object = {
      'status': 'success',
      'container_id': os.uname()[1]
    }
    model = SupplyModel.query.filter_by(id=model_id).first()
    if request.method == 'PUT':
        post_data = request.get_json()
        for k in post_data:
            model.__dict__[k] = post_data.get(k)
        db.session.commit()
        response_object['message'] = 'Model updated!'
    if request.method == 'DELETE':
        db.session.delete(model)
        db.session.commit()
        response_object['message'] = 'Model removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
