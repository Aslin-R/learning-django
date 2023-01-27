from django.shortcuts import render,redirect
from requests import request
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def login(request):
    if (request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/travello')
        else:
            messages.info(request,'invalid data')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already exists !')
                print('user name already existed')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email is already Taken!')
                print('email already existed')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
            
        else:
            print('password not matched')
            messages.info(request,"Password is not matching!!!")
            return redirect('register')
        return redirect('/travello')
    else:
        return render(request, 'account/register.html')