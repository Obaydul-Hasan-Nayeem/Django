from django.urls import path
from . import views

urlpatterns = [
    path('university/<int:university_id>/', views.university_detail, name='university_detail'),
    
    # path('my_department/<int:university_id>/<int:department_id>/<int:course_id>/', views.my_department, name='my_department'),
    
    path('my_department/<int:university_id>/<int:department_id>/', views.my_department, name='my_department'),
    
    path('course/<int:course_id>/', views.course, name='course'),
    
    path('add_question/', views.add_question, name='add_question'),
    
    path('view_questions/<int:course_id>/', views.view_questions, name='view_questions'),
    
    path('resources/<int:question_id>/', views.view_resources, name='view_resources'),
    
    path('get_departments/', views.get_departments, name='get_departments'),
    
    # path('select_department/', views.select_department, name='select_department'),
    
    # path('my_form/', views.my_form_view, name='my_form'),
]
