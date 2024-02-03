import pkg_resources
from django.apps import AppConfig
from core.SOK.core import Platform
class CoreConfig(AppConfig):
    name = 'graph_explorer'
    platform = Platform()



