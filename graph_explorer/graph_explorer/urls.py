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
from .views import index, visualize_graph, index_test, workspace_test, update_active_workspace

urlpatterns = [
    path('', workspace_test, name='workspace_test'),
    path('update_active_workspace/', update_active_workspace, name='update_active_workspace'),
    path('visualize-graph/', visualize_graph, name='visualize_graph'),
    path("admin/", admin.site.urls)
]