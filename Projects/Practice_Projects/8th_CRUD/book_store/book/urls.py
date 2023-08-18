from django.urls import path
from . import views 

urlpatterns = [
    #-----------------------------------------------------------
    # path('', home),
    #-----------------------------------------------------------
    # path('', views.TemplateView.as_view(template_name = 'home.html')),
    #-----------------------------------------------------------
    path('<int:roll>/', views.MyTemplateView.as_view(), {'author': 'Rahim'}, name='homepage'), # .as_view er moddhe argument dile, orthat template_name = 'home.html' likhle views.py er class er tar cheye etar priority agee pabe. mane override korbe
    #-----------------------------------------------------------
    # path('store_new_book/', views.store_book, name="storebook"),
    #-----------------------------------------------------------
    
    path('store_new_book/', views.BookFormView.as_view(), name="storebook"), # as_view: render korar jonno
    #-----------------------------------------------------------
    
    # path('show_books/', views.show_book, name="showbook"),
    #-----------------------------------------------------------
    
    path('show_books/', views.BookListView.as_view(), name="showbook"),
    #----------------------------------------------------------
    
    path('book_details/<int:id>', views.BookDetailsView.as_view(), name="book_details"),
    #-----------------------------------------------------------
    
    # path('edit_book/<int:id>', views.edit_book, name="editbook"),
    #-------------------------------------------------------------
    
    path('edit_book/<int:pk>', views.BookUpdateView.as_view(), name="editbook"),
    #-------------------------------------------------------------
    
    # path('delete_book/<int:id>', views.delete_book, name="deletebook"),
    #-------------------------------------------------------------
    
    path('delete_book/<int:pk>', views.DeleteBookView.as_view(), name="deletebook"),
    #-------------------------------------------------------------
]