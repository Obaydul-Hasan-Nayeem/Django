from django.shortcuts import render
from first_app.forms import StudentForm
from first_app.models import Student, Teacher

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # form.save(commit=False)
            form.save()
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})

def showData(request):
    # students list for one student
    teacher = Teacher.objects.get(name = 'Tareq')
    students = teacher.student.all()
    
    for std in students:
        print(std.name, std.roll, std.class_name)
    
    # teachers list for one student
    student = Student.objects.get(name = 'Arup')
    # teachers = student.teacher_set.all() # many to many relationship howar karone "_set" use korte hoy.
    teachers = student.teachers.all() # jehetu model er moddhe related_name use korchi< tai r "_set" lagbe na
    
    for tcr in teachers:
        print(f"{tcr.name} {tcr.subject} {tcr.mobile}")
    
    return render(request, 'show_data.html')
