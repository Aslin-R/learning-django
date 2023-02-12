from django.shortcuts import render
from django.http import *
from myapp.forms import BookingForm
from .models import Menu

def intro(): 
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

def menus(request):
    newmenu={'mains':[
        {'name':'Biriyani','price':'120'},
        {'name':'Parota','price':'15'},
        {'name':'Chapathi','price':'10'}
    ]}
    return render(request,'menu.html',newmenu)

def menu_by_id(request):
    newmenu=Menu.objects.all()
    newmenu_dict={'menu':newmenu}
    print(newmenu_dict)
    return render(request,'menu_card.html',newmenu_dict)


def register(request): 
    return render(request, "register.html", {}) 

def login(request): 
    return render(request, "login.html", {}) 

#week 4 lab

def home(request): 
    return render(request, "home.html") 

def about(request):
    return render(request,'about.html')

def book(request): 
    return render(request, "book.html") 

def index(request): 
    return render(request, "index.html") 
def base(request): 
    return render(request, "base.html") 
