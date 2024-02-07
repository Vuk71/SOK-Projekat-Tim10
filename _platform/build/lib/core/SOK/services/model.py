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
    def __init__(self, source: str, target: str, name: str = "default"):
        self.source = source
        self.target = target
        self.name = name

    def __str__(self):
        return "source: " + self.source + " target: " + self.target + "name: " + self.name