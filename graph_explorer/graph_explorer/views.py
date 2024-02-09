from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.apps.registry import apps
import json
import jsonpickle
import pkg_resources

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
        main_script, bird_script, tree_script = core_config.platform.get_visualized_graph(selected_visualizer)
    except Exception as e:
        print(f"An exception occurred: {e}")
        main_script = ""
        bird_script = ""
        tree_script= ""
    roots = "nema"
    graph = "nema"
    if core_config.platform.get_graph():
        roots = core_config.platform.get_graph().get_roots()
        graph = core_config.platform.get_graph()

    main_script_decoded = ""
    if main_script != "":
        main_script_decoded = main_script.decode("utf-8")

    tree_script = pkg_resources.resource_string(__name__, 'static/js/tree_view.js')
    # transform to json
    json_data_sources = json.dumps(data_sources)
    return render(request, 'tree_view.html',
                  {'main_script': main_script_decoded,
                   'bird_script': bird_script,
                   'tree_script': tree_script.decode("utf-8"),
                   'graph': graph,
                   'roots': roots,
                   'data_sources': json_data_sources,
                   'workspaces': workspace_indices}
                  )


# take graph from workspaces and set it on platform
def update_active_workspace(request):
    print("ovde je upao")
    if request.method == 'POST' and 'active_workspace' in request.POST:
        print("updated")
        active_workspace = int(request.POST['active_workspace'])
        core_config.active_workspace = active_workspace
        core_config.platform.set_graph(core_config.workspaces[core_config.active_workspace])
        return JsonResponse({'success': True})
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
            return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def visualize_graph(request):
    core_config.platform.set_data_source(core_config.platform.get_available_data_sources()[0])
    return render(request, 'test.html', {'data': core_config.platform.get_visualized_graph(selected_visualizer)})



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


def get_children(request):
    node_id =  request.GET["node_id"]
    children = []
    for edge in core_config.platform.get_graph().edges:
        if node_id == edge.source:
            children.append(edge.destination)
    children_json = jsonpickle.encode(children, unpicklable=False)
    return JsonResponse(children_json, safe=False)

