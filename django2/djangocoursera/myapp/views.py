from django.shortcuts import render
from django.http import *
from myapp.forms import BookingForm
from django.contrib.auth.decorators import login_required 

def intro(request): 
    return HttpResponse("Welcome to Django") 


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

def form_view(request):
     form = BookingForm()
     if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
             form.save()
     context = {"form" : form}
     return render(request, "booking.html", context)

def about(request):
        about_content={'about':"Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."}

        return render(request,'about.html',about_content)

def menus(request):
    content={'items':"Biriyani,parota,chicken,kuruma"}
    return render(request,'menu.html',content)

