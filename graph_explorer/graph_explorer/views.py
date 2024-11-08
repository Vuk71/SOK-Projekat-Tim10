import pkg_resources
from django.http import JsonResponse
from django.shortcuts import render, redirect

from django.apps.registry import apps
import json
import jsonpickle
import pkg_resources

core_config = apps.get_app_config("graph_explorer")

# simple/detailed
selected_visualizer = core_config.platform.get_available_visualizers()[1]
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
    bird_script = pkg_resources.resource_string(__name__, 'static/js/bird_view.js')
    # transform to json
    print("generisani graf: ")
    print(graph)
    print("roots grafa: ")
    print(roots)
    json_data_sources = json.dumps(data_sources)
    return render(request, 'tree_view.html',
                  {'main_script': main_script_decoded,
                   'bird_script': bird_script.decode("utf-8"),
                   'tree_script': tree_script.decode("utf-8"),
                   'graph': graph,
                   'roots': [roots],
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
        core_config.platform.set_graph(core_config.workspaces[core_config.active_workspace]["graph"])
        core_config.platform.set_og_graph(core_config.workspaces[core_config.active_workspace]["og_graph"])
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
                    data_source.set_width(int(width))
                else:
                    data_source.set_width(5)
                if(username != ""):
                    data_source.set_username(username)
                if(password != ""):
                    data_source.set_password(password)

                core_config.platform.set_data_source(data_source)

            if (selected_data_source == "JSON Parser Data Source"):
                json_path = request.POST.get('param1')
                data_source = core_config.get_data_source_plugin(selected_data_source)
                data_source.set_filepath(json_path)
                core_config.platform.set_data_source(data_source)

            core_config.workspaces.append({
                    "graph": core_config.platform.get_graph(),
                    "og_graph": core_config.platform.get_graph(),
                })
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
    node_id =  int(request.GET["node_id"])
    children = []
    print("Node_id:::")
    print(node_id)
    for edge in core_config.platform.get_graph().edges:
        if node_id == edge.source:
            children.append(core_config.platform.get_graph().nodes[edge.target])
        if node_id == edge.target:
            children.append(core_config.platform.get_graph().nodes[edge.source])
    children_json = jsonpickle.encode(children, unpicklable=False)
    print("deca:::")
    print(children)
    return JsonResponse(children_json, safe=False)

def filter(request):
    print("filter")
    og_graph = core_config.platform.get_og_graph()
    if og_graph is None:
        og_graph = core_config.platform.get_graph()
        core_config.platform.set_og_graph(og_graph)

    filtered_graph = core_config.platform.get_graph().filter(request.POST["query"])
    core_config.platform.set_graph(filtered_graph)
    core_config.workspaces[core_config.active_workspace]["graph"] = filtered_graph
    return JsonResponse({'success': True})

def search(request):
    print("search")
    og_graph = core_config.platform.get_og_graph()
    if og_graph is None:
        og_graph = core_config.platform.get_graph()
        core_config.platform.set_og_graph(og_graph)

    searched_graph = core_config.platform.get_graph().search(request.POST["query"])
    core_config.platform.set_graph(searched_graph)
    core_config.workspaces[core_config.active_workspace]["graph"] = searched_graph
    return JsonResponse({'success': True})

def clean(request):
    og_graph = core_config.platform.get_og_graph()
    core_config.platform.set_graph(og_graph)
    core_config.workspaces[core_config.active_workspace]["graph"] = og_graph
    return JsonResponse({'success': True})


def change_visualization(request):

    global selected_visualizer
    if request.method == 'POST':
        visualization_type = request.POST.get('visualization_type')
        # Ovde dodajte logiku za promenu vizualizacije
        # Na primer, ako imate listu dostupnih vizualizatora, možete postaviti selected_visualizer na odgovarajuću vrednost

        available_visualizers = core_config.platform.get_available_visualizers()
        print("visualizers:::")
        print(visualization_type)
        if visualization_type == 'basic':
            print('uso u basic')
            selected_visualizer = core_config.platform.get_available_visualizers()[0]
            return JsonResponse({'success': True})
        else:
            print('uso u detailed')
            selected_visualizer = core_config.platform.get_available_visualizers()[1]
            return JsonResponse({'success': True})
        
            #return JsonResponse({'success': False, 'error': 'Invalid visualization type'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

