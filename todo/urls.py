from django.urls import path, include
from todo.views import *


urlpatterns = [
    path('', index, name="dashboard"),
    path('tasks', todo_list, name='todo_list'),
    path('task', todo_create, name='todo_create'),
    path('task/<int:pk>', todo_edit, name="todo_edit"),
    path('task/<int:pk>/detele', todo_delete, name="todo_delete")
]

