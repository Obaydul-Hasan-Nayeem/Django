from django.urls import path
from . import views

urlpatterns = [
    # SIGNUP ========================
    path('signup/', views.signup, name='signup'),
    path('api/v1/signup/', views.SignupAPIView.as_view(), name='signup_api'),
    
    # LOGIN ========================
    path('login/', views.user_login, name='login'),
    path('api/v1/login/', views.LoginAPIView.as_view(), name='login_api'),
    
    # LOGOUT ========================
    path('logout/', views.user_logout, name='logout'),
    path('api/v1/logout/', views.LogoutAPIView.as_view(), name='logout_api'),
    
    # PROFILE ========================
    path('profile/', views.profile, name='profile'),
    path('api/v1/profile/', views.ProfileAPIView.as_view(), name='profile_api'),
    
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    # CHANGE PASSWORD ========================
    path('change_password/', views.change_password, name='change_password'),
    path('api/v1/change_password/', views.ChangePasswordAPIView.as_view(), name='change_password_api'),
]
