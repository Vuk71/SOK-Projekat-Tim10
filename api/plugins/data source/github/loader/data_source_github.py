from abc import ABC, abstractmethod
from core.services.graph import DataSourceBase
from core.services.model import Graph,Node,Edge

class DataSourcePlugin(DataSourceBase):

    def identifier(self):
        return "Github Data Source"

    def name(self):
        return "Load from github"
    @abstractmethod
    def parse_data(self) -> Graph:
        graph = Graph()
        node1 = Node(id="2",data = {'podatak':'neka vrednost'})
        node2 = Node(id="3",data = {'podatak':'neka druga vrednost'})
        edge = Edge(source = "2",target = "3")
        graph.nodes[node1.id]=node1
        graph.nodes[node2.id]=node2
        graph.edges.append(edge)
        return graph