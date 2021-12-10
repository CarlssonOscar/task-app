from django.shortcuts import render
from .models import Task


def main(request):
    the_tasks = Task.objects.order_by('id')
    context = {'the_tasks' : the_tasks}
    return render(request, 'index.html', context)
