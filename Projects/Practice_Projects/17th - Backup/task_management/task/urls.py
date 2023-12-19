from django.urls import path
from . import views

urlpatterns = [
    # # Example URL for registration
    # path('home/', views.home, name='home'),
    
    path('home/', views.HomeView.as_view(), name='home'),
       
    path('test/<int:task_id>/', views.MyTemplateView.as_view(template_name='test.html'), name='test'),
    
    path('test/', views.MyListView.as_view()),
     
    path('home/', views.HomeView.as_view(template_name='home.html'), name='home'),
    
    path('test2/', views.MyDetailView.as_view(), name='home'),
    
    # path('add_task/', views.add_task, name='add_task'),
    
    path('add_task/', views.MyFormView.as_view(), name='add_task'),
    
    # path('<int:task_id>/edit/', views.edit_task, name='edit_task'),
    
    path('<int:pk>/edit/', views.MyUpdateView.as_view(), name='edit_task'),
    
    # path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
    
    path('<int:pk>/delete/', views.MyDeleteView.as_view(), name='delete_task'),
    
    
    path('<int:task_id>/complete/', views.complete_task, name='complete_task'),
    
    path('task_list/', views.task_list, name='task_list'),
    
    path('task_detail/<int:task_id>/', views.task_detail, name='task_detail'),
]
