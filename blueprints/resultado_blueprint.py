from flask import Blueprint
from flask import request

from controllers.resultado_controller import ResultadoController

resultado_blueprint = Blueprint('resultado_blueprint', __name__)
resultado_controller = ResultadoController()


@resultado_blueprint.route("/resultado/all", methods=['GET'])
def get_resultado():
    response = resultado_controller.index()
    return response, 200


@resultado_blueprint.route("/resultado/<string:id_>", methods=['GET'])
def get_resultado_by_id(id_):
    response = resultado_controller.show(id_)
    return response, 200


@resultado_blueprint.route("/resultado/insert", methods=['POST'])
def insert_resultado():
    resultado = request.get_json()
    response = resultado_controller.create(resultado)
    return response, 201


@resultado_blueprint.route("/resultado/update/<string:id_>", methods=['PATCH'])
def update_resultado(id_):
    resultado = request.get_json()
    response = resultado_controller.update(id_, resultado)
    return response, 201


@resultado_blueprint.route("/resultado/delete/<string:id_>", methods=['DELETE'])
def delete_resultado(id_):
    response = resultado_controller.delete(id_)
    return response, 204
