from django.shortcuts import render
from .models import Movie

# Create your views here.
def home(request):
    searchItem = request.GET.get('searchItem')
    movie = Movie.objects.all()
    return render(request, 'home.html', {'searchItem': searchItem, 'movie': movie})