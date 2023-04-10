from django.shortcuts import render

from . import models

def to_do_list(request):
    to_do_items = models.ToDoItem.objects.all()
    
    return render(request, 'main/to_do_list.html', {'all_items': to_do_items})