from abc import abstractmethod, ABC


class SqsRepository(ABC):
    @abstractmethod
    def send(self, message, queue_url):
        pass
