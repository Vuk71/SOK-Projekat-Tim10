from abc import abstractmethod, ABC

class VisualizeService(ABC):

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def get_html(self, graph):
        pass
