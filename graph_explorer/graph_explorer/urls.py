"""
URL configuration for graph_explorer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_test, name='index_test'),
    path('add_workspace/', views.workspace_test, name='add_workspace'),
    path('update_active_workspace/', views.update_active_workspace, name='update_active_workspace'),
    path('change_visualization/', views.change_visualization, name='change_visualization'),
    path('visualize-graph/', views.visualize_graph, name='visualize_graph'),
    path('get_children', views.get_children, name="get_children"),
    path("admin/", admin.site.urls)
]