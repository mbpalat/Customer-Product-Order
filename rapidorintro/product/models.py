from django.db import models

# Create your models here.
class Product(models.Model):
    name            =  models.TextField() 
    code            =  models.TextField() 
    unit            =  models.IntegerField() 
    price           =  models.IntegerField()
    tax             =  models.IntegerField()
    percent         =  models.IntegerField()

class Meta:  
        db_table = "product"  