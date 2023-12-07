from typing import Dict, List

class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.edges: List[Edge] = []

class Node:
    def __init__(self, id: str, data: Dict):
        self.id = id
        self.data = data

class Edge:
    def __init__(self, source: str, target: str, data: Dict = None):
        self.source = source
        self.target = target
        self.data = data