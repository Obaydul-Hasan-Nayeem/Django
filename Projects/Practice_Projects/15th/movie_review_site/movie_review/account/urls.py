from django.urls import path
from account.views import signup_view, login_view, logout_account

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_account, name='logout'),
]