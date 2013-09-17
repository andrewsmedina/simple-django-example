from django.shortcuts import render

from .forms import TodoForm
from .models import Todo


def list(request):
    todos = Todo.objects.all()
    return render(request, {"todos": todos}, "list.html")
