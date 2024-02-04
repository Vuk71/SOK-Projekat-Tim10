from .services.api import ParseDataBase, VisualizeDataBase
import pkg_resources


class Platform:
    def __init__(self):
        self.graph = None
        self.data_sources = []
        self.data_visualizers = []

    def set_data_source(self, plugin: ParseDataBase) -> None:
        self.graph = plugin.parse_data()

    def get_visualized_graph(self, plugin: VisualizeDataBase) -> str:
        if not self.graph:
            raise Exception("No data source has been set.")
        return plugin.visualize_graph(self.graph)

    def load_available_plugins(self):
        self.data_sources = load_plugins("graph.load")
        self.data_visualizers = load_plugins("graph.visualizer")

    def get_available_data_sources(self) -> list[ParseDataBase]:
        return self.data_sources
    def get_available_visualizators(self) -> list[VisualizeDataBase]:
        return self.data_visualizers


    def platform_test(self) -> str:
        dataLoader = load_plugins("graph.load")
        dataVisualizer = load_plugins("graph.visualizer")
        self.graph = dataLoader[0].parse_data()
        return dataVisualizer[0].visualize_graph(self.graph)


def load_plugins(oznaka):
    """
    Dinamicko prepoznavanje plagina na osnovu pripadajuce grupe.
    """
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=oznaka):
        # Ucitavanje plagina.
        p = ep.load()
        print(f"{ep.name} {p}")
        # instanciranje odgovarajuce klase
        plugin = p()
        plugins.append(plugin)
    return plugins