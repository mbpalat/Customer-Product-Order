from .import views
from django.urls import path 

urlpatterns = [
        path('', views.customerList),
        
        path('savecustomer', views.savecustomer),  
        path('editcustomer', views.editcustomer),  
        path('fetchcustomers', views.fetchcustomers),
        path('fetchsinglecustomer/<int:id>', views.fetchsinglecustomer),  
        path('deletecustomer/<int:id>', views.deletecustomer),  
]