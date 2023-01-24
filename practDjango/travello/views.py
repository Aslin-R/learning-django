from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1=Destination()
    dest1.name='Mumbai'
    dest1.desc='Crowdest City in India'
    dest1.img='destination_6.jpg'
    dest1.price=10000
    dest1.offer=False

    dest2=Destination()
    dest2.name='Chennai'
    dest2.desc='Gethu city of Tamilnadu'
    dest2.img='destination_2.jpg'
    dest2.price=99000
    dest2.offer=1

    dest3=Destination()
    dest3.name='Pattarivilai'
    dest3.desc='City of Prime Minister'
    dest3.img='destination_7.jpg'
    dest3.price=90
    dest3.offer=True

    dests=[dest1,dest2,dest3]
    #return render(request, 'index.html',{'dest1':dest1,'dest2':dest2})
    return render(request, 'index.html',{'dests':dests})
