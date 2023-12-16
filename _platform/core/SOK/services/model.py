#node edges graph


from typing import Dict, List

class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.edges: List[Edge] = []

class Node:
    def __init__(self, id: str, data: Dict):
        self.id = id
        self.data = data

    def __str__(self):
        return " id: " + self.id + " data: " + str(self.data)

class Edge:
    def __init__(self, source: str, target: str, data: Dict = None):
        self.source = source
        self.target = target
        self.data = data

    def __str__(self):
        if self.data == None:
            return "source: " + self.source + " target: " + self.target + " data: None "
        return "source: " + self.source + " target: " + self.target + " data: " + str(self.data)