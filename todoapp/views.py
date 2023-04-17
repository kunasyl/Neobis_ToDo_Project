from django.shortcuts import render, redirect

from . import models, forms, services

todo_services = services.ToDoServices()


def to_do_list(request, sort_by='-created_at'):
    to_do_items = models.ToDoItem.objects.order_by(sort_by)
    context = {'todo_list': to_do_items, 'title': 'Главная страница'}

    return render(request, 'todoapp/to_do_list.html', context)


def add_todo(request):
    if request.method == 'POST':
        form = forms.NewToDoForm(request.POST)
        if form.is_valid() and todo_services.validate_deadline(form.cleaned_data['deadline']):
            form = form.save(commit=False)
            form.is_complete = False
            form.save()
            return redirect('home')

    form = forms.NewToDoForm()
    return render(
        request=request,
        template_name="todoapp/add_to_do.html",
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
