from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from .models import User

from django.contrib.sessions.models import Session
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email Already Exists ..")
            return redirect('/signup')
        else:
            user = User(name=name,email=email,password=password)
            user.save()
            messages.success(request,"Your Acoount Registered with Us")
            return redirect('/')
    return render(request,'signup.html')

def userlogin(request):
   
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        
        return render(request,'home.html')

    return render(request,'login.html')


def home(request):

    return render(request,'home.html',{"name":name})



def notifications(request):
    return render(request,'notifications.html')

def charts(request):
    return render(request,'charts.html')

def orders(request):
    return render(request,'orders.html')

