from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to the user's profile page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def user_profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    return render(request, 'profile.html', {'user': user, 'profile': profile})
