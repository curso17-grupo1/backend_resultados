from models.mesa import Mesa
from repositories.mesa_repositories import MesaRepository


class MesaController:

    def __init__(self):
        """
        :return:
        """
        print("Mesa Controller ready")
        self.mesa_repositories = MesaRepository()

    def index(self) -> list:
        """


        :return:
        """
        print("All mesas")
        return self.mesa_repositories.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("mostrar una mesa")
        mesa = self.mesa_repositories.find_by_id(id_)
        return mesa

    def create(self, mesa_: dict) -> Mesa:
        """

        :param mesa_:
        :return:
        """
        print("crear mesa")
        mesa = Mesa(mesa_)
        return self.mesa_repositories.save(mesa)

    def update(self, id_: str, mesa_: dict) -> Mesa:
        """

        :param id_:
        :param mesa_:
        :return:
        """
        print("update mesa")
        mesa = Mesa(mesa_)
        return self.mesa_repositories.update(id_, mesa)

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete mesa")
        return self.mesa_repositories.delete(id_)
