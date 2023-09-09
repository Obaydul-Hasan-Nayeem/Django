from django.db import models
from django.contrib.auth.models import User
from store.models import Product


# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # akjon user jate multiple payment korte pare
    
    payment_id = models.CharField(max_length=100) # transaction id
    
    payment_method = models.CharField(max_length=100) # bkash / nagad / rocket / others
    
    amount_paid = models.IntegerField() # payment amount
    
    status = models.CharField(max_length=100) # paid / pending / failed
    
    created_at = models.DateTimeField(auto_now_add=True)
    

class Order(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    
    order_number = models.CharField(max_length=20)
    
    first_name = models.CharField(max_length=50) # onno kew o to receive korte pare
    
    last_name = models.CharField(max_length=50)
    
    phone = models.CharField(max_length=15)
    
    email = models.EmailField(max_length=50)
    
    address_line1 = models.CharField(max_length=100)
    
    address_line2 = models.CharField(max_length=100)
    
    country = models.CharField(max_length=100)
    
    state = models.CharField(max_length=100)
    
    city = models.CharField(max_length=100)
    
    order_note = models.CharField(max_length=100)
    
    order_total = models.FloatField()
    
    tax = models.FloatField()
    
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    
    ip = models.CharField(max_length=100, blank=True, null = True)
    
    is_ordered = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    quantity = models.IntegerField()
    
    ordered = models.BooleanField(default=False)
    
    created = models.DateTimeField(auto_now_add=True)
    
class PaymentGateWaySettings(models.Model):
    store_id = models.CharField(max_length=500, blank=True, null=True)
    store_pass = models.CharField(max_length=500, blank=True, null=True)