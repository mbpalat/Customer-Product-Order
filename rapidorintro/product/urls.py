from .import views
from django.urls import path 

urlpatterns = [
        path('', views.productList),
        
        path('saveproduct', views.saveproduct),  
        path('editproduct', views.editproduct),  
        path('fetchproducts', views.fetchproducts),
        path('fetchsingleproduct/<int:id>', views.fetchsingleproduct),  
        path('deleteproduct/<int:id>', views.deleteproduct),  
]