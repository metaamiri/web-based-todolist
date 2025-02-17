from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import NewTaskForm

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"]=[]
        
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            print(request.session["tasks"])
            return HttpResponseRedirect(reverse("list:index"))
        else:
            return render(request, "list/index.html", {"form":form,"tasks":request.session["tasks"]})
    else:
        form = NewTaskForm()
    return render(request, "list/index.html", {"form":form,"tasks":request.session["tasks"]})
