from django.shortcuts import render, redirect
from . forms import RegistrationForm
from django.contrib.auth import login, logout, authenticate
from cart.models import Cart, CartItem
# Create your views here.

def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("Form is valid and user will be saved.")
            # print(form.cleaned_data.get('first_name'))
            user = form.save()
            login(request, user)
            print("User is logged in.")
            return redirect('login')
            
    return render(request, 'accounts/register.html', {'form': form})

def profile(request):
    return render(request, 'accounts/dashboard.html')

def user_login(request):
    if request.method == 'POST':
        # print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        # akhn o login hoyni
        session_key = get_create_session(request)
        cart = Cart.objects.get(cart_id = session_key)
        is_cart_item_exists = CartItem.objects.filter(cart = cart).exists()
        if is_cart_item_exists:
            cart_item = CartItem.objects.filter(cart = cart)
            for item in cart_item:
                item.user = user
                item.save()
        login(request, user)
        # login hoye geche
        return redirect('profile')
    return render(request, 'accounts/signin.html')

def user_logout(request):
    logout(request)
    return redirect('login')