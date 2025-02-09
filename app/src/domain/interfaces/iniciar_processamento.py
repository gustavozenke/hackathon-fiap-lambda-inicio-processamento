from abc import abstractmethod, ABC


class IniciarProcessamento(ABC):
    @abstractmethod
    def execute(self, nome_video, tamanho):
        pass
