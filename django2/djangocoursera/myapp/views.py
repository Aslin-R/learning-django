from django.shortcuts import render
from django.http import *
from myapp.forms import LogForm
from myapp.forms import BookingForm


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

def forms_view(request):
     form = LogForm()
     if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
     context = {"form" : form}
     return render(request, "home.html", context)

def form_view(request):
     form = BookingForm()
     if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
             form.save()
     context = {"form" : form}
     return render(request, "booking.html", context)