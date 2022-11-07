from flask import Blueprint
from flask import request

from controllers.mesa_Controller import MesaController


mesa_blueprint = Blueprint('mesa_blueprint', __name__)
mesa_controller = MesaController()


@mesa_blueprint.route("/mesa/all", methods=['GET'])
def get_mesa():
    response = mesa_controller.index()
    return response, 200


@mesa_blueprint.route("/mesa/<string:id_>", methods=['GET'])
def get_mesa_by_id(id_):
    response = mesa_controller.show(id_)
    return response, 200


@mesa_blueprint.route("/mesa/insert", methods=['POST'])
def insert_mesa():
    mesa = request.get_json()
    response = mesa_controller.create(mesa)
    return response, 201


@mesa_blueprint.route("/mesa/update/<string:id_>", methods=['PATCH'])
def update_mesa(id_):
    mesa = request.get_json()
    response = mesa_controller.update(id_, mesa)
    return response, 201


@mesa_blueprint.route("/mesa/delete/<string:id_>", methods=['DELETE'])
def delete_mesa(id_):
    response = mesa_controller.delete(id_)
    return response, 204
