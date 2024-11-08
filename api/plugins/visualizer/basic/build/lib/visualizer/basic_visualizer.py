from core.SOK.services.api import VisualizeDataBase
from core.SOK.services.model import Graph,Node,Edge
import pkg_resources



class VisualizeBasic(VisualizeDataBase):
    #  def identifier(self):
    #     return "VisualizerBasic"
    #
    # def name(self):
    #     return "Basic visualization graph"
    #
    # def visualize_graph(self, graph: Graph):
    #     nodes = ""
    #     edges = ""
    #     for node in graph.nodes:
    #         nodes += str(node) + " "
    #     for edge in graph.edges:
    #         edges += str(edge) + " "
    #     string = "Nodovi: " + nodes + " " + "Grane: " + edges
    #     return string
    #
    # def __str__(self):
    #     return "load_github " + str(type(self))
    #
    def visualize_graph(self, graph:Graph):
        return pkg_resources.resource_string(__name__, 'basic_main_view.js')

    def identifier(self):
        return "basic_visualizer"

    def name(self):
        return "plugin_for_basic_visualization"