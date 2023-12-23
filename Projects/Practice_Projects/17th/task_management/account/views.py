from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import UserEditForm
from rest_framework.generics import CreateAPIView
from .forms import SignupForm
from .serializers import SignupSerializer, ChangePasswordSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .serializers import ProfileSerializer

# SIGNUP =============================
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            # UserProfile.objects.create(user=user)
            return redirect('task_list')  # Redirect to the user's profile page
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

class SignupAPIView(CreateAPIView):
    serializer_class = SignupSerializer

    def create(self, request, *args, **kwargs):
        form = SignupForm(request.data)
        if form.is_valid():
            print(form)
            user = form.save()
            login(request, user)
            return Response({'detail': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response({'error': form.errors}, status=status.HTTP_400_BAD_REQUEST)


# LOGIN =============================
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('task_list')  # Redirect to the user's profile page
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

class LoginAPIView(CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # Perform additional actions if needed
        # For example, you may want to create or update a token for the user
        login(request, user)
        # token, created = Token.objects.get_or_create(user=user)

        return Response({'detail': 'User logged in successfully'}, status=status.HTTP_200_OK)
    
# LOGOUT =============================
def user_logout(request):
    logout(request)
    return redirect('login')

class LogoutAPIView(APIView):
    authentication_classes = [SessionAuthentication]  # Enforce session-based authentication

    def post(self, request):
        logout(request)
        return Response({'message': 'User logged out successfully'}, status=200)

    # Optional: Handle GET requests with redirection
    def get(self, request):
        return redirect('login')  # Redirect to login view


# PROFILE =============================
@login_required
def profile(request):
    try:
        profile = request.user.profile  # Retrieve the user's profile
    except Profile.DoesNotExist:
        # If the profile does not exist, create a new one
        profile = Profile(user=request.user)
        profile.save()

    return render(request, 'profile.html', {'profile': profile})

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication for this view

    def get(self, request):
        profile = get_object_or_404(Profile, user=request.user)  # Retrieve the user's profile
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)  # Return serialized profile data as JSON

# CHANGE PASSWORD =========================
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to update the session with the new password
            # messages.success(request, 'Your password has been successfully changed.')
            return render(request, 'profile.html', {'form': form})
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

class ChangePasswordAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        # print('dddddddddddddddddd')
        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password1 = serializer.validated_data['new_password1']
            new_password2 = serializer.validated_data['new_password2']

            form = PasswordChangeForm(user=request.user, data={
                'old_password': old_password,
                'new_password1': new_password1,
                'new_password2': new_password2,
            })

            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important to update the session with the new password
                return Response({'detail': 'Password changed successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': form.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        
# EDIT PROFILE =============================
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # Redirect to profile page or any other desired page after successful update
            return redirect('profile')
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})