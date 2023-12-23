from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
# router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    
    # HOME ===============================
    path('home/', views.home, name='home'),
    path('api/v1/home/', views.HomeAPIView.as_view(), name='home_api'),
    
    # ADD TASK ===============================
    path('add_task/', views.add_task, name='add_task'),
    path('api/v1/add_task/', views.AddTaskCreateView.as_view(), name='add_task_api'),
    
    # EDIT TASK ===============================
    path('<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('api/v1/edit_task/<int:pk>/', views.EditTaskAPIView.as_view(), name='edit_task_api'),
    
    # DELETE TASK ===============================
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('api/v1/delete_task/<int:pk>/', views.DeleteTaskAPIView.as_view(), name='delete_task_api'),
    
    # COMPLETE TASK ===============================
    path('<int:task_id>/complete/', views.complete_task, name='complete_task'),
    path('api/v1/complete_task/<int:pk>/', views.CompleteTaskAPIView.as_view(), name='complete_task_api'),
    
    # TASK LIST ===============================
    path('task_list/', views.task_list, name='task_list'),
    path('api/v1/task_list/', views.TaskListView.as_view(), name='task_list_api'),
    
    # TASK DETAIL ===============================
    path('task_detail/<int:task_id>/', views.task_detail, name='task_detail'),
    path('api/v1/task_detail/<int:pk>/', views.TaskDetailAPIView.as_view(), name='task_detail_api'),
]
