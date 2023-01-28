from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Just think like an engineer")

def aslin(request):
    return HttpResponse("I am Aslin-R")





