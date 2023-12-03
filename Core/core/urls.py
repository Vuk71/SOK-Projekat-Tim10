from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('treeview_birdview', views.treeview_birdview),
    path('simple', views.simple),
    path('block', views.block),
    path('search', views.search),
    path('filter', views.filter)
]
