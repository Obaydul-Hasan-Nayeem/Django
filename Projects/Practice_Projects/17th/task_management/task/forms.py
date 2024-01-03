from django import forms
from .models import Task, TaskImage

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'completion_status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Description', 'rows': 3}),
            
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'completion_status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
