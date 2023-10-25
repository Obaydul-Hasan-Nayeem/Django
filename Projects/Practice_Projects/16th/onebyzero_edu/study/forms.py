from django import forms
from .models import University, Department, Course, Question

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
        
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['university', 'department', 'year', 'semester', 'course', 'exam_name', 'session', 'question_file']


class MyDepartmentForm(forms.Form):
    university = forms.ModelChoiceField(
        queryset=University.objects.all(),
        empty_label="Select a university",
        widget=forms.Select(attrs={'id': 'id_university'})
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        empty_label="Select a department",
        widget=forms.Select(attrs={'id': 'id_department'})
    )
