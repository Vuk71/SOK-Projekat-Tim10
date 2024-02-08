import pkg_resources
import importlib.resources as resources

from _platform.core.SOK.core import VisualizeDataBase

class DetailedVisualizer(VisualizeDataBase):
    def visualize(self):
         return pkg_resources.resource_string(__name__, 'detailed_main_view.js')
        # with resources.open_text(__name__, 'detailed_main_view.js') as f:
        #     return f.read()

    def identifier(self):
        return "detailed_visualizer"


    def name(self):
        return "plugin_for_detailed_visualization"