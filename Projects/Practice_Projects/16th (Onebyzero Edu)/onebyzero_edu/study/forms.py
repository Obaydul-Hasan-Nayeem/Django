from django import forms
from .models import University, Department, Course, Question

class UniversityForm(forms.Form):
    university = forms.ModelChoiceField(queryset=University.objects.all(), empty_label="Select a university")

class DepartmentForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Department.objects.all(), empty_label="Select a department")


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['university', 'department', 'year', 'semester', 'course', 'exam_name', 'session', 'question_file']


# class MyForm(forms.Form):
#     name = forms.CharField(label='Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     age = forms.IntegerField(label='Age')
#     comments = forms.CharField(
#         label='Comments',
#         widget=forms.Textarea(attrs={'rows': 4, 'cols': 40})
#     )

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
