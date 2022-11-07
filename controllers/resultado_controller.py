from models.resultado import Resultado
from repositories.resultados_repositories import ResultadoRepository


class ResultadoController:

    def __init__(self):
        """
        :return:
        """
        print("Resultado Controller ready")
        self.resultado_repositories = ResultadoRepository()

    def index(self) -> list:
        """

        :param: self
        :return:
        """
        print("All resultado")
        return self.resultado_repositories.find_all()

    def show(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("mostrar un resultado")
        resultado = self.resultado_repositories.find_by_id(id_)
        return resultado

    def create(self, resultado_: dict) -> Resultado:
        """

        :param resultado_:
        :return:
        """
        print("crear resultado")
        resultado = Resultado(resultado_)
        return self.resultado_repositories.save(resultado)

    def update(self, id_: str, resultado_: dict) -> Resultado:
        """

        :param id_:
        :param resultado_:
        :return:
        """
        print("update resultado")
        resultado = Resultado(resultado_)
        return self.resultado_repositories.update(id_, resultado)

    def delete(self, id_: str) -> dict:
        """

        :param id_:
        :return:
        """
        print("delete resultado")
        return self.resultado_repositories.delete(id_)
