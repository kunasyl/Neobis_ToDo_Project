from django.shortcuts import render, redirect

from . import models, forms

def to_do_list(request):
    to_do_items = models.ToDoItem.objects.all()
    context = {'all_items': to_do_items}

    return render(request, 'main/to_do_list.html', context)


def add_todo(request):
    if request.method == 'POST':
        form = forms.NewToDoForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.is_complete = False
            form.save()
            return redirect('home')
 
    form = forms.NewToDoForm()
    return render(
        request=request,
        template_name="main/add_to_do.html",
        context={"form": form}
    )


def update_todo(request, todo_id):
    todo = models.ToDoItem.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()

    return redirect('home')


def delete_todo(request, todo_id):
    todo = models.ToDoItem.objects.get(id=todo_id)
    todo.delete()

    return redirect('home')