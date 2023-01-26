from django.shortcuts import render
from requests import request

# Create your views here.

def register(request):
    return render(request, 'account/register.html')