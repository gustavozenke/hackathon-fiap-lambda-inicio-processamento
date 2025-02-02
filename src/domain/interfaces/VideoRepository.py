from abc import abstractmethod, ABC

from domain.entitites.video import Video


class VideoRepository(ABC):
    @abstractmethod
    def gravar_metadados_video(self, video: Video) -> None:
        pass
