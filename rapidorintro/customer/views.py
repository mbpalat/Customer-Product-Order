import json
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from .models import Customer
from django.views.decorators.csrf import csrf_exempt

def customerList(request):
    return render(request,'customer/customerlist.html')

@csrf_exempt
def savecustomer(request):
    if request.method == "POST":  
        try:
            body = json.loads(request.body)
            length = len(list(Customer.objects.all()))
            print(length)
            customer = Customer()
            customer.id = length+1
            customer.customername = body.get('customername','')
            customer.username = body.get('username','')
            customer.mobile = body.get('mobile','')
            customer.save()  
            response = {"status": True, "code": 200, "message": "Customer saved successfully"}
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)

@csrf_exempt
def editcustomer(request):
    if request.method == "POST": 
        try:
            body = json.loads(request.body)
            id= body.get('id','')
            customer = Customer.objects.get(id=id)  
            customer.customername = body.get('customername','')
            customer.username = body.get('username','')
            customer.mobile = body.get('mobile','')
            customer.save()    
            response = {"status": True, "code": 200, "message": "Customer Updated successfully"}
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)


@csrf_exempt
def fetchcustomers(request):
    if request.method == "GET": 
        try:
            customers = list(Customer.objects.all().order_by('id')
                            .values('id', 'customername', 'username', 'mobile'))
            response = {
                        "status": True, 
                        "code": 200,
                        "message": "Customer List Fetched Successfully",
                        "customerlist": customers,
                        }
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)

@csrf_exempt
def fetchsinglecustomer(request, id):
    if request.method == "GET": 
        try:
            customerobj = Customer.objects.get(id=id)
            customer = {}
            customer["id"] = customerobj.id
            customer["customername"] = customerobj.customername
            customer["username"] = customerobj.username
            customer["mobile"] = customerobj.mobile
            response = {
                        "status": True, 
                        "code": 200,
                        "message": "Customer Fetched Successfully",
                        "customers": [],
                        }
            response["customers"].append(customer)
            print(response)
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)


@csrf_exempt
def deletecustomer(request, id):
    if request.method == "GET": 
        try:
            customer = Customer.objects.get(id=id)  
            customer.delete()   
            response = {"status": True, "code": 200, "message": "Customer Deleted successfully"}
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)
