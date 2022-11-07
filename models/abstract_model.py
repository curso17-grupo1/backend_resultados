from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):

    def __init__(self, data: dict):
        """
        Este es el constructor que es usado para trasnformar un diccionario llamado data
        en un objeto con
        :param data: data para convertir en objeto
        """
        for key, value in data.items():
            setattr(self, key, value)
