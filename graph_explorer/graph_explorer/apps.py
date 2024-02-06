import pkg_resources
from django.apps import AppConfig
from core.SOK.core import Platform, VisualizeDataBase, ParseDataBase
class CoreConfig(AppConfig):
    name = 'graph_explorer'
    platform = Platform()

    def ready(self):
        if self.platform is None:
            self.platform = Platform()
            print("plugins: ")
            self.platform.load_available_plugins()

    def get_vizualizator_plugin(self, visualizer_identifier) -> VisualizeDataBase:
        for visualizer in self.platform.get_available_visualizers():
            if visualizer.identifier() == visualizer_identifier:
                return visualizer
        return None

    def get_data_source_plugin(self, data_source_identifier) -> ParseDataBase:
        for data_source in self.platform.get_available_data_sources():
            if data_source.identifier() == data_source_identifier:
                return data_source
        return None


