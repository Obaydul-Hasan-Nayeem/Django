from django.shortcuts import render, get_object_or_404
from . models import Product
from category.models import Category
from django.core.paginator import Paginator

# Create your views here.

def store(request, category_slug=None): # category_slug: user jodi filter na kore tahole jeno shobgulo category er product dekhay
    
    # category = None
    # products = None
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(is_available=True, category=category) # category wise products
        paginator = Paginator(products, 1) #(total objects/ products, per page e kotogulo object dekhte chai)
        page = request.GET.get('page')
        page_product = paginator.get_page(page)
        
    else:
        products = Product.objects.filter(is_available=True) # all products
        paginator = Paginator(products, 2)
        page = request.GET.get('page')
        page_product = paginator.get_page(page)
        # print(page_product)
        # for i in page_product:
        #     print(i)
        
    # print(products)
    # for item in products:
    #     print(item.product_name, item.price, item.category, item.stock, item.is_available)
    
    # print(page_product.has_previous(), page_product.has_next(), page_product.previous_page_number(), page_product.next_page_number())
    
    categories = Category.objects.all()
    
    # print(page_product.num_pages)
    
    # print(categories)
    
    context = {'products': page_product, 'categories': categories}
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    single_product = Product.objects.get(slug = product_slug, category__slug = category_slug)
    # category jehetu alada model, tai double underscore
    # jehetu single product niye ashte hobe, tai 'get'. noyto 'filter' ditam
    
    return render(request, 'store/product_detail.html', {'product': single_product})