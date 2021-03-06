from django.urls import path
from . import views


app_name = "cheeses" # Django wiring to link url to cheeses app
urlpatterns = [
    path( route='', # be explicit here
        view=views.CheeseListView.as_view(),
        name='list'
    ),
    path( route='<slug:slug>/',
        view=views.CheeseDetailView.as_view(),
        name='detail'
    ),
    path(
        route='add/new/',
        view=views.CheeseCreateView.as_view(),
        name='add'
    ),
    path( route='<slug:slug>/update/',
        view=views.CheeseUpdateView.as_view(),
        name='update'
    ),
]