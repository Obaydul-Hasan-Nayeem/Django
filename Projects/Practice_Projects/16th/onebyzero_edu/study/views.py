from django.shortcuts import render
from .models import University, Department, Course

def university_detail(request, university_id):
    university = University.objects.get(pk=university_id)
    departments = Department.objects.filter(university=university)
    return render(request, 'university_detail.html', {'university': university, 'departments': departments})

def my_department(request, depertment_id):
    department = Department.objects.get(pk=depertment_id)
    university = Department.objects.get(pk=depertment_id).university
    courses = Course.objects.filter(department=department)
    semester = Course.objects.get(pk=depertment_id).semester
    
    return render(request, 'my_department.html', {'department': department, 'university': university, 'courses': courses, 'semester': semester})


# Similar views for departments and courses
