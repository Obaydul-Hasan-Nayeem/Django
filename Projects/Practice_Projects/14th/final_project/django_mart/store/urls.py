from django.urls import path, include
from . import views

urlpatterns = [
    path('product_detail/', views.product_detail, name='product_detail'),

    path('store/', views.store, name='store'),
]
