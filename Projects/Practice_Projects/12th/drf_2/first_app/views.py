from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from . import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from . import paginations

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AdminOrReadOnly] 
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    # permission_classes = [IsAuthenticated]
    
    # filter_backends = [filters.SearchFilter] # for searching
    # search_fields = ['name', 'description']
    
    filter_backends = [filters.OrderingFilter] # for ordering
    search_fields = ['price']
    
    pagination_class = paginations.ProductPagination
    

class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.ReviewerOrReadOnly]
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer
    
    # filter_backends = [DjangoFilterBackend] # for filtering
    # # filterset_fields = ['user__username']
    # filterset_fields = ['rating', 'product']
    
    filter_backends = [filters.OrderingFilter] # for ordering
    search_fields = ['rating']
    
    # permission_classs = [IsAuthenticated] # from: https://www.django-rest-framework.org/api-guide/permissions/#setting-the-permission-policy
    
    # def get_queryset(self):
    #     queryset = models.ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains=username) # icontains: case sensitive hobe na. choto hat / boro hat jetai dek kono somossa hobe na.
    #     return queryset
    
    