from .import views
from django.urls import path 

urlpatterns = [
        path('', views.orderList),
        path('vieworderlines/<int:oid>', views.vieworderlinesList),
        path('orderlines/<int:oid>', views.orderlinesList),
        
        path('saveorder', views.saveorder),  
        path('editorder', views.editorder),  
        path('fetchorders', views.fetchorders),
        path('fetchsingleorder/<int:id>', views.fetchsingleorder),  
        path('deleteorder/<int:id>', views.deleteorder),  

        path('saveorderline', views.saveorderline),  
        path('editorderline', views.editorderline),  
        path('fetchorderlines', views.fetchorderlines),
        path('fetchorderlinesbyord/<int:ord>', views.fetchorderlinesbyord),
        path('fetchsingleorderline/<int:id>', views.fetchsingleorderline),  
        path('deleteorderline/<int:id>', views.deleteorderline),

]