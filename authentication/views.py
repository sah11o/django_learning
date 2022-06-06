import logging
import re
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import path, include
from . import views
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login

#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
def home(request):
      return render(request, "authentication/index.html")
def signin(request):
      if request.method == "POST":
            username= request.POST.get("Name")
            pass1= request.POST.get("Password")
            user = authenticate(username=username,password=pass1)
            if user is not None:
                 # login(request,user)
                 messages.success(request, "You logged in")
                 return redirect("home")
            else: 
                messages.error(request, "login failed, please check your username or password")
                return redirect("signin")
      return render(request, "authentication/signin.html")
def signup(request):
    if request.method == "POST":
        username= request.POST.get("Name")
        email= request.POST.get("Email")
        pass1= request.POST.get("Password")
        pass2= request.POST.get("Confirm Password")
        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()

        messages.success(request, "Your account is created successfully")
        return redirect("signin")
    return render(request, "authentication/signup.html")
def signout(request):
      messages.success(request, "you logged out")
      return redirect("signin")
      