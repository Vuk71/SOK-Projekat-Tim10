from django.apps import AppConfig
import pkg_resources


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'
    og_graph = None
    graph = None
    SIMPLE = "simple"
    BLOCK = "block"
    view = None
    loaded_plugins = {}

    def ready(self):
        svp_plugins = load_plugins("svp_plugin")
        bvp_plugins = load_plugins("bvp_plugin")
        self.loaded_plugins["svp_plugin"] = svp_plugins[0] if len(
            svp_plugins) > 0 else None
        self.loaded_plugins["bvp_plugin"] = bvp_plugins[0] if len(
            bvp_plugins) > 0 else None


def load_plugins(group):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=group):
        p = ep.load()
        print("{} {}".format(ep.name, p))
        print(p)
        plugin = p()
        plugins.append(plugin)
    return plugins
