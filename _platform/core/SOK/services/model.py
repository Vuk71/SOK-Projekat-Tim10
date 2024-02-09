#node edges graph


from typing import Dict, List
#import json

class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.edges: List[Edge] = []

    def get_roots(self):
        # Stvorite skup odredišnih čvorova iz bridova
        targets = set(edge.target for edge in self.edges)

        # Inicijalizirajte listu korijenskih čvorova
        roots = []

        # Iterirajte kroz sve čvorove grafa
        for node_id, node in self.nodes.items():
            # Ako čvor nije odredište nijednog brida, dodajte ga u listu korijenskih čvorova
            if node_id not in targets:
                roots.append(node)

        return roots


    def __str__(self) -> str:
        node_str = '\n'.join(str(node) for node in self.nodes.values())
        edge_str = '\n'.join(str(edge) for edge in self.edges)
        return f"#node\n{node_str}\n\n#edges\n{edge_str}"

class Node:
    def __init__(self, id: int, data: Dict):
        self.id = id
        self.data = data

    def __str__(self):
        return " id: " + str(self.id) + " data: " + str(self.data)

class Edge:
    def __init__(self, source: str, target: str, name: str = "default"):
        self.source = source
        self.target = target
        self.name = name

    def __str__(self):
        return "source: " + str(self.source) + " target: " + str(self.target) + " name: " + self.name

    #
    #
    # graph = Graph()
    # nodes_data = {node_id: {"name": node.id, "attributes": node.data} for node_id, node in graph.nodes.items()}
    # edges_data = [{"source": edge.source, "target": edge.target} for edge in graph.edges]
    # nodes_json = json.dumps(nodes_data)
    # edges_json = json.dumps(edges_data)
