from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views.decorators.http import require_POST


def main(request):
    # Enable adding tasks to task list.
    the_tasks = Task.objects.order_by('id')
    form = TaskForm()
    context = {'the_tasks': the_tasks, 'form': form}
    return render(request, 'index.html', context)


@require_POST
def addTask(request):

    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = Task(text=request.POST['task_input'])
        new_task.save()

    return redirect('main')


def finishedTask(request, task_id):

    task = Task.objects.get(primary_key=task_id)
    task.complete = True
    task.save()

    return redirect('main')


def deleteFinished(request):

    Task.objects.filter(complete__exact=True).delete()

    return redirect('main')


def clear(request):

    Task.objects.all().delete()

    return redirect('main')


