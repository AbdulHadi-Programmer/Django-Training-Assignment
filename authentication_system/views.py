from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def login_page(request):
    result = ""
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('home')   # After login redirect to home page
        else:
            result = "Username or Password is Invalid"

    return render(request, 'main.html', {'result':result})

def signup_page(request):
    if request.method=="POST":
        # Get username,email and password from signup form
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # Add User data to User Model
        user_data = User.objects.create_user(username,email,password)
        user_data.save()
        return redirect("login")         # redirect to login page

    return render(request, "signup.html")

def logoutpage(request):
    logout(request)
    return redirect("login")

def home(request):
    return render('main.html')