from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.
def add_task(request):
    task = request.POST.get('task')
    Task.objects.create(task=task)
    return redirect('home')


def mark_as_done(request, pk):
    print("helo")
    task = Task.objects.get(id=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = Task.objects.get(id=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = Task.objects.get(id=pk)
    if request.method == 'POST':
        new_task = request.POST.get('task')
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else :
       context = {'get_task': get_task}
    return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    get_task = Task.objects.get(id=pk)
    get_task.delete()
    return redirect('home')