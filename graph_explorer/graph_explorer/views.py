from django.shortcuts import render, redirect

from django.apps.registry import apps
from core.SOK.services.api import ParseDataBase, VisualizeDataBase
from core.SOK.core import Platform

platform = Platform()


def index(request):
    # Handle user interactions, list available data sources and visualizers
    # ...
    # Load chosen data source and visualizer plugins
    data_source_plugin = get_data_source_plugin(request.POST['data_source'])
    visualizer_plugin = get_visualizer_plugin(request.POST['visualizer'])

    if request.method == 'POST':
        # Parse data and generate visualization
        apps.get_app_config("graph_explorer").platform.set_data_source(data_source_plugin)
        visualized_graph = apps.get_app_config("graph_explorer").platform.get_visualized_graph(visualizer_plugin)
        return render(request, 'graph.html', {'visualized_graph': visualized_graph})

    return render(request, 'index.html', {'data_sources': get_available_data_sources(), 'visualizers': get_available_visualizers()})

def index_test(request):
    print(apps.get_app_config("graph_explorer"))
    return render(request, 'test.html', {'data': apps.get_app_config("graph_explorer").platform.platform_test()})


def visualize_graph(request):
    pass
    # ...

def get_data_source_plugin(name):
    pass
    # Implement logic to retrieve the specific data source plugin based on the provided name
    # ...

def get_visualizer_plugin(name):
    pass
    # Implement logic to retrieve the specific visualizer plugin based on the provided name
    # ...

def get_available_data_sources():
    pass
    # Implement logic to discover and return available data source plugins
    # ...

def get_available_visualizers():
    pass
    # Implement logic to discover and return available visualizer plugins
    # ...