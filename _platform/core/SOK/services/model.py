from typing import Dict, List
#import json

class Node:
    def __init__(self, id: str, data: Dict):
        self.id = id
        self.data = data

    def __str__(self):
        return " id: " + self.id + " data: " + str(self.data)

class Edge:
    def __init__(self, source: str, target: str, name: str = ""):
        self.source = source
        self.target = target
        self.name = name

    def __str__(self):
        return "source: " + self.source + " target: " + self.target + "name: " + self.name

<<<<<<< Updated upstream
    #
    #
    # graph = Graph()
    # nodes_data = {node_id: {"name": node.id, "attributes": node.data} for node_id, node in graph.nodes.items()}
    # edges_data = [{"source": edge.source, "target": edge.target} for edge in graph.edges]
    # nodes_json = json.dumps(nodes_data)
    # edges_json = json.dumps(edges_data)
=======
class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.edges: List[Edge] = []

    def __str__(self) -> str:
        node_str = '\n'.join(str(node) for node in self.nodes.values())
        edge_str = '\n'.join(str(edge) for edge in self.edges)
        return f"#node\n{node_str}\n\n#edges\n{edge_str}"
    
    def add_node(self, node: Node) -> None:
        self.nodes[node.id] = node

    def add_edge(self, edge: Edge) -> None:
        self.edges.append(edge)
    
    def search(self, query: str) -> 'Graph':
        subgraph = Graph()
        for node in self.nodes.values():
            for attr_key, attr_value in node.data.items():
                if (query in attr_key) or (query in str(attr_value)):
                    subgraph.add_node(node)
                    break
        subgraph.edges = [edge for edge in self.edges if edge.source in subgraph.nodes and edge.target in subgraph.nodes]
        return subgraph

    def filter(self, filter_query: str) -> 'Graph':
        attribute_comparator, rest = filter_query.split(None, 1)
        attribute, comparator = attribute_comparator.split()
        value = rest.strip()
        subgraph = Graph()
        for node in self.nodes.values():
            if attribute not in node.data:
                continue
            node_value = node.data[attribute]
            try:
                if comparator == "==":
                    if node_value == type(node_value)(value):
                        subgraph.add_node(node)
                elif comparator == ">":
                    if node_value > type(node_value)(value):
                        subgraph.add_node(node)
                elif comparator == ">=":
                    if node_value >= type(node_value)(value):
                        subgraph.add_node(node)
                elif comparator == "<":
                    if node_value < type(node_value)(value):
                        subgraph.add_node(node)
                elif comparator == "<=":
                    if node_value <= type(node_value)(value):
                        subgraph.add_node(node)
                elif comparator == "!=":
                    if node_value != type(node_value)(value):
                        subgraph.add_node(node)
                else:
                    raise ValueError(f"Operator {comparator} is not supported.")
            except ValueError:
                raise ValueError(f"The value {value} is not of the appropriate type for the attribute {attribute}.")
        subgraph.edges = [edge for edge in self.edges if edge.source in subgraph.nodes and edge.target in subgraph.nodes]
        return subgraph
>>>>>>> Stashed changes
