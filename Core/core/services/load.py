from abc import abstractmethod, ABC


class LoadService(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def load(self, *args):
        pass

