from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST


@login_required
def main(request):
    # Enable adding tasks to task list.
    the_tasks = Task.objects.filter(user=request.user.id).order_by('id')
    form = TaskForm()
    context = {'the_tasks': the_tasks, 'form': form}

    return render(request, 'index.html', context)

@require_POST
def addTask(request):
    
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()

    return redirect('main')


def finishedTask(request, task_id):

    task = Task.objects.get(pk=task_id)
    task.finished = True
    task.save()

    return redirect('main')


def deleteFinished(request):

    Task.objects.filter(finished__exact=True).delete()

    return redirect('main')


def clear(request):

    Task.objects.all().delete()

    return redirect('main')


