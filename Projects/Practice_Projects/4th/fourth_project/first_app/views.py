from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, './first_app/home.html', {
        "name": "I am Nayeem",
        "marks": 86,
        "courses": [
            {
                "id": 1,
                "course": "A",
                "teacher": "Tanvir"
            },
            {
                "id": 2,
                "course": "B",
                "teacher": "Anis"
            },
            {
                "id": 3,
                "course": "C",
                "teacher": "Shuvo"
            }
        ]
    })
    
def about(request):
    return render(request, './first_app/about.html', {'author': 'glenn maxwell'})
