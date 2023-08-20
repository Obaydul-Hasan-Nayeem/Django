from django.shortcuts import render

# Create your views here.
from .models import BookStoreModel
from .serializers import BookStoreSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Method-1: APIView=================================
# class BookListView(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         model = BookStoreModel.objects.all()
#         serializer = BookStoreSerializer(model, many=True) # model er data gulo serializer diye json format e convert korbe. & eta db te autometic save hoye jabe
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = BookStoreSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED) # 201: create kora hoiche
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 401: bad request. kono akta vul hoiche
    

# class BookListUpdateDelete(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return BookStoreModel.objects.get(pk=pk)
#         except BookStoreModel.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = BookStoreSerializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = BookStoreSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# Method-2: Concrete APIView=================================
# from rest_framework import generics

# class BookListCreateAPIView(generics.ListCreateAPIView): # get, post request
#     queryset = BookStoreModel.objects.all()
#     serializer_class = BookStoreSerializer


# class BookRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): # update, delete, single element access
#     queryset = BookStoreModel.objects.all()
#     serializer_class = BookStoreSerializer


# Method-3: Shortcut / Model View Set=================================
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = BookStoreModel.objects.all()
    serializer_class = BookStoreSerializer