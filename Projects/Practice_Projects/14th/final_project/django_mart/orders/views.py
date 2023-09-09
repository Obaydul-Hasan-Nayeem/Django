from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from .forms import OrderForm
from . ssl import sslcommerz_payment_gateway
from . models import Payment, Order, OrderProduct
from store.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


# Create your views here.

@method_decorator(csrf_exempt, name='dispatch') # csrf k disable kore deya
def success_view(request):
    data = request.POST
    print('data---------------',data)
    
    user_id = int(data['value_b'])
    user = User.object.get(pk=user_id)
    
    payment = Payment(
        user = request.user,
        payment_id = data['tran_id'],
        payment_method = data['card_issuer'],
        amount_paid = data['store_amount'][0],
        status = data['status'],
    )
    
    payment.save()
    
    # working with order model
    order = Order.objects.get(user=request.user, is_ordered = False, order_number = data['value_a'])
    
    order.payment = payment
    order.is_ordered = True
    order.save()
    
    cart_items = Cart.objects.filter(user = request.user)
    
    for item in cart_items:
        orderproduct = OrderProduct()
        orderproduct.order = order
        orderproduct.payment = payment
        orderproduct.user = request.user
        orderproduct.product = item
        orderproduct.quantity = item.quantity
        orderproduct.ordered = True
        orderproduct.save()
        
        # Reduce the quantity of the sold products
        product = Product.objects.get(id = item.product.id)
        product.stock -= item.quantity #jehetu order complete, tai stock theke quantity komano hoyeche
        product.save()
    
    CartItem.objects.filter(user=user).delete()
    return redirect('cart')



def order_complete(request):
    return render(request, 'orders/order_complete.html')

def place_order(request):
    print(request.POST)
    cart_items = None
    tax = 0
    total = 0
    grand_total = 0
    
    cart_items = CartItem.objects.filter(user=request.user)
    
    if cart_items.count() < 1:
        return redirect('store')
    
    for item in cart_items:
        total += item.product.price * item.quantity
    print(cart_items)
    tax = (2 * total)/100
    grand_total = total + tax
    
    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.order_total = grand_total
            form.instance.tax = tax
            form.instance.ip = request.META.get('REMOTE_ADDR')
            form.instance.payment_id = 2
            saved_instance = form.save() # ai form er shobkichu database e save hoye jabe
            form.instance.order_number = saved_instance.id
            form.save()
            print('form print:',form)
            return redirect(sslcommerz_payment_gateway(request, saved_instance.id, str(request.user.id), grand_total))
    
    return render (request, 'orders/place_order.html', {'cart_items': cart_items, 'tax': tax, 'total' : total, 'grand_total': grand_total})
