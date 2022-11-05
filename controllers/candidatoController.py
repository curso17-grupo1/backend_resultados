from models.candidato import Candidato


class CandidatoController:

    def __init__(self):
        """
        Este es el constructor de el CandidatoController
        """
        print("Candidato Controller ready")

    def index(self) -> list:
        """
        Este es el metodo que retorna todos los candidatos
        :param: self
        :return: lista de candidatos
        """
        print("All candidatos")
        data = {
            "_id": "abc123",
            "cedula": "79001122",
            "nombre": "Petrosky",
            "lema": "Trabajar, trabajar y trabajar",
        }
        print(data)
        candidato = Candidato(data)
        return[candidato.__dict__]

    # Equivalente a 'uno por el elemento'
    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("mostrar un candidato")
        data = {
            "_id": id_,
            "cedula": "79001122",
            "nombre": "Petrosky",
            "lema": "Trabajar, trabajar y trabajar"
        }
        candidato = Candidato(data)
        return candidato.__dict__

    # equivalente a agregar
    def create(self, candidato_: dict) -> dict:
        """

        :param candidato_:
        :return:
        """
        print("crear candidadato")
        candidato = Candidato(candidato_)
        return candidato.__dict__

    def update(self, id_: str, candidato_: dict) -> dict:
        """

        :param id_:
        :param candidato_:
        :return:
        """
        print("update candidato")
        data = candidato_
        data['_id'] = id_
        candidato = Candidato(data)
        return candidato.__dict__

    def delete(self, id_: str) -> dict:
        print("delete candidato " + id_)
        return {"Borramos un elemento": 1}
