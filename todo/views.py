from django.shortcuts import render, redirect
from todo.models import Todo
from todo.forms import TodoForm

from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from todo.serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = (BasicAuthentication, )

def index(request):
    return render(request, 'todo/index.html')

def todo_list(request):
    tasks = Todo.objects.all()
    return render(request, 'todo/tasks.html', {'tasks': tasks})

def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    form = TodoForm()
    return render(request, 'todo/edit.html', {'form':form})

def todo_edit(request, pk):
    task = Todo.objects.get(pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            task.description = request.POST.get('description')
            task.status = request.POST.get('status')
            task.save()
            return redirect('todo_list')
    form = TodoForm(instance=task)
    return render(request, 'todo/edit.html', {'form':form})

def todo_delete(request, pk):
    task = Todo.objects.get(pk=pk)
    task.delete()
    return redirect('todo_list')