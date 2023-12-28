from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from django.contrib.auth.hashers import make_password,check_password
# Create your views here.

def courses(request):
    return render(request,'courses.html')

def dashboard(request):
    return render(request,'dashboard.html')

def index(request):
    return render(request,'index.html')

def profile(request):
    return render(request,'profile.html')

def signup(request):
    return render(request,'sign-up.html')

def viewstudents(request):
    return render(request,'viewstudents.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email = email).exists():
            return HttpResponse("Email already Exists")
        else:
            User.objects.create(name = name, email = email, password= make_password(password))
            return HttpResponse("User created successfully")
    
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user_password = request.POST.get('password')

        if User.objects.filter(email = email).exists():
            user_obj = User.objects.get(email = email)
            Password = user_obj.password
        
            if check_password(user_password,Password):
                return redirect('/dashboard/')
            else:
                return HttpResponse("Invalid Password")
        else:
            return HttpResponse("Email not exist")

