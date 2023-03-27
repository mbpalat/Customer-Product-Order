import json
# import pandas as pd
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from .models import OrdLines, Order
from django.views.decorators.csrf import csrf_exempt

def orderList(request):
    return render(request,'order/orderlist.html')

def vieworderlinesList(request,oid):
    return render(request,'order/vieworderlines.html')

def orderlinesList(request,oid):
    return render(request,'order/orderlineslist.html')

#Order

@csrf_exempt
def saveorder(request):
    if request.method == "POST":  
        try:
            body = json.loads(request.body)
            length = len(list(Order.objects.all()))
            print(length)
            order = Order()
            order.id = length+1
            order.ordernumber = body.get('ordernumber','')
            order.customer = body.get('customer','')
            order.customerid = body.get('customerid','')
            order.save()  
            response = {"status": True, "code": 200, "message": "Order saved successfully", "id":order.id}
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)

@csrf_exempt
def editorder(request):
    if request.method == "POST": 
        try:
            body = json.loads(request.body)
            id= body.get('id','')
            order = Order.objects.get(id=id)  
            order.ordernumber = body.get('ordernumber','')
            order.customer = body.get('customer','')
            order.customerid = body.get('customerid','')
            order.save()  
            response = {"status": True, "code": 200, "message": "Order Updated successfully"}
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)


@csrf_exempt
def fetchorders(request):
    if request.method == "GET": 
        try:
            orders = list(Order.objects.all().order_by('id')
                            .values('id', 'ordernumber', 'customer', 'customerid' , 'date'))
            response = {
                        "status": True, 
                        "code": 200,
                        "message": "Order List Fetched Successfully",
                        "orderlist": orders,
                        }
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)

@csrf_exempt
def fetchsingleorder(request, id):
    if request.method == "GET": 
        try:
            orderobj = Order.objects.get(id=id)
            order = {}
            order["id"] = orderobj.id
            order["ordernumber"] = orderobj.ordernumber
            order["customer"] = orderobj.customer
            order["customerid"] = orderobj.customerid
            order["date"] = orderobj.date
            response = {
                        "status": True, 
                        "code": 200,
                        "message": "Order Fetched Successfully",
                        "orders": [],
                        }
            response["orders"].append(order)
            print(response)
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)


@csrf_exempt
def deleteorder(request, id):
    if request.method == "GET": 
        try:
            order = Order.objects.get(id=id)
            orderlines = list(OrdLines.objects.filter(ordernumber=id).values())
            for key in  orderlines:
                ord = key.get('id')
                orderline = OrdLines.objects.get(id=ord)
                orderline.delete()
            order.delete()   
            response = {"status": True, "code": 200, "message": "Order Deleted successfully"}
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)


# Order Lines


@csrf_exempt
def saveorderline(request):
    if request.method == "POST":  
        try:
            body = json.loads(request.body)
            length = len(list(OrdLines.objects.all()))
            print(length)
            orderline = OrdLines()
            orderline.id = length+1
            orderline.ordernumber      = body.get('ordernumber','')
            orderline.orderlinenumber  = body.get('orderlinenumber','')
            orderline.productcode      = body.get('productcode','')
            orderline.productname      = body.get('productname','')
            orderline.customerid       = body.get('customerid','')
            # orderline.date             = body.get('date','')
            orderline.productid        = body.get('productid','')
            orderline.quantity         = body.get('quantity','')
            orderline.price            = body.get('price','')    
            orderline.save()  
            response = {"status": True, "code": 200, "message": "Order Line saved successfully"}
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)

@csrf_exempt
def editorderline(request):
    if request.method == "POST": 
        try:
            body = json.loads(request.body)
            id= body.get('id','')
            orderline = OrdLines.objects.get(id=id)  
            orderline.ordernumber      = body.get('ordernumber','')
            orderline.orderlinenumber  = body.get('orderlinenumber','')
            orderline.productcode      = body.get('productcode','')
            orderline.productname      = body.get('productname','')
            orderline.customerid       = body.get('customerid','')
            # orderline.date             = body.get('date','')
            orderline.productid        = body.get('productid','')
            orderline.quantity         = body.get('quantity','')
            orderline.price            = body.get('price','')    
            orderline.save()  
            response = {"status": True, "code": 200, "message": "Order Line Updated successfully"}
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)


@csrf_exempt
def fetchorderlines(request):
    if request.method == "GET": 
        try:
            orderlines = list(OrdLines.objects.all().order_by('id')
                            .values('id', 'ordernumber', 'orderlinenumber', 'productcode' ,'productname',
                                    'customerid', 'date', 'productid','quantity','price'))
            response = {
                        "status": True, 
                        "code": 200,
                        "message": "OrderLine List Fetched Successfully",
                        "orderlinelist": orderlines,
                        }
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)

@csrf_exempt
def fetchorderlinesbyord(request, ord):
    if request.method == "GET": 
        print(type(ord))
        # params = request.GET
        # ord_no = params.get('order_id', 0)
        try:
            orderlines = list(OrdLines.objects.filter(ordernumber=ord).values())
            response = {
                "status": True, 
                "code": 200,
                "message": "OrderLine List Fetched Successfully",
                "orderlinelist": orderlines,
            }
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)

@csrf_exempt
def fetchsingleorderline(request, id):
    if request.method == "GET": 
        try:
            orderlineobj = OrdLines.objects.get(id=id)
            orderline = {}
            orderline["id"]                 = orderlineobj.id
            orderline["ordernumber"]        = orderlineobj.ordernumber
            orderline["orderlinenumber"]    = orderlineobj.orderlinenumber
            orderline["productcode"]        = orderlineobj.productcode
            orderline["productname"]        = orderlineobj.productname
            orderline["customerid"]         = orderlineobj.customerid
            orderline["date"]               = orderlineobj.date
            orderline["productid"]          = orderlineobj.productid
            orderline["quantity"]           = orderlineobj.quantity
            orderline["price"]              = orderlineobj.price
            response = {
                        "status": True, 
                        "code": 200,
                        "message": "Order Fetched Successfully",
                        "orderline": [],
                        }
            response["orderline"].append(orderline)
            print(response)
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)


@csrf_exempt
def deleteorderline(request, id):
    if request.method == "GET": 
        try:
            orderline = OrdLines.objects.get(id=id)  
            orderline.delete()   
            response = {"status": True, "code": 200, "message": "Order Line Deleted successfully"}
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)
