from django import forms 
from book.models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    class Meta: 
        model = BookStoreModel
        # exclude = ['first_pub', 'last_pub']
        fields = ['id', 'book_name', 'author', 'category']