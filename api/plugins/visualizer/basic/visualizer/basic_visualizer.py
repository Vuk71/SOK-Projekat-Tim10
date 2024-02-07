from core.SOK.services.api import VisualizeDataBase
from core.SOK.services.model import Graph,Node,Edge



class VisualizeBasic(VisualizeDataBase):
    def identifier(self):
        return "VisualizerBasic"

    def name(self):
        return "Basic visualization graph"

    def visualize_graph(self, graph: Graph):
        nodes = ""
        edges = ""
        for node in graph.nodes:
            nodes += str(node) + " "
        for edge in graph.edges:
            edges += str(edge) + " "
        string = "Nodovi: " + nodes + " " + "Grane: " + edges
        return string

    def __str__(self):
        return "load_github " + str(type(self))