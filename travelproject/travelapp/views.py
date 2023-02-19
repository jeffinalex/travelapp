from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Place
def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'index2.html')
def  register(request):
    if request.method=='POST':
        username=request.POST["username"]
        firstname = request.POST["first_name"]
        secondname = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        confpassword = request.POST["password1"]
        if password==confpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                            last_name=secondname, email=email)

                user.save();
                return redirect('login')

        else:
            messages.info(request,'password not matching')
            return redirect('register')
        return  redirect('/')
    return render(request,'index1.html')
def logout(request):
    auth.logout(request)
    return redirect('/')