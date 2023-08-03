from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = "homepage"),
    path('index/', views.home, name = "indexpage"),
]