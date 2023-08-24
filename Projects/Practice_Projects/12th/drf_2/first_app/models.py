from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
   
    description = models.TextField() # multiple line likhte parbe
   
    price = models.DecimalField(max_digits=10, decimal_places=2) # 120.34
    
    def __str__(self): # object create hole shetar nam jeno ai product er nam diyei hoy. 
        return self.name
    
class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews") # reviews: kon product er jonno kon review sheta eta diye find out kora jabe
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)]) # choice(i, j) --> i database e save korar jonno, j user k dekhanor jonno
   
    review = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True) # obj kokhon toiri hobe shetar time save korbe
    
    updated_at = models.DateTimeField(auto_now=True) # user jokhon review edit korbe tokhon er time dekhabe.
    
    class Meta: # class er akta notun behaviour add kore
        unique_together = ('product', 'user') # akjon user akta product er under e aktai review dite parbe
        
    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.rating}"