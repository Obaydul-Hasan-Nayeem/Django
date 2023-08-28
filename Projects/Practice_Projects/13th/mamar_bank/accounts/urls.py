from django.urls import path
from . views import UserRegistrationView, UserLoginView, UserLogoutView, UserBankAccountUpdateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    # class based view hole as_view dite hoy
    
    path('login/', UserLoginView.as_view(), name='login'),
    
    path('logout/', UserLogoutView.as_view(),name='logout'),
    
    path('profile/', UserBankAccountUpdateView.as_view(),name='profile'),
]
