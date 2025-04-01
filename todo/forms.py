# todo/forms.py
from django import forms
from .models import TodoModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'description', 'completed']
