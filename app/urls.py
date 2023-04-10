from django.urls import path

from main.views import *

urlpatterns = [
    path('', to_do_list, name='home')
]
