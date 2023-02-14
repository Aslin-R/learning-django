from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print('Hello World')
    return HttpResponse('<h1>Welcome to Insta Book<h1>')