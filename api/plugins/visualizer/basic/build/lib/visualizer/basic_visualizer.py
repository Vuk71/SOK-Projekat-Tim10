from core.SOK.services.graph import VisualizeDataBase
from core.SOK.services.model import Graph,Node,Edge



class VisualizeBasic(VisualizeDataBase):
    def identifier(self):
        return "VisualizerBasic"

    def name(self):
        return "Basic visualization graph"

    def visualize_graph(self, graph: Graph):
        print("NODOVI")
        print(graph.nodes)
        print("GRNCICE")
        print(graph.edges)