from abc import ABC, abstractmethod
from typing import Union
from ..models.graph import Graph

class DataSourcePlugin(ABC):
    @abstractmethod
    def parse_data(self, data: Union[str, bytes]) -> Graph:
        """
        Parses data and constructs a Graph object.

        Args:
            data: The data to parse.

        Returns:
            A Graph object.
        """