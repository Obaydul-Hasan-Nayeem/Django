from django.db import models
from django.contrib.auth.models import User

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
    # photo = models.ImageField(upload_to='task/',
    #     validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'jpeg'])])
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    


