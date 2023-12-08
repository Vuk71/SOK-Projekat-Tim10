from ..api.plugins.data_source import DataSourcePlugin
from ..api.plugins.visualization import VisualizerPlugin
from typing import Union

class Platform:
    def __init__(self):
        self.graph = None

    def set_data_source(self, plugin: DataSourcePlugin, data: Union[str, bytes]) -> None:
        self.graph = plugin.parse_data(data)

    def get_visualized_graph(self, plugin: VisualizerPlugin) -> str:
        if not self.graph:
            raise Exception("No data source has been set.")
        return plugin.visualize_graph(self.graph)