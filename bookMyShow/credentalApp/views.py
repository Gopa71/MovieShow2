from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def Register(req):
    if req.method=='POST':
        username=req.POST['username']
        first_name=req.POST['first_name']
        last_name=req.POST['last_name']
        email=req.POST['email']
        password=req.POST['password']
        compassword=req.POST['c_password']
        if password==compassword:
           if User.objects.filter(username=username).exists():
              messages.info(req,"Username Already Taken")
              return redirect('Register')
           elif User.objects.filter(email=email).exists():
              messages.info(req,"Email Already Taken")
              return redirect('Register')
           else:
              user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)

              return redirect('Login')
    
        else:
            messages.info(req,"password not Match")
            return redirect('Register')       
    return render(req,'Reg.html')



def login(req):
   if req.method=='POST':
        username=req.POST['username']
        password=req.POST['password']
        user=auth.authenticate(username=username,
        password=password)
        print(user)
        if user is not None:
            auth.login(req,user)
            return redirect('/')
        else:
            messages.info(req,"invalid User")
            return redirect('Login')


   return render(req,'login.html')
def logout(req):
    auth.logout(req)
    return redirect('/')
