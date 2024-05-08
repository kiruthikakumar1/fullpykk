from django.db import models
import datetime
import os
# Create your models here.
class Company(models.Model):
  company_name=models.CharField(max_length=150,null=False,blank=False)
  company_username=models.CharField(max_length=150,null=False,blank=False)
  company_email=models.CharField(max_length=150,null=False,blank=False)
  company_create_password=models.CharField(max_length=8,null=False,blank=False)
  company_image=models.ImageField(upload_to="img/%y",null=True,blank=True)
  company_description=models.TextField(null=False,blank=False)
  company_contact=models.BigIntegerField(null=False,blank=False)
  company_address=models.CharField(max_length=100,null=False,blank=False)
  company_bankname=models.CharField(max_length=100,null=False,blank=False)
  company_accountNo=models.BigIntegerField(null=False,blank=False)
  company_ifsc=models.CharField(max_length=10,null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self) :
    return self.company_name
 
class Product(models.Model):
  company=models.ForeignKey(Company,on_delete=models.CASCADE)
  product_name=models.CharField(max_length=150,null=False,blank=False)
  product_image=models.ImageField(upload_to="img/%y",null=True,blank=True)
  product_originalPrice=models.IntegerField(null=False,blank=False)
  product_sellingPrice=models.IntegerField(null=False,blank=False)
  product_color=models.CharField(max_length=100,null=False,blank=False)
  product_battery=models.CharField(max_length=100,null=False,blank=False)
  product_storage=models.CharField(max_length=100,null=False,blank=False)
  product_screen=models.CharField(max_length=100,null=False,blank=False)
  product_network=models.CharField(max_length=100,null=False,blank=False)
  product_features=models.TextField(null=False,blank=False)
  status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
  trending=models.BooleanField(default=False,help_text="0-default,1-Trending")
  created_at=models.DateTimeField(auto_now_add=True)
 
  def __str__(self) :
    return self.product_name

class Customer(models.Model):
  user_fname=models.CharField(max_length=150,null=False,blank=False)
  user_lname=models.CharField(max_length=150,null=False,blank=False)
  user_email=models.CharField(max_length=150,null=False,blank=False)
  user_create_password=models.CharField(max_length=8,null=False,blank=False)
  user_dob=models.DateField(null=False,blank=False)
  user_city=models.CharField(max_length=100,null=False,blank=False)
  user_state=models.CharField(max_length=100,null=False,blank=False)
  user_pincode=models.IntegerField(null=False,blank=False)
  user_contact=models.BigIntegerField(null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)
  
  def __str__(self) :
    return self.user_fname


class Order(models.Model):
  oduserfname=models.CharField(max_length=150,null=False,blank=False)
  odcomname=models.CharField(max_length=150,null=False,blank=False)
  odproname=models.CharField(max_length=150,null=False,blank=False)
  odprocolor=models.CharField(max_length=150,null=False,blank=False)
  odprostorage=models.CharField(max_length=150,null=False,blank=False)
  odproprice=models.IntegerField(null=False,blank=False)
  odprobattery=models.CharField(max_length=100,null=False,blank=False)
  odproscreen=models.CharField(max_length=100,null=False,blank=False)
  odpronetwork=models.CharField(max_length=100,null=False,blank=False)
  
  def __str__(self) :
    return self.oduserfname