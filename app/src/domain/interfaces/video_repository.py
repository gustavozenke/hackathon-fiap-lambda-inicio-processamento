from abc import abstractmethod, ABC


class VideoRepository(ABC):
    @abstractmethod
    def put_item(self, item: dict) -> dict:
        pass
