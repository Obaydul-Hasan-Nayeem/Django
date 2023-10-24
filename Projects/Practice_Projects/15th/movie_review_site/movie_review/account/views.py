from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from account.forms import SignupForm, LogInForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.
def signup_view(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': SignupForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {'form': SignupForm(), 'error': 'Username already exists'})
                
        else:
            return render(request, 'signup.html', {'form': SignupForm(), 'error': 'Passwords must match'})

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': LogInForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'login.html', {'form': LogInForm(), 'error': 'Username or password is incorrect'})
        else:
            login(request, user)
            return redirect('home')
        
def logout_account(request):
    # if request.method == 'POST':
        logout(request)
        return redirect('home')