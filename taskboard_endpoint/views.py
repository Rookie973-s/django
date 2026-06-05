from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .models import *
import json
# Create your views here.


def create_task(request):
    if request.method == "POST":
        try:
            body = request.body.decode("utf-8")

            if not body:
                return JsonResponse({"error": "Empty request body"}, status=400)

            data = json.loads(body)

            task = TaskboardDetails.objects.create(
                task_title=data.get("task_title"),
                task_description=data.get("task_description")
            )

            return JsonResponse({
                "message": "Task created successfully",
                "task_id": task.id
            })

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Not a POST request"}, status=405)
   
def get_all_tasks(request):
    if request.method == "GET":
        all_task = TaskboardDetails.objects.all()
        data = []

        for task in all_task:
           data.append({
                "id": task.id,
                "task_title": task.task_title,
                "task_description": task.task_description,
                "task_created_date": task.task_created_date,
                "task_updated_date": task.task_updated_date
            })
        return JsonResponse({"tasks": data})
    else:
        return JsonResponse({"error": "Not a GET request"}, status=405)
    
    
def update_task(request, task_id):
    if request.method == "PATCH":
        task = get_object_or_404(TaskboardDetails, pk=task_id)
        data = json.loads(request.body.decode("utf-8"))

        if "task_title" in data:
            task.task_title = data["task_title"]
        if "task_description" in data:
            task.task_description = data["task_description"]


        task.save()
        return JsonResponse({"message": "Task updated successfully"})
    else:        
        return JsonResponse({"error": "Not a PATCH request"}, status=405)
    
def delete_task(request, task_id):
    if request.method == "DELETE":
        task = get_object_or_404(TaskboardDetails, pk=task_id)
        task.delete()
        return JsonResponse({"message": f"The task with id {task_id} has been deleted successfully"})
    else:
        return JsonResponse({"error": "Not a DELETE request"}, status=405)