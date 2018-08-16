from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Todo


# Create your views here.
def index(request):
    todo_list = Todo.objects.all().order_by('-created_date')
    context = {'todos': todo_list}  # gets sent to index.html
    return render(request, 'todo_app/index.html', context)


def add(request):
    if request.method == 'POST':
        text = request.POST['todoInput']
        new_todo = Todo(todo_text=text)
        new_todo.save()
    return HttpResponseRedirect(reverse('todo_app:index'))


def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todo_app:index'))


def markdone(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    todo.completed = not todo.completed
    todo.save()
    return HttpResponseRedirect(reverse('todo_app:index'))
