from django.shortcuts import render, redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse

## home: function based view
# =============================
# def home(request):
#     return render(request, 'store_book.html')


## home: class based view
# =============================
class MyTemplateView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs): #kwargs: keyword argument nibo
        context = super().get_context_data(**kwargs) # url theke kono kichu hit korle sheta jate context er moddhe chole ashe
        context = {'name' : 'Rahim', 'age' : '23'}
        print(kwargs)
        context.update(kwargs) # dictionary update kora / kwargs k context e convert kora
        print(context)
        return context
    
        # context k dekhate pari
        # template name k render na korei ...
        # template ta override kora jay
        # aladavabe r o dictionary pass korte pari
    


# store_book: function based view 
# ===============================
# def store_book(request):
#     if request.method == 'POST':
#         book = BookStoreForm(request.POST)
#         if book.is_valid():
#             # book.save(commit=False)
#             book.save()
#             print(book.cleaned_data)
#             return redirect('showbook')
#     else:
#         book = BookStoreForm
#     return render(request, 'store_book.html', {'form' : book})


# store_book: class based view 
# =============================
# class BookFormView(FormView):
#     template_name = 'store_book.html'
#     form_class = BookStoreForm
#     # success_url = '/show_books/'
#     # success_url = reverse_lazy('show_books') 
#         # url beshi complex hole reverse_lazy. eta dile o baki shob component k load korar pore ai url ta hit kore. mane kono akta kaj k fast korar process
        
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         form.save()
#         # return HttpResponse('Form Submitted')
#         return redirect('showbook')

# store_book: alternative / more optimized way (class based view) =================================================================
class BookFormView(CreateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('showbook')

# show_book: function based view 
# ================================
# def show_book(request):
#     book = BookStoreModel.objects.all() #bookstoremodel theke data gulo niye ashbe
#     # print(book)
#     for item in book:
#         print(item.first_pub)
#     return render(request, 'show_book.html', {'data': book})

# show_book (List): class based view 
# =============================
class BookListView(ListView):
    model = BookStoreModel
    template_name = 'show_book.html' # jetar moddhe data gulo show korbo
    context_object_name = 'data' # ai 'data' er moddhei BookStoreModel er data gulo chole ashbe. objects.all() / return render er r kichu korte hobe na.

    ## filtering---------------
    # def get_queryset(self):
    #     return BookStoreModel.objects.filter(author='Tanvir')
    
    ## context-------------------
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) # keyword arguments theke asha data gulo context e show koranor jonno
    #     context = {'Tanvir' : BookStoreModel.objects.filter(author='Tanvir')}
    #     return context
    
     ## ordering-------------------
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) # keyword arguments theke asha data gulo context e show koranor jonno
    #     context = {'Tanvir' : BookStoreModel.objects.all().order_by('author')}
    #     return context
    
    ## ordering-------------------
    ordering= ['id']
    ordering= ['-id'] # reverse order
    
    
    ## Home Work --------------------  # TODO
    ## particular bivinno user er jonno template ta k different kore felte hobe
    # def get_template_names(self): # template k override korbe
    #     if self.request.user.is_superuser:
    #         template_name = 'superuser.html'
    #     elif self.request.user.is_staff:
    #         template_name = '' # TODO
    #     else:
    #         template_name = self.template_name
    #     return [template_name]
     
        
# show_book (Detail): class based view 
# ====================================
class BookDetailsView(DetailView):
    model = BookStoreModel
    template_name = 'book_details.html'
    context_object_name = 'item' # jekhane egulo pass hobe / jeta diye access korbo
    pk_url_kwarg = 'id' # primary key accept korar jonno je keyword accept kortechi


# edit_book: function based view 
# ===============================
# def edit_book(request, id):
#     book = BookStoreModel.objects.get(pk = id)
#     form = BookStoreForm(instance = book)
    
#     if request.method == 'POST':
#         form = BookStoreForm(request.POST, instance=book) # instance: edit korte gele jate ager data gulo show kore.
#         if form.is_valid():
#             form.save()
#             return redirect('showbook')
#     return render(request, 'store_book.html', {'form': form})

# edit_book: class based view 
# ===============================
class BookUpdateView(UpdateView):
    model = BookStoreModel
    template_name = 'store_book.html'
    form_class = BookStoreForm
    success_url = reverse_lazy('showbook')

# delete_book: function based view 
# ===============================
# def delete_book(request, id):
#     book = BookStoreModel.objects.get(pk = id).delete()
#     return redirect('showbook')

# delete_book: class based view 
# ===============================
class DeleteBookView(DeleteView):
    model = BookStoreModel
    template_name = 'delete_confirmation.html'
    success_url = reverse_lazy('showbook')