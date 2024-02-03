from core.SOK.services.model import Graph, Node, Edge
import json

class FileSystemJSONPlugin:
    def __init__(self, filepath: str):
        self.filepath = filepath

    def parse_data(self) -> Graph:
        """Parses the JSON file and constructs the graph."""
        graph = Graph()

        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)

            for node_data in data:
                node_id = node_data["@id"]
                node_data = {key: value for key, value in node_data.items() if not key.startswith("@")}
                node = Node(node_id, node_data)
                graph.nodes[node_id] = node

                for key, value in node_data.items():
                    if key.startswith("@") and key != "@id":
                        if isinstance(value, list):
                            for edge_data in value:
                                ref_id = edge_data["@id"]
                                edge_data = {key: value for key, value in edge_data.items() if not key.startswith("@")}
                                edge_data["@edge_name"] = key[1:]
                                edge = Edge(node_id, ref_id, edge_data)
                                graph.edges.append(edge)
                        else:
                            ref_id = value["@id"]
                            edge_data = {key: value for key, value in value.items() if not key.startswith("@")}
                            edge_data["@edge_name"] = key[1:]
                            edge = Edge(node_id, ref_id, edge_data)
                            graph.edges.append(edge)

        except FileNotFoundError:
            raise ValueError(f"File not found: {self.filepath}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {self.filepath}")

        return graph