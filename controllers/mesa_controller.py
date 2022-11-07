from models.mesa import Mesa


class MesaController:

    def __init__(self):
        """

        :return:
        """
        print("Mesa Controller ready")

    def index(self) -> list:
        """

        :return:
        """
        print("All mesas")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("mostrar una mesa")

    def create(self, mesa_) -> dict:
        """

        :param mesa_:
        :return:
        """
        print("crear mesa")

    def update(self, id_, mesa_) -> dict:
        """

        :param id_:
        :param mesa_:
        :return:
        """
        print("update mesa")

    def delete(self, id_) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete mesa")

