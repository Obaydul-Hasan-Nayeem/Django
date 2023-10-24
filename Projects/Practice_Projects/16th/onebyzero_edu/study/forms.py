from django import forms
from .models import University, Department, Course

class UniversityForm(forms.ModelForm):
    class Meta:
        model = University
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
