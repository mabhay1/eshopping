from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class UserProfile(User):
    
    phone_number=PhoneNumberField()
    

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('a1:profile',kwargs={'pk':self.pk})     

    






class Category(models.Model):
    name=models.CharField(max_length=255,unique=True)
    

    def __str__(self):
        return self.name     


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    name=models.CharField(max_length=255,unique=True)
    price=models.PositiveIntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='product_images',blank=True)

    
    
    def __str__(self):
        return self.name
CHOICES= (
    ('good', 'good'),
    ('average', 'average'),
    ('bad', 'bad'),
)
class Review(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="reviews") 
    rev=models.CharField(choices=CHOICES,max_length=8)   
    experience=models.TextField()
    def get_absolute_url(self):
        return reverse('a1:prod_detail',kwargs={'pk':self.product.pk})     

class Cart(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)  
    total_price=models.PositiveIntegerField()

    def __str__(self):
        return self.user.username     

       

class CartVariable(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    a=models.CharField(max_length=255,default='') 
    total_qty=models.PositiveIntegerField(default=0)
    total_price=models.PositiveIntegerField(default=0)
    up=models.CharField(max_length=255,default='')
    d=models.CharField(max_length=255,default='')
    qnty=models.PositiveIntegerField(default=0)
    
    


    def __str__(self):
        return self.user.username     

class Checkout(models.Model):
    user=models.OneToOneField(UserProfile,on_delete=models.CASCADE,related_name="checkouts")
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    state=models.CharField(max_length=50)
    zipcode=models.CharField(max_length=50)
    name_on_card=models.CharField(max_length=255)
    credit_card_no=models.CharField(max_length=100)
    ex_month=models.CharField(max_length=10)
    ex_year=models.CharField(max_length=4)
    cvv=models.CharField(max_length=5)
        
    def __str__(self):
        return f'{self.user.username}'  
    def get_absolute_url(self):
        return reverse('a1:placeorder')       

class Order(models.Model):

    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now=True)
    quantity=models.PositiveIntegerField()
    total_price=models.PositiveIntegerField()
    

    def __str__(self):
        return f'{self.user.username} {self.id}'

    class Meta:
        ordering=['-order_date']

class OrderUpdates(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='orders')  
    updates=models.CharField(max_length=255)
    update_description=models.TextField()
    updates_date=models.DateTimeField(auto_now=True)
    delivered=models.BooleanField(default=False)  
    
    
    def __str__(self):
        return f' {self.order.user.username} {self.updates}'

    class Meta:
        ordering=['-updates_date'] 

        get_latest_by = 'updates_date'   

class CancelOrder(models.Model):
    order=models.OneToOneField(Order,on_delete=models.CASCADE)
    reason=models.TextField()
    cancel_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f' {self.order.user.username} {self.order_id}'

    def get_absolute_url(self):
        return reverse('a1:yourorder')       
    
    class Meta:
        ordering=['-cancel_date']

class ReturnOrder(models.Model):
    order=models.OneToOneField(Order,on_delete=models.CASCADE,related_name="returns")
    reason=models.TextField()
    return_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f' {self.order.user.username} {self.order_id}'

    def get_absolute_url(self):
        return reverse('a1:yourorder')       
    
    class Meta:
        ordering=['-return_date']       
     