from django.shortcuts import render
from django.http import *
# Create your views here.

def home(request):
    
    path=request.path
    scheme=request.scheme
    method=request.method
    address=request.META['REMOTE_ADDR']
    user_agent=request.META['HTTP_USER_AGENT']
    path_info=request.path_info
    response=HttpResponse()
    response.headers['Name']='Aslin R'

    msg=f""" <br>
    <br>Path:{path}
    <br>Scheme:{scheme}
    <br>Method:{method}
    <br>Address:{address}
    <br>User Agent:{user_agent}
    <br>Path Info:{path_info}
    <br>Response Header:{response.headers}
    """
    return HttpResponse(msg)

def aslin(request):
    return HttpResponse("I am Aslin-R")
    
def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 


def showform(request): 
    return render(request,'templates/form.html') 

def menuitems(request,dish):
    items={
        'biriyani':"chicken biriyani is nice",
        'parota':'Parota with chicken'
    }
    desc=items[dish]
    return HttpResponse(f"<h2> {dish} </h2>"+desc)

def drinks(request,drink_name):
    drink={
        'mocha':'type of coffee',
        'tea':'type of beverage'
    }
    choice_of_drink =drink[drink_name]
    return HttpResponse(f"<h2>{drink_name} <br>{choice_of_drink} </h2>")


