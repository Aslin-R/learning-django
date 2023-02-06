from django.shortcuts import render
from django.http import *
# Create your views here.

def info(request):
    
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
  
def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 


def showform(request): 
    return render(request,'templates/form.html') 


def drinks(request,drink_name):
    drink={
        'mocha':'type of coffee',
        'tea':'type of beverage'
    }
    choice_of_drink =drink[drink_name]
    return HttpResponse(f"<h2>{drink_name} <br>{choice_of_drink} </h2>")

def menu(request,num):
    items=['Dosai','Puttu','Biriyani']
    return HttpResponse(f'<h2>{items[num]}</h2>')

def home(request):
    return HttpResponse('Welcome to Little Lemon!')

def about(request):
    return HttpResponse('About us')

def book(request):
    return HttpResponse('Make a booking')

from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # do something with the form data
            # ...
            return HttpResponse("Form submitted successfully.")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})