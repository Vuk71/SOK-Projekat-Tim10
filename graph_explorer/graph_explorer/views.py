from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.apps.registry import apps
import json

core_config = apps.get_app_config("graph_explorer")

# simple/detailed
selected_visualizer = core_config.platform.get_available_visualizers()[0]
available_data_sources = core_config.platform.get_available_data_sources()

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

    return render(request, 'index.html',
                  {'data_sources': get_available_data_sources(), 'visualizers': get_available_visualizers()})


def index_test(request):
    data_sources = [{"id": ds.identifier(), "name": ds.name()} for ds in available_data_sources]
    workspace_indices = range(0, len(core_config.workspaces))
    try:
        data, bird_view, tree_view = core_config.platform.get_visualized_graph(selected_visualizer)
    except:
        data = "no data source selected"
        bird_view = "no data"
        tree_view= "no data"
    # transform to json
    json_data_sources = json.dumps(data_sources)
    return render(request, 'test.html', {'data': data, 'bird' : bird_view, 'tree' : tree_view,
                                         'data_sources': json_data_sources,
                                         'workspaces': workspace_indices})


# take graph from workspaces and set it on platform
def update_active_workspace(request):
    print("ovde je upao")
    if request.method == 'POST' and 'active_workspace' in request.POST:
        print("updated")
        active_workspace = int(request.POST['active_workspace'])
        core_config.active_workspace = active_workspace
        core_config.platform.set_graph(core_config.workspaces[core_config.active_workspace])
        data = core_config.platform.get_visualized_graph(selected_visualizer)
        return JsonResponse({'success': False, 'data':data})
    return JsonResponse({'success': False})


# change graph on platform based on selected data source and add it to workspaces
def workspace_test(request):

    # check if form was sent
    if request.method == 'POST':
        # if clicked on add workspace
        if 'add_workspace' in request.POST:
            # get selected data source
            selected_data_source = request.POST.get('selected_data_source')

            # get params based on data source
            param1 = ""
            param2 = ""
            param3 = ""
            param4 = ""

            # make data source and send it to platform to make a graph with it
            if (selected_data_source == "Github Data Source"):
                param1 = request.POST.get('param1')
                data_source = core_config.get_data_source_plugin(selected_data_source)
                data_source.set_account(param1)
                core_config.platform.set_data_source(data_source)

            if (selected_data_source == "Instagram Data Source"):
                profile = request.POST.get('param1')
                width = request.POST.get('param2')
                username = request.POST.get('param3')
                password = request.POST.get('param4')
                print("profile: " + profile)
                print("width: " + width)
                print("username: " + username)
                print("password: " +password)
                data_source = core_config.get_data_source_plugin(selected_data_source)
                if(profile != ""):
                    data_source.set_profile(profile)
                if(width != ""):
                    data_source.set_width(width)
                if(username != ""):
                    data_source.set_username(username)
                if(password != ""):
                    data_source.set_password(password)

                core_config.platform.set_data_source(data_source)

            core_config.workspaces.append(core_config.platform.get_graph())
            core_config.active_workspace = len(core_config.workspaces) - 1  # Postavljamo na indeks poslednjeg workspace-a
            return redirect('index_test')

    return redirect('index_test')

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
