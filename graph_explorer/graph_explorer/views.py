from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.apps.registry import apps
import json


core_config = apps.get_app_config("graph_explorer")

#simple/detailed
selected_visualizer = core_config.platform.get_available_visualizers()[0]

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
    core_config.platform.set_data_source(core_config.platform.get_available_data_sources()[0])
    return render(request, 'test.html', {'data': core_config.platform.get_visualized_graph(core_config.platform.get_available_visualizators()[0])})


def update_active_workspace(request):
    if request.method == 'POST' and 'active_workspace' in request.POST:
        active_workspace = int(request.POST['active_workspace'])
        core_config.active_workspace = active_workspace
        print("selected workspace: " + str(active_workspace))
        core_config.platform.set_graph(core_config.workspaces[core_config.active_workspace])
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def workspace_test(request):
    print(request.POST)
    # Prikupimo broj workspaces i trenutno aktivni workspace iz CoreConfig klase
    num_workspaces = len(core_config.workspaces)
    active_workspace = core_config.active_workspace
    print("number of workspaces: ")
    print(num_workspaces)
    print("active workspace: ")
    print(str(active_workspace))
    # Provera da li je forma poslata
    if request.method == 'POST':
        # Provera da li je kliknuto dugme "Add Workspace"
        if 'add_workspace' in request.POST:
            selected_data_source = request.POST.get('selected_data_source')
            param1 = ""
            param2 = ""
            if(selected_data_source == "Github Data Source"):
                param1 = request.POST.get('param1')
                data_source = core_config.get_data_source_plugin(selected_data_source)
                data_source.set_account(param1)
                core_config.platform.set_data_source(data_source)

            core_config.workspaces.append(core_config.platform.get_visualized_graph(selected_visualizer))
            core_config.active_workspace = len(core_config.workspaces)-1 # Postavljamo na indeks poslednjeg workspace-a

            print(core_config.active_workspace)

            print("Selected data source:", selected_data_source)
            print("Input param 1:", param1)
            print("Input param 2:", param2)
            return redirect('workspace_test')


    # Kreiramo listu indeksa za svaki workspace
    workspace_indices = range(0, num_workspaces)
    available_data_sources = core_config.platform.get_available_data_sources()

    # Pretvaranje Python objekta u Python dictionary ili listu
    data_sources = [{"id": ds.identifier(), "name": ds.name()} for ds in available_data_sources]
    print(data_sources)
    # Pretvaranje u JSON format
    json_data_sources = json.dumps(data_sources)

    # Renderujemo template sa prosleđenim kontekstom
    return render(request, 'workspace.html', {'data_sources': json_data_sources, 'workspaces': workspace_indices})

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