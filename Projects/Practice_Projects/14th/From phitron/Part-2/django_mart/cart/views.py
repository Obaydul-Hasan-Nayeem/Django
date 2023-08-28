from django.shortcuts import render, redirect
from store.models import Product
# Create your views here.
from .models import Cart, CartItem
def cart(request):
    return render(request, 'cart/cart.html')

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    print('add to cart', product)
    session_id = request.session.session_key
    cart_id = Cart.objects.filter(cart_id = session_id).exists()
    if cart_id:
        cart_item = CartItem.objects.filter(product=product).exists()
        if cart_item:
            item = CartItem.objects.get(product=product)
            item.quantity += 1
            item.save()
        else :
            cartid = Cart.objects.get(cart_id = session_id)
            item = CartItem.objects.create(
                cart = cartid,
                product = product,
                quantity = 1
            )
            item.save()
    else:
        cart = Cart.objects.create(
        cart_id = session_id
        )
        cart.save()
    

    
    
    return redirect('cart')
    