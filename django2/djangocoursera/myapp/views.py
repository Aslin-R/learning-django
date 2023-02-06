from django.shortcuts import render
from django.http import *
# Create your views here.

def intro(request): 
    
    return HttpResponse("Welcome to Django") 

def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

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