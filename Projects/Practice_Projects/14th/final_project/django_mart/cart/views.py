from django.shortcuts import render, redirect
from store.models import Product
from . models import Cart, CartItem

# Create your views here.
# user logged out hole session id er upor base kore kaj korbo.
# user logged in hole user er upore base kore kaj korbo.     

def cart(request):
    session_id = request.session.session_key # session id k niye ashlam
    cartid = Cart.objects.get(cart_id = session_id) # model ber kore anlam
    cart_id = Cart.objects.filter(cart_id = session_id).exists() # ai session id wala kono cart database e ache kina. thakle -> True, na thakle -> False dibe

    cart_items = None
    tax = 0
    total = 0
    grand_total = 0
    
    if cart_id:
        cart_items = CartItem.objects.filter(cart = cartid)
        for item in cart_items:
            total += (item.product.price * item.quantity)
            
        tax = (2 * total) / 100 # 2% vat
        grand_total = total + tax

    
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'tax': tax, 'total': total, 'grand_total': grand_total})

def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def add_to_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    # print(product)
    session_id = get_create_session(request) # session id niye ashlam
    # print("cart id:", cart_id)
    print(session_id)
    
    cart_id = Cart.objects.filter(cart_id = session_id).exists() # ai session id wala kono cart database e ache kina. thakle -> True, na thakle -> False dibe
    
    if cart_id:
        # print("cart ache")
        cart_item = CartItem.objects.filter(product = product).exists()
        if cart_item:
            # print('ache')
            item = CartItem.objects.get(product = product)
            item.quantity += 1
            item.save()
        else:
            cart_id = Cart.objects.get(cart_id = session_id)
            item = CartItem.objects.create(
                cart = cart_id,
                product = product,
                quantity = 1
            )
            item.save()
    else:
        cart = Cart.objects.create(
            cart_id = session_id
            )
        cart.save()
    
    # cart_item = CartItem.objects.create(
    #     product = product,
    #     cart = cart,
    #     quantity = 1
    # )
    
    return redirect('cart')

def remove_cart_item(request, product_id):
    # print(product_id)
    product = Product.objects.get(id = product_id)
    session_id = request.session.session_key
    cartid = Cart.objects.get(cart_id = session_id) # cart search korlam
    cart_item = CartItem.objects.get(cart = cartid, product = product)
    # print('aaaaa:', cart_item)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')

def remove_cart(request, product_id):
    product = Product.objects.get(id = product_id)
    session_id = request.session.session_key
    cartid = Cart.objects.get(cart_id = session_id)
    cart_item = CartItem.objects.get(cart = cartid, product = product)
    cart_item.delete()
    return redirect('cart')