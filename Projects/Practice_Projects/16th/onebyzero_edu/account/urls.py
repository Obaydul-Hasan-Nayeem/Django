from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
]
