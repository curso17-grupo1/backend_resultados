from models.resultado import Resultado


class ResultadoController:

    def __init__(self):
        """

        :return:
        """
        print("Resultado Controller ready")

    # Equivalente al 'all'
    def index(self) -> list:
        """

        :return:
        """
        print("All resultado")

    # Equivalente a 'uno por el elemento'
    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("mostrar un resultado")

    # equivalente a agregar
    def create(self, resultado_: dict) -> dict:
        """

        :param resultado_:
        :return:
        """
        print("crear resultado")

    # Equivalente a actualizar
    def update(self, id_: str, resultado_: dict) -> dict:
        """

        :param id_:
        :param resultado_:
        :return:
        """
        print("update resultado")

    # Equivalente a borrar
    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete resultado")

