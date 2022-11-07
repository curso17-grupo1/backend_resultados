from models.partido import Partido
from repositories.partido_repositories import PartidoRepository


class PartidoController:

    def __init__(self):
        """
        :return:
        """
        print("Partido Controller ready")
        self.partido_repositories = PartidoRepository()

    def index(self) -> list:
        """


        :return:
        """
        print("All partido")
        return self.partido_repositories.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("mostrar un partido")
        partido = self.partido_repositories.find_by_id(id_)
        return partido

    def create(self, partido_: dict) -> Partido:
        """

        :param partido_:
        :return:
        """
        print("crear partido")
        partido = Partido(partido_)
        return self.partido_repositories.save(partido)

    def update(self, id_: str, partido_: dict) -> Partido:
        """

        :param id_:
        :param partido_:
        :return:
        """
        print("update partido")
        partido = Partido(partido_)
        return self.partido_repositories.update(id_, partido)

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete partido")
        return self.partido_repositories.delete(id_)
