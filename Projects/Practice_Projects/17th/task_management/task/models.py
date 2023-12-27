from django.db import models
from django.contrib.auth.models import User

    
# class Task(models.Model):
#     PRIORITY_CHOICES = [
#         ('low', 'Low'),
#         ('medium', 'Medium'),
#         ('high', 'High'),
#     ]
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     due_date = models.DateField()
#     priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
#     completion_status = models.BooleanField(default=False)
#     creation_date = models.DateTimeField(auto_now_add=True)
#     last_updated = models.DateTimeField(auto_now=True)
#     # photo = models.ImageField(upload_to='photos/', null=True, blank=True)
#     # images = models.ImageField(upload_to='photos/', null=True, blank=False)
#     # images = models.ManyToManyField(TaskImage, blank=True, related_name='task_images')  # Use a unique related_name
#     uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)

#     def __str__(self):
#         return self.title


# class TaskImage(models.Model):
#     task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_images')
#     image = models.ImageField(upload_to='task_images/')



class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    completion_status = models.BooleanField(default=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_tasks', null=True, blank=True)

    def __str__(self):
        return self.title

class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_images')
    image = models.ImageField(upload_to='task_images/')
