from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def Home(request):
    return render(request,'home.html')


def signup(request):
    if request.method == 'POST':
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        user=User.objects.filter(username=username)

        if user.exists():
            messages.info(request,'User Name already taken')
            return redirect("/register/")
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
            
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Account created successfully')
        return redirect("/login/")

    return render(request,"signup.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            user = authenticate(username = username , password = password)
            if user is not None:
                login(request,user)
                if user.is_superuser or user.is_staff:
                    return redirect('/admin')
                return redirect('/home/')
                
            else:
                messages.info(request,'Invalid Password')
                return redirect('/login/')
            

        else:
            messages.info(request,'Invalid Username')
            return redirect('/login/')
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect("/login/")
