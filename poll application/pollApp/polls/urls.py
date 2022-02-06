from django.urls import path

# Importing the required views to be rendered
from . import views

urlpatterns = [
    path(route='', view=views.index, name='index')
]