#node edges graph


from typing import Dict, List

class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.edges: List[Edge] = []

    def __str__(self) -> str:
        node_str = '\n'.join(str(node) for node in self.nodes.values())
        edge_str = '\n'.join(str(edge) for edge in self.edges)
        return f"#node\n{node_str}\n\n#edges\n{edge_str}"

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