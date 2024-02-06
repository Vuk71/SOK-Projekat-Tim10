import pkg_resources
import importlib.resources as resources

from _platform.core.SOK.core import VisualizeDataBase
from _platform.core.SOK.services.model import Graph


class DetailedVisualizer(VisualizeDataBase):
    def identifier(self):
        return "VisualizerDetailed"

    def name(self):
        return "Detailed visualization graph"

    def visualize_graph(self, graph: Graph):
        nodes = ""
        edges = ""
        for node in graph.nodes.values():
            nodes += str(node) + " "
        for edge in graph.edges:
            edges += str(edge) + " "
        string = "Nodovi: " + nodes + " " + "Grane: " + edges
        return string