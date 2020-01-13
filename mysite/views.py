from django.shortcuts import render,HttpResponse,redirect
import json 
from django.http import JsonResponse
from . import settings
import os
import requests 


def index(request):
    file = os.path.join(settings.BASE_DIR,'data.json')
    data = json.load(open(file)) 
    return render(request,"json.html",{'menus':data})
        
def show(request):
    data = requests.get('http://localhost/getapi')
    return HttpResponse(data)
def show(request):
    data = requests.get('http://localhost/get_cat')
    return HttpResponse(data)    
def search(request):
    course = request.GET.get('subject','')
    if len(course)>0:
        file =os.path.join(settings.BASE_DIR,'data.json')
        data = json.load(open(file))
        for stream in data:
            if course in data[stream]:
                return JsonResponse(data[stream][course],safe=False)
    else:
        return JsonResponse({'error':'not found'},safe=False)
 

