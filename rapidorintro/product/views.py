import json
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from .models import Product
from django.views.decorators.csrf import csrf_exempt

def productList(request):
    return render(request,'product/productlist.html')

@csrf_exempt
def saveproduct(request):
    if request.method == "POST":  
        try:
            body = json.loads(request.body)
            length = len(list(Product.objects.all()))
            product = Product()
            product.id = length+1
            product.name = body.get('name','')
            product.code = body.get('code','')
            product.unit = body.get('unit','')
            product.price = body.get('price','')
            product.tax = body.get('tax','')
            product.percent = body.get('percent','')
            product.save()  
            response = {"status": True, "code": 200, "message": "Product saved successfully"}
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)

@csrf_exempt
def editproduct(request):
    if request.method == "POST": 
        try:
            body = json.loads(request.body)
            id= body.get('id','')
            product = Product.objects.get(id=id)  
            product.name = body.get('name','')
            product.code = body.get('code','')
            product.unit = body.get('unit','')
            product.price = body.get('price','')
            product.tax = body.get('tax','')
            product.percent = body.get('percent','')
            product.save()    
            response = {"status": True, "code": 200, "message": "Product Updated successfully"}
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)


@csrf_exempt
def fetchproducts(request):
    if request.method == "GET": 
        try:
            products = list(Product.objects.all().order_by('id')
                            .values('id', 'name', 'code', 'unit', 'price', 'tax', 'percent'))
            response = {
                        "status": True, 
                        "code": 200,
                        "message": "Product List Fetched Successfully",
                        "productlist": products,
                        }
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)

@csrf_exempt
def fetchsingleproduct(request, id):
    if request.method == "GET": 
        try:
            productobj = Product.objects.get(id=id)
            product = {}
            product["id"] = productobj.id
            product["name"] = productobj.name
            product["code"] = productobj.code
            product["unit"] = productobj.unit
            product["price"] = productobj.price
            product["tax"] = productobj.tax
            product["percent"] = productobj.percent
            response = {
                        "status": True, 
                        "code": 200,
                        "message": "Product Fetched Successfully",
                        "products": [],
                        }
            response["products"].append(product)
            print(response)
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)


@csrf_exempt
def deleteproduct(request, id):
    if request.method == "GET": 
        try:
            product = Product.objects.get(id=id)  
            product.delete()   
            response = {"status": True, "code": 200, "message": "Product Deleted successfully"}
        except Exception as e:
            print(e)
            response = {"status": False, "code": 500, "message": "Internal Server Error"}
    return JsonResponse(response, safe=False)
