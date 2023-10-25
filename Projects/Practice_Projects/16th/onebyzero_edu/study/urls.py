from django.urls import path
from . import views

urlpatterns = [
    path('university/<int:university_id>/', views.university_detail, name='university_detail'),
    
    path('my_department/<int:university_id>/<int:department_id>/<int:course_id>/', views.my_department, name='my_department'),
    
    path('add_question/', views.add_question, name='add_question'),
    
    path('resources/<int:question_id>/', views.view_resources, name='view_resources'),
    
    path('select_department/', views.select_department, name='select_department'),
]
