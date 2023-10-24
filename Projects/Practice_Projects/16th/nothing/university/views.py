from django.shortcuts import render, redirect
from .models import University
from .forms import UniversityForm

def add_university(request):
    if request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('university_list')
    else:
        form = UniversityForm()

    return render(request, 'add_university.html', {'form': form})

def university_list(request):
    universities = University.objects.all()
    return render(request, 'university_list.html', {'universities': universities})
