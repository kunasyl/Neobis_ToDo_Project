from django import forms

from main.models import ToDoItem

class NewToDoForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ['title', 'text']