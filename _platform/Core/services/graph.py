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


class GraphLoadBase(ServiceBase):

    @abstractmethod
    def ucitati_fakultete(self) -> List[Fakultet]:
        pass
