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

def Findjob(request):
    context={}
    queryset = Jobs.objects.all()
    total_jobs = queryset.count()
    context['total_jobs'] = total_jobs
    context['jobs']=queryset
    return render(request,'findjob.html',context)

def Benefits(request):
    return render(request,'benefits.html')

def Apply(request):
    return render(request,'apply.html')

def search(request):
    if request.method == 'GET':
        location=request.PORT.get("location")
        if location:
            results = Jobs.objects.filter(job_location=location)
            return render(request, 'findjob.html', {'results': results})
    
    return render(request, 'findjob.html', results)


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

@login_required(login_url="/login/")
def adddetails(request):
    context={}
    context['show_form']=True
    try:
        data = Details.objects.get(user__username=request.user.username)
        context['show_form']=False
    except:
        if request.method=="POST":
            full_name=request.POST.get("full_name")
            email=request.POST.get("email")
            areain=request.POST.get("areain")
            mobile_no=request.POST.get("mobile_no")
            address=request.POST.get("address")
            cv=request.POST.get("file")
            user = request.user
            Details.objects.create(
                user=user,
                full_name=full_name,
                email=email,
                mobile_no=mobile_no,
                areain=areain,
                address=address,
                cv=cv
            )
            messages.info(request,'Submitted')
            
    

    return render(request,'adddetails.html',context)

