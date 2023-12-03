from django.shortcuts import redirect, render
from django.apps.registry import apps
import pkg_resources
import json
import copy


def search(request):
    term = request.GET.get("term")
    graph = apps.get_app_config('core').graph
    searched_graph = graph.search(term)
    apps.get_app_config('core').graph = searched_graph
    return redirect("/")


def filter(request):
    query = request.GET.get("query")
    graph = apps.get_app_config('core').graph
    filtered_graph = graph.filter(query)
    apps.get_app_config('core').graph = filtered_graph
    return redirect("/")


def simple(request):
    apps.get_app_config('core').view = apps.get_app_config('core').SIMPLE
    return redirect("/")


def block(request):
    apps.get_app_config('core').view = apps.get_app_config('core').BLOCK
    return redirect("/")


def treeview_birdview(graph):
  if graph is None:
    return {"data": json.dumps({})}

  root_id = None
  full_data = {}

  for node_id in graph.data:
      root_id = node_id
      break
  for node_id in graph.data:
      node = graph.data[node_id]
      if node_id not in full_data:
          full_data[node_id] = {"name": node_id,
                                "parent": "", "info": "", "children": []}
      full_data[node_id]["info"] = node.__str__().replace("\n", "     ")
      for edge in node.edges:
          full_data[node_id]["children"].append({"name": edge.second_node})
          if edge.second_node not in full_data:
              full_data[edge.second_node] = {"name": edge.second_node, "parent": "", "info": node.__str__(
              ).replace("\n", "     "), "children": []}
          full_data[edge.second_node]["parent"] = str(node_id)

  all_data = {
      root_id: full_data,
  }

  context = {'data': json.dumps(all_data)}
  return context


def index(request):
    og_graph = apps.get_app_config('core').og_graph
    graph = apps.get_app_config('core').graph
    view_type = apps.get_app_config('core').view
    plugins = apps.get_app_config('core').loaded_plugins

    context = {
        "title": "Index",
        "code": ""
    }

    for plugin in plugins:
        context[plugin] = plugins[plugin]

    if graph is None or view_type is None:
        return render(request, "index.html", context)

    if view_type == apps.get_app_config('core').SIMPLE:
        svp = apps.get_app_config('core').loaded_plugins["svp_plugin"]
        context["code"] = svp.get_html(graph)
    else:
        bvp = apps.get_app_config('core').loaded_plugins["bvp_plugin"]
        context["code"] = bvp.get_html(graph)

    treeview_birdview_context = treeview_birdview(og_graph)

    for key in treeview_birdview_context:
        context[key] = treeview_birdview_context[key]

    return render(request, "index.html", context)
