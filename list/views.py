from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import NewTaskForm
from .Task import Task
from django.http import JsonResponse
import json

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
        
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = Task(form.cleaned_data["task"])
            request.session["tasks"] += [task.__dict__]  # تبدیل آبجکت‌ها به دیکشنری
            return HttpResponseRedirect(reverse("list:index"))
        else:
            return render(request, "list/index.html", {"form":form,"tasks":request.session["tasks"]})
    else:
        form = NewTaskForm()
    return render(request, "list/index.html", {"form":form,"tasks":request.session["tasks"]})

def clear(request):
    request.session["tasks"] = []
    return HttpResponseRedirect(reverse("list:index"))


def save_tasks(request):
    if request.method == "POST":
        changeItems = json.loads(request.body)  # دریافت داده‌های JSON
        taskName = changeItems["task"]
        status = changeItems["task_status"]
        # اینجا می‌توان داده‌ها را در دیتابیس ذخیره کرد
        print("Received Finished Tasks:", changeItems) 
        print("request session tasks :", request.session["tasks"])
        for dict in request.session["tasks"]:
            if dict["taskname"] == taskName:
                if status == "open":
                    dict["status"] = "open"
                else:
                    dict["status"] = "finished"

        print("request session tasks :", request.session["tasks"])
        return JsonResponse({"status": "success", "message": "Tasks updated successfully!"})

    return JsonResponse({"status": "error", "message": "Invalid request!"}, status=400)

