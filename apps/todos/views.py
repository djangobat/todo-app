from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Topic, Task
from .forms import CreateTopicForm
from .filters import TaskFilter


@login_required
def todo(request):
    topics = Topic.objects.filter(owner=request.user)
    query = Task.objects.filter(topic__owner=request.user)
    task_filter = TaskFilter(request.GET, queryset=query)
    print(task_filter.qs)
    context = {
        'topics': topics,
        'tasks': task_filter.qs,
        'form': task_filter.form, 
    }

    return render(request, 'todos/todo.html', context)


@login_required
def create_task(request):
    user = request.user

    return render(request, 'todos/task_create.html')


@login_required
def create_topic(request):
    user = request.user
    if request.method == 'POST':
        form = CreateTopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = user
            new_topic.save()
            return redirect('todo')
    else:
        form = CreateTopicForm()

    context = {
        'form': form,
    }

    return render(request, 'todos/topic_create.html', context)