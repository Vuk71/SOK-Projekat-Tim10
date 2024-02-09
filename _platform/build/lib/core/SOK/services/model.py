from typing import Dict, List

class Node:
    def __init__(self, id: int, data: Dict):
        self.id = id
        self.data = data

    def __str__(self):
        return "ID: " + str(self.id) + " Data: " + str(self.data)

class Edge:
    def __init__(self, source: int, target: int, name: str = ""):
        self.source = source
        self.target = target
        self.name = name

    def __str__(self):
        return "Source Node ID: " + str(self.source) + " Target Node ID: " + str(self.target) + " Edge Name: " + self.name

class Graph:
    def __init__(self):
        self.nodes: Dict[int, Node] = {}
        self.edges: List[Edge] = []

    def __str__(self) -> str:
        node_str = '\n'.join(str(node) for node in self.nodes.values())
        edge_str = '\n'.join(str(edge) for edge in self.edges)
        return f"# Graph Nodes:\n{node_str}\n\n# Graph Edges:\n{edge_str}"
    
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
        attribute, comparator_value = filter_query.split(None, 1)
        comparator, value = comparator_value.split()
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

if __name__ == "__main__":
    graph = Graph()
    graph.add_node(Node(1, {"name": "John", "age": 25}))
    graph.add_node(Node(2, {"name": "Jane", "age": 30, "searchFilter": True}))
    graph.add_node(Node(3, {"name": "Alice", "age": 20}))
    graph.add_edge(Edge(1, 2, "friend"))
    graph.add_edge(Edge(2, 3, "friend"))
    print(graph)
    print("\n==========\n")
    print(graph.search("searchFilter"))
    print("\n==========\n")
    print(graph.filter("age >= 25"))