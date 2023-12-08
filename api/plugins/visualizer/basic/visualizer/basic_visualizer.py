from typing import List

from core.sevices.model import Graph
from core.sevices.graph import VisualizeDataBase


class VisualizeBasic(VisualizeDataBase):
    def identifier(self):
        return "VisualizerBasic"

    def name(self):
        return "Basic visualization graph "

    def visualize_graph(self, graph: Graph):
        print(graph)