from django.urls import path
from . import views

urlpatterns = [
    path('university/<int:university_id>/', views.university_detail, name='university_detail'),
    path('my_department/<int:depertment_id>/', views.my_department, name='my_department'),
    # Define URLs for departments and courses
]
