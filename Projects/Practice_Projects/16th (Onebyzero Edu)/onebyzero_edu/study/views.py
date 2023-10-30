from django.shortcuts import render, redirect
from .models import University, Department, Course, Question
from django.shortcuts import get_object_or_404
from .forms import QuestionForm, MyDepartmentForm
from django.contrib.auth.models import User
from collections import Counter
from django.db.models import Count

# Assuming you want to find the user by username
# username = 'nayeem'
# try:
#     user = User.objects.get(username=username)
#     user_id = user.id
#     print(f"User ID for {username} is {user_id}")
# except User.DoesNotExist:
#     print(f"User with username {username} does not exist.")


def university_detail(request, university_id):
    university = University.objects.get(pk=university_id)
    departments = Department.objects.filter(university=university)
    return render(request, 'university_detail.html', {'university': university, 'departments': departments})


# def my_form_view(request):
#     if request.method == 'POST':
#         form = MyForm(request.POST)
#         if form.is_valid():
#             university_id = form.cleaned_data['university'].id
#             department_id = form.cleaned_data['department'].id
#             return redirect('my_department', university_id=university_id, department_id=department_id)
#     else:
#         form = MyForm()

#     return render(request, 'my_form.html', {'form': form})
    

# def my_department(request, university_id, department_id, course_id):
#     university = get_object_or_404(University, pk=university_id)
#     department = get_object_or_404(Department, pk=department_id, university=university)
#     course = get_object_or_404(Course, pk=course_id)
#     # course = Course.objects.filter(department=department)
#     semester = course.semester
#     year = course.year
#     credit = course.credit
#     code = course.code

#     # context = {
#     #     'department': department,
#     #     'university': university,
#     #     'semester': semester,
#     #     'course': course,
#     #     'year': year,
#     #     'credit': credit,
#     # }
    
#     return render(request, 'my_department.html', {'department': department, 'university': university, 'semester': semester, 'course': course, 'year': year, 'credit': credit, 'code': code})

def my_department(request, university_id, department_id):
    university = get_object_or_404(University, pk=university_id)
    department = get_object_or_404(Department, pk=department_id, university=university)
    
    # courses = department.course_set.filter(year=1, semester=2)
    courses = department.course_set.all()

    return render(request, 'my_department.html', {'department': department, 'university': university, 'courses': courses})

from django.http import JsonResponse
def get_departments(request):
    university_id = 1
    # Query the database to get the departments for the selected university.
    departments = Department.objects.filter(university_id=university_id)
    department_list = [{'id': department.id, 'name': department.name} for department in departments]
    # return JsonResponse({'departments': department_list})
    return render(request, 'home.html', {'department_list':department_list})

def add_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False) # Create the question object but don't save it yet
            question.uploaded_by = request.user  # Set the uploaded_by field to the currently logged-in user
            question.save()  # Save the question with the uploaded_by information
            return redirect('view_questions', course_id=question.course.id)
    else:
        form = QuestionForm()
    return render(request, 'add_question.html', {'form': form})

# def view_questions(request, course_id):
#     questions = Question.objects.filter(course=course_id).order_by('-upload_time')
#     course = get_object_or_404(Course, pk=course_id)
    
#     return render(request, 'view_questions.html', {'questions': questions, 'course': course})

def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    course_id = question.course.id
    return redirect('view_questions', course_id=course_id)

def view_questions(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    questions = Question.objects.filter(course=course).order_by('-upload_time')
    
    session_filter = request.GET.get('session')
    exam_name_filter = request.GET.get('exam_name')

    if session_filter:
        questions = questions.filter(session=session_filter)

    if exam_name_filter:
        questions = questions.filter(exam_name__icontains=exam_name_filter)
        
    all_uploaders = Question.objects.filter(course=course_id).values_list('uploaded_by__username', flat=True).distinct()
    
    users_with_question_count = (
        Question.objects
        .filter(course=course)
        .values('uploaded_by__username')
        .annotate(question_count=Count('uploaded_by__username'))
    )

    context = {
        'questions': questions,
        'course': course,
        'all_uploaders': all_uploaders,
        # 'question_count': question_count
        'users_with_question_count': users_with_question_count
    }

    return render(request, 'view_questions.html', context)

def view_resources(request, question_id):
    question = Question.objects.all()
    
    return render(request, 'resources.html', {'question': question})


def course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    university = course.university
    department = course.department
    question_count = Question.objects.filter(course=course).count()
    return render(request, 'view_course.html', {'course': course, 'university': university, 'department': department, 'question_count': question_count})


# def select_department(request):
#     if request.method == 'GET':
#         form = MyDepartmentForm(request.GET)
#         if form.is_valid():
#             university_id = form.cleaned_data['university'].id
#             department_id = form.cleaned_data['department'].id
#             return redirect('my_department', university_id=university_id, department_id=department_id)
#     else:
#         form = MyDepartmentForm()

#     return render(request, 'select_department.html', {'form': form})



