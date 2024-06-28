from datetime import timezone
from django.shortcuts import redirect, render, get_object_or_404
from .models import Task
from .forms import TaskForm, TaskFilterForm


def task_list(request):
    filter_form = TaskFilterForm(request.GET)
    tasks = Task.objects.all()
    if filter_form.is_valid():
        status = filter_form.cleaned_data['status']
        if status:
            tasks = tasks.filter(status=status)
    return render(request, 'task_list.html', {'tasks': tasks, 'filter_form': filter_form})


def task_detail(request, pk):   
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})


def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            if form.cleaned_data['status'] == 'completed' and task.completed_at is None:
                task.completed_at = timezone.now()
            form.save()
            return redirect('task_list')
        else:
            task = TaskForm(instance=task)
        return render(request, 'task_form.html', {'form': form, 'task': task })    
        

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})
