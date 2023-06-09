from django.urls import path

from todoapp.views import *

urlpatterns = [
    path('', to_do_list, name='home'),
    path('add/', add_todo, name='add'),
    path('update/<int:todo_id>/', update_todo, name='update'),
    path('delete/<int:todo_id>/', delete_todo, name='delete')
]
