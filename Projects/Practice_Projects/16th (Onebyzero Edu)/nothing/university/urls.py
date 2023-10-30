from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_university, name='add_university'),
    path('list/', views.university_list, name='university_list'),
]
