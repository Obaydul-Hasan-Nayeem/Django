from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import TaskForm
from datetime import timedelta
from datetime import date
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            # question = form.save(commit=False) # Create the question object but don't save it yet
            # question.uploaded_by = request.user  # Set the uploaded_by field to the currently logged-in user
            form.save()  # Save the question with the uploaded_by information
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

from django.shortcuts import render

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            task.delete()
            return redirect('task_list')
    return render(request, 'confirm_delete.html', {'task': task})


def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completion_status = True
    task.save()
    return redirect('task_list')

@login_required
def task_list(request):
    query = request.GET.get('q')
    # tasks = Task.objects.all()
    tasks = Task.objects.order_by('-creation_date')  # Or any other field you want to order by


    if query:
        tasks = tasks.filter(title__icontains=query)

    # Filter by creation date
    created_date = request.GET.get('created_date')
    if created_date:
        tasks = tasks.filter(creation_date=created_date)

    # Filter by due date
    due_date = request.GET.get('due_date')
    if due_date:
        tasks = tasks.filter(due_date=due_date)

    # Filter by priority
    priority = request.GET.get('priority')
    if priority:
        tasks = tasks.filter(priority=priority)

    # Filter by completion status
    completion_status = request.GET.get('completion_status')
    if completion_status in ['True', 'False']:
        tasks = tasks.filter(completion_status=completion_status)
    
    for task in tasks:
        if task.due_date:
            due_date = task.due_date
            creation_date = task.creation_date.date() if task.creation_date else date.today()
            task.remaining_time = due_date - creation_date
        else:
            task.remaining_time = None
    
    return render(request, 'task_list.html', {'tasks': tasks, 'query': query})




def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    # Calculate remaining time
    if task.due_date:
        due_date = task.due_date
        creation_date = task.creation_date.date() if task.creation_date else date.today()
        remaining_time = due_date - creation_date
    else:
        remaining_time = None
        
    return render(request, 'task_detail.html', {'task': task, 'remaining_time': remaining_time})

