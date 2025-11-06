from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string(request):
    return HttpResponse("this is my first deploy")
def strings(request):
    return HttpResponse("this is my first deploy")
def queryper(request):
    name=request.GET.get("name"," ")
    return HttpResponse(f"hello {name}")

