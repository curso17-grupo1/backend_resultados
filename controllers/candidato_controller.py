from models.candidato import Candidato
from repositories.candidato_repositories import CandidatoRepository


class CandidatoController:

    def __init__(self):
        """
        Este es el constructor de el CandidatoController
        """
        print("Candidato Controller ready")
        self.candidato_repositories = CandidatoRepository()

    def index(self) -> list:
        """
        Este es el metodo que retorna todos los candidatos
        :param: self
        :return: lista de candidatos
        """
        print("All candidatos")
        return self.candidato_repositories.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("mostrar un candidato")
        candidato = self.candidato_repositories.find_by_id(id_)
        return candidato

    def create(self, candidato_: dict) -> Candidato:
        """

        :param candidato_:
        :return:
        """
        print("crear candidadato")
        candidato = Candidato(candidato_)
        return self.candidato_repositories.save(candidato)

    def update(self, id_: str, candidato_: dict) -> Candidato:
        """

        :param id_:
        :param candidato_:
        :return:
        """
        print("update candidato")
        candidato = Candidato(candidato_)
        return self.candidato_repositories.update(id_, candidato)

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete candidato ")
        return self.candidato_repositories.delete(id_)
