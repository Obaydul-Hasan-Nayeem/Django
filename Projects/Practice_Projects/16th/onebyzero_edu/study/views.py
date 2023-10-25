from django.shortcuts import render, redirect
from .models import University, Department, Course, Question
from django.shortcuts import get_object_or_404
from .forms import QuestionForm, MyDepartmentForm

def university_detail(request, university_id):
    university = University.objects.get(pk=university_id)
    departments = Department.objects.filter(university=university)
    return render(request, 'university_detail.html', {'university': university, 'departments': departments})


def my_department(request, university_id, department_id, course_id):
    university = get_object_or_404(University, pk=university_id)
    department = get_object_or_404(Department, pk=department_id, university=university)
    course = get_object_or_404(Course, pk=course_id)
    # course = Course.objects.filter(department=department)
    semester = course.semester
    year = course.year
    credit = course.credit
    code = course.code

    # context = {
    #     'department': department,
    #     'university': university,
    #     'semester': semester,
    #     'course': course,
    #     'year': year,
    #     'credit': credit,
    # }
    
    return render(request, 'my_department.html', {'department': department, 'university': university, 'semester': semester, 'course': course, 'year': year, 'credit': credit, 'code': code})

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect or show a success message
            return render(request, 'resources.html')
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})


def view_resources(request, question_id):
    question = Question.objects.all()
    
    return render(request, 'resources.html', {'question': question})


def select_department(request):
    if request.method == 'GET':
        form = MyDepartmentForm(request.GET)
        if form.is_valid():
            university_id = form.cleaned_data['university'].id
            department_id = form.cleaned_data['department'].id
            return redirect('my_department', university_id=university_id, department_id=department_id)
    else:
        form = MyDepartmentForm()

    return render(request, 'select_department.html', {'form': form})

