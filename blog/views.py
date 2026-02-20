from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse("Ursheeta make your self strong!")
def iphone(request,id):
    return HttpResponse(f"show colour of iphone{id}")

def iphone15(request,year):
    return HttpResponse(f"show the year of iphone15{year}")

def iphone(request,name):
    return HttpResponse(f"give your name{name}")

def login(request):
    return render(request,'login/lodin.html')        
