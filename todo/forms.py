from django.forms import ModelForm

from .models import Todo


class TodoForm(ModelForm):
    model = Todo
