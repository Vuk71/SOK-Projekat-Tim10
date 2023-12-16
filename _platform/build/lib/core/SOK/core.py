from .services.graph import ParseDataBase, VisualizeDataBase
import pkg_resources


class Platform:
    def __init__(self):
        self.graph = None

    def set_data_source(self, plugin: ParseDataBase) -> None:
        self.graph = plugin.parse_data()

    def get_visualized_graph(self, plugin: VisualizeDataBase) -> str:
        if not self.graph:
            raise Exception("No data source has been set.")
        return plugin.visualize_graph(self.graph)

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