from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import user


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def signin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    else:
        return render(request, 'signin.html')
    
def register(request):

    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email') 
        password1 = request.POST.get('password')
        password2 = request.POST.get('password2')

        user = User.objects.create_user(username=username, password=password1, email=email, firstname=firstname, lastname=lastname)
        user.save();
        print("user created successfully") 
        return redirect('/')
    else:
        return render(request, 'register.html')



