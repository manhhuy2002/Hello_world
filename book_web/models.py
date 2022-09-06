from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.urls import  reverse

class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class User(Base):
    username = models.CharField(max_length=200,unique=True,db_index=True)
    password = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.username
    
class KYC(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    name_customer = models.CharField(max_length=200,db_index=True,null=False, blank=False)
    phone_number = models.CharField(max_length=200,null=False, blank=False)
    email = models.CharField(max_length=200,null=True,blank=True)
    date_birth = models.DateField(null=True)
    
class Role(Base):
    role_id = models.AutoField(primary_key=True,null= False)
    role_name = models.CharField(max_length=200,null= False,blank=False)
    description = models.TextField(max_length=100,null=True,blank=True)
    
class Function(Base):
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    name_function = models.CharField(max_length=100,null=True)
class Discount(Base):
    discount_id = models.AutoField(primary_key=True,null= False)
    value = models.FloatField(null=True)
    description = models.TextField(max_length=200,null=True,blank=True)
    expiry = models.DateTimeField(null=True)    
class Book(Base):
    book_id = models.AutoField(primary_key=True,null= False, blank=False)
    name_book = models.CharField(max_length=200,null = False, blank=False)
    
class Category(Base):
    category_id = models.AutoField(primary_key=True,null= False)
    name_category = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    book = models.ManyToManyField(Book,null = True, blank=True)    
class Review(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200,null = True, blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)
class Carts(Base):
    cart_id = models.AutoField(primary_key=True,null= False,blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=True)
class Voucher(Base):
    voucher_id = models.AutoField(primary_key=True,null= False)
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    expiry_date = models.DateTimeField(null=True)
class Detail_cart(Base):
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    voucher_id = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    quantity_buy = models.PositiveIntegerField(null=True, blank=True)

    
    
     
    
    
    

    

    
    