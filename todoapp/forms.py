from django import forms

from todoapp.models import ToDoItem


class NewToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'text', 'deadline']
