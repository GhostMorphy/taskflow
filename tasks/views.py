from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/task_list.html", {"tasks": tasks})

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return JsonResponse({"completed": task.completed})


# PR PRACTICE COMMENT       
