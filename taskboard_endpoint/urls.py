from django.urls import include, path
from .views import *
urlpatterns = [
    path("create_task/", create_task),
    path("all_tasks/", get_all_tasks),
    path("update_task/<int:task_id>/update_task/", update_task),
   path("delete_task/<int:task_id>/delete_task/", delete_task)
]

