from django.db import models

# Create your models here.
class Customer(models.Model):
    customername    =  models.TextField() 
    username        =  models.TextField() 
    mobile          =  models.TextField() 

class Meta:  
        db_table = "customer"  