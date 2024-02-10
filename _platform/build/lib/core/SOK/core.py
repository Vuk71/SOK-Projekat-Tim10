from .services.api import ParseDataBase, VisualizeDataBase
import pkg_resources


from .services.api import ParseDataBase, VisualizeDataBase
import pkg_resources


class Platform:
    def __init__(self):
        self.graph = None
        self.og_graph = None
        self.data_sources = []
        self.data_visualizers = []

    def set_graph(self,graph):
        self.graph = graph

    def get_graph(self):
        return self.graph

    def set_og_graph(self,graph):
        self.og_graph = graph

    def get_og_graph(self):
        return self.og_graph

    def set_data_source(self, plugin: ParseDataBase) -> None:
        self.graph = plugin.parse_data()

    def get_visualized_graph(self, plugin: VisualizeDataBase):
        if not self.graph:
            raise Exception("No data source has been set.")
        return plugin.visualize_graph(self.graph), "bird view", "tree view"

    def load_available_plugins(self):
        self.data_sources = load_plugins("graph.load")
        self.data_visualizers = load_plugins("graph.visualizer")

    def get_available_data_sources(self) -> list[ParseDataBase]:
        return self.data_sources
    def get_available_visualizers(self) -> list[VisualizeDataBase]:
        return self.data_visualizers


    def platform_test(self) -> str:
        self.data_sources = load_plugins("graph.load")
        self.data_visualizers = load_plugins("graph.visualizer")
        self.graph = self.data_sources[0].parse_data()
        return self.data_visualizers[0].visualize_graph(self.graph)


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