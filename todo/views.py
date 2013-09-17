from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo


def list(request):
    todos = Todo.objects.all()
    return render(request, "list.html", {"todos": todos})


def add(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("/todo")
    return render(request, "add.html", {"form": form})
