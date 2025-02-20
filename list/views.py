from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import NewTaskForm
from django.http import JsonResponse
import json

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
        request.session["finished_tasks"] = []
        
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("list:index"))
        else:
            return render(request, "list/index.html", {"form":form,"tasks":request.session["tasks"], "finished_tasks":request.session["finished_tasks"]})
    else:
        form = NewTaskForm()
    return render(request, "list/index.html", {"form":form,"tasks":request.session["tasks"], "finished_tasks":request.session["finished_tasks"]})

def clear(request):
    request.session["tasks"] = []
    return HttpResponseRedirect(reverse("list:index"))


def save_finished_tasks(request):
    if request.method == "POST":
        data = json.loads(request.body)  # دریافت داده‌های JSON
        request.session["finished_tasks"] += data.get("finished_tasks", [])  # استخراج تسک‌ها از داده‌ها

        # اینجا می‌توان داده‌ها را در دیتابیس ذخیره کرد
        print("Received Finished Tasks:", request.session["finished_tasks"]) 
        for task in request.session["tasks"]:
            for ftask in request.session["finished_tasks"]:
                if task == ftask:
                    request.session["tasks"].remove(task) 

        return JsonResponse({"status": "success", "message": "Tasks updated successfully!"})

    return JsonResponse({"status": "error", "message": "Invalid request!"}, status=400)

