# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect

from myapp.models import Todo


def todolist(request):
    todos = Todo.objects.filter(status=1)
    todo_count = len(todos)
    finishtodos = Todo.objects.filter(status=0)
    return render(request, 'index.html', {'todos': todos, 'finishtodos': finishtodos, 'todo_count': todo_count})


def addtodo(request):
    if request.method == 'POST':
        content = request.POST['content']
        Todo(content=content).save()
        return redirect(todolist)


def finishtodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.status = 0
    todo.save()
    return redirect(todolist)


def unfinishtodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.status = 1
    todo.save()
    return redirect(todolist)


def deletetodo(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect(todolist)

