#abstrakte metode za graf (load visualizer filter?)
from abc import ABC, abstractmethod
from typing import List


from .model import *

class ServiceBase(ABC):
    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def name(self):
        pass


class ParseDataBase(ServiceBase):

    @abstractmethod
    def parse_data(self) -> Graph:
        pass

class VisualizeDataBase(ServiceBase):

    @abstractmethod
    def visualize_graph(self, graph: Graph):
        pass
