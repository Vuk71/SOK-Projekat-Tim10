from core.SOK.services.graph import ParseDataBase
from core.SOK.services.model import Graph,Node,Edge
import json
from typing import Dict, List

class FileSystemJSONPlugin:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def parse_data(self) -> Graph:
        """Parses the JSON file and constructs the graph."""
        graph = Graph()

        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)

            # Create the root node
            root_node = self._create_node_and_children(data, graph)

        except FileNotFoundError:
            raise ValueError(f"File not found: {self.filepath}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {self.filepath}")

        return graph

    def _create_node_and_children(self, node_data: Dict, graph: Graph) -> Node:
        """Creates a node and its children recursively."""
        node_id = node_data["@id"]
        node = Node(node_id, node_data)
        graph.nodes[node_id] = node

        for key, child_data in node_data.items():
            if isinstance(child_data, list):
                for child_item in child_data:
                    child_node = self._create_node_and_children(child_item, graph)
                    edge = Edge(node_id, child_node.id)
                    graph.edges.append(edge)
            elif isinstance(child_data, dict):
                child_node = self._create_node_and_children(child_data, graph)
                edge = Edge(node_id, child_node.id)
                graph.edges.append(edge)

        return node