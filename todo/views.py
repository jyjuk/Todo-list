from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from todo.forms import TaskForm, TagForm
from todo.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all().order_by("is_done", "-created_at")
    return render(request, "todo/index.html", {"tasks": tasks})


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:index")


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "todo/tag_list.html", {"tags": tags})


def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:index")
    else:
        form = TaskForm()
    return render(request, "todo/task_form.html", {"form": form})


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("todo:index")
    else:
        form = TaskForm(instance=task)
    return render(request, "todo/task_form.html", {"form": form})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("todo:index")


def add_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo:tag_list")
    else:
        form = TagForm()
    return render(request, "todo/tag_form.html", {"form": form})


def update_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return redirect("todo:tag_list")
    else:
        form = TagForm(instance=tag)
    return render(request, "todo/tag_form.html", {"form": form})


def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    tag.delete()
    return redirect("todo:tag_list")
