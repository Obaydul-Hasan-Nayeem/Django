from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Alhamdulillah! This is my first django page.</h1>")

def about(request):
    return HttpResponse("This is about django page.")