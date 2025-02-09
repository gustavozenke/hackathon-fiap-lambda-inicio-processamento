from abc import abstractmethod, ABC

from domain.entitites.video import Video


class EnvioProcessamento(ABC):
    @abstractmethod
    def iniciar_processamento(self, video: Video):
        pass
