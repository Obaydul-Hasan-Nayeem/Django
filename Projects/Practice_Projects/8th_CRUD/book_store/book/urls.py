from django.urls import path
from book.views import home, store_book, show_book, edit_book, delete_book

urlpatterns = [
    path('', home),
    path('store_new_book/', store_book, name="storebook"),
    path('show_books/', show_book, name="showbook"),
    path('edit_book/<int:id>', edit_book, name="editbook"),
    path('delete_book/<int:id>', delete_book, name="deletebook"),
]
