from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, TaskImage
from .forms import TaskForm
from datetime import timedelta
from datetime import date
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import TaskSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# HOME ====================
def home(request):
    return render(request, 'home.html')

class HomeAPIView(APIView):
    def get(self, request, format=None):
        return Response({'message': 'Welcome to the Task Home Page'}, status=status.HTTP_200_OK)

# ADD TASK ====================
# @login_required
# def add_task(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST, request.FILES)
#         images = request.FILES.getlist('images')
#         if form.is_valid():
#             task = form.save(commit=False)
#             task.uploaded_by = request.user
#             task.images = images
#             task.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm()
#     return render(request, 'add_task.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import TaskForm

@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.uploaded_by = request.user
            task.save()

            # Handle multiple images
            images = request.FILES.getlist('images')
            for image in images:
                task_image = TaskImage.objects.create(task=task, image=image)

            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


class AddTaskCreateView(CreateAPIView): 
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# EDIT TASK ====================
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    last_updated = task.last_updated
    # images = TaskImage.objects.filter(task=task)
    images = task.task_images.all()
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'last_updated': last_updated, 'images': images})




class EditTaskAPIView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# DELETE TASK ====================
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            task.delete()
            return redirect('task_list')
    return render(request, 'confirm_delete.html', {'task': task})

class DeleteTaskAPIView(RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# COMPLETE TASK ====================
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completion_status = True
    task.save()
    return redirect('task_list')

class CompleteTaskAPIView(RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_update(self, serializer):
        serializer.instance.completion_status = True
        serializer.save()

# TASK LIST ====================
@login_required
def task_list(request):
    query = request.GET.get('q')
    # tasks = Task.objects.order_by('-creation_date')
    tasks = Task.objects.filter(uploaded_by=request.user).order_by('-creation_date')


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

class TaskListView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# TASK DETAIL ====================
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    # Calculate remaining time
    if task.due_date:
        due_date = task.due_date
        creation_date = task.creation_date.date() if task.creation_date else date.today()
        remaining_time = due_date - creation_date
    else:
        remaining_time = None
    
    task_images = task.task_images.all()
    
    return render(request, 'task_detail.html', {'task': task, 'remaining_time': remaining_time, 'task_images': task_images})

class TaskDetailAPIView(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer