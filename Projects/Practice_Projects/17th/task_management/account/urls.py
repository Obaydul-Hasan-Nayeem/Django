from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('signup/', views.signup, name='signup'),
    
    path('login/', views.user_login, name='login'),
    
    path('logout/', views.user_logout, name='logout'),
    
    path('profile/', views.profile, name='profile'),
    
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    path('change_password/', views.change_password, name='change_password'),
]
