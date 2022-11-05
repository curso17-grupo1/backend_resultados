from models.partido import Partido


class PartidoController:

    def __int__(self):
        """

        :return:
        """
        print("Partido Controller ready")

    def index(self) -> list:
        """

        :return:
        """
        print("All partido")

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("mostrar un partido")

    def create(self, partido_: dict) -> dict:
        """

        :param partido_:
        :return:
        """
        print("crear partido")

    def update(self, id_: str, partido_: dict) -> dict:
        """

        :param id_:
        :param partido_:
        :return:
        """
        print("update partido")

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete partido")

