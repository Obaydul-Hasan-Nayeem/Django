from django.shortcuts import render, redirect
from .models import Movie
from django.shortcuts import get_object_or_404
from .forms import ReviewForm

# Create your views here.
def home(request):
    searchItem = request.GET.get('searchItem')
    if searchItem:
        movie = Movie.objects.filter(name__icontains=searchItem)
    else:
        movie = Movie.objects.all()
    return render(request, 'home.html', {'searchItem': searchItem, 'movie': movie})

def details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request, 'details.html', {'movie': movie, 'reviews': reviews})

def create_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        return render(request, 'create_review.html', {'form': ReviewForm(), 'movie': movie})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = request.movie
            newReview.save()
            return redirect('details', newReview.movie.id)
        except ValueError:
            return render(request, 'create_review.html', {'form': ReviewForm(), 'movie': movie, 'error': 'Bad data passed in. Try again!'})