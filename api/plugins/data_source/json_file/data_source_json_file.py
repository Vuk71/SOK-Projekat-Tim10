from core.SOK.services.model import Graph, Node, Edge
from core.SOK.services.api import ParseDataBase
import json

class FileSystemJSONPlugin(ParseDataBase):

    def __init__(self):
        self.filepath = None

    def get_filepath(self):
        return self.filepath
    
    def set_filepath(self, filepath):
        self.filepath = filepath

    def identifier(self):
        return "JSON Parser Data Source"

    def name(self):
        return "Load from a JSON file"

    def parse_data(self) -> Graph:
        """Parses the JSON file and constructs the graph."""
        graph = Graph()

        try:
            with open(self.filepath, "r") as f:
                data = json.load(f)

            for node_data in data:
                node_id = node_data["@id"]
                node_data_attributes = {key: value for key, value in node_data.items() if not key.startswith("@")}
                node = Node(node_id, node_data_attributes)
                graph.add_node(node)

                for key, value in node_data.items():
                    if key.startswith("@") and key != "@id":
                        if isinstance(value, list):
                            for ref_id in value:
                                edge = Edge(node_id, ref_id, key[1:])
                                graph.add_edge(edge)
                        else:
                            ref_id = value
                            edge = Edge(node_id, ref_id, key[1:])
                            graph.add_edge(edge)

        except FileNotFoundError:
            raise ValueError(f"File not found: {self.filepath}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {self.filepath}")

        return graph
    
if __name__=="__main__":
    data_source = FileSystemJSONPlugin()
    data_source.set_filepath("C:\SOK_TEST\json_test.json")
    graph = data_source.parse_data()
    print(graph)