from ..models.graph import Graph
from abc import ABC, abstractmethod

class VisualizerPlugin(ABC):
    @abstractmethod
    def visualize_graph(self, graph: Graph) -> str:
        """
        Generates HTML code representing the graph.

        Args:
            graph: The Graph object to visualize.

        Returns:
            A string containing the generated HTML code.
        """