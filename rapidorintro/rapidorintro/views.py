
import json
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def dashboard(request):
    return render(request,'dashboard.html')



