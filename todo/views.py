from django.shortcuts import render

from .forms import TodoForm
from .models import Todo


def list(request):
    todos = Todo.objects.all()
    return render(request, {"todos": todos}, "list.html")


def add(request):
    form = TodoForm(request.POST or {})
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, {"form": form}, "add.html")
