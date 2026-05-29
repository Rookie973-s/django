from django.urls import include, path
from .views import *
urlpatterns = [
    path("create_task/", create_task)   
]
