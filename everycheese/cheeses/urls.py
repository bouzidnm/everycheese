from django.urls import path
from . import views


app_name = "cheeses" # Django wiring to link url to cheeses app
urlpatterns = [
    path( route='',
        view=views.CheeseListView.as_view(),
        name='list' #
    ),
]