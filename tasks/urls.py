from django.urls import path
from .views import task_list, toggle_task

urlpatterns = [
    path("", task_list, name="task-list"),
    path("toggle/<int:task_id>/", toggle_task, name="toggle-task"),
]
