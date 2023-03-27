from django.db import models

# Create your models here.
class Order(models.Model): 
    ordernumber     =  models.IntegerField() 
    customer        =  models.TextField()
    customerid      =  models.IntegerField()
    date            =  models.DateTimeField(auto_now_add=True)

class OrdLines(models.Model): 
    ordernumber     =  models.BigIntegerField()
    orderlinenumber =  models.IntegerField()
    productcode     =  models.TextField()
    productname     =  models.TextField()
    customerid      =  models.IntegerField()
    date            =  models.DateTimeField(auto_now_add=True)
    productid       =  models.IntegerField()     
    quantity        =  models.IntegerField()     
    price           =  models.IntegerField()      

class Meta:  
        db_table = "order"  
        db_table = "ordlines"

  
  
        