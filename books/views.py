from django.shortcuts import render
from django.http import JsonResponse
from .models import Author
import random
import os
import psutil




# Create your views here.
def some_view(request):
    query = Author.objects.all()
    authors = []
    for obj in query:
        tempData={
        "name" : obj.name,
        "city": obj.city,
        }
        authors.append(tempData)
    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0]/2.**30  # memory use in GB.(probably)
    data = {}
    data['success']=True
    data['usage']= memoryUse
    data['item'] = authors

    print('-----------', memoryUse )
    return JsonResponse(data,safe=False) 

def optimized_view(request):
    query = Author.objects.all().iterator()
    authors = []
    for obj in query:
        tempData={
        "name" : obj.name,
        "city": obj.city,
        }
        authors.append(tempData)

    pid = os.getpid()
    py = psutil.Process(pid)
    memoryUse = py.memory_info()[0]/2.**30  # memory use in GB.
    data = {}
    data['success']=True
    data['usage']= memoryUse
    data['item'] = authors

    print('-----------', memoryUse )

    return JsonResponse(data,safe=False) 


def add_data(request):
    names=['Anc','Niaf','TRewo','Uihw','Fgbjig','Haof','ADFngrw','Reaqrw']
    cities = ['fabdj','aguf','agbiuhei','gajeifgq','gaejk','agjea','gake','agbkje']
    
    for i in range(1,1000):
        
        p = Author(name=(random.choices(names)), city=(random.choices(cities)))
        p.save()