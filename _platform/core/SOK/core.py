from _platform.core.SOK.services import ParseDataBase, VisualizeDataBase


class Platform:
    def __init__(self):
        self.graph = None

    def set_data_source(self, plugin: ParseDataBase) -> None:
        self.graph = plugin.parse_data()

    def get_visualized_graph(self, plugin: VisualizeDataBase) -> str:
        if not self.graph:
            raise Exception("No data source has been set.")
        return plugin.visualize_graph(self.graph)

    def load_plugins(oznaka):
        pass