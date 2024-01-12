from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def SignupPage(request):
    if request.method=='POST':
      uname=request.POST.get('username')
      email=request.POST.get('email')
      pass1=request.POST.get('password1')
      pass2=request.POST.get('password2')
      if pass1!=pass2:
         return HttpResponse("passowrds do not match")
      else:
        my_user=User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect('login')
    return render (request,'signup.html')

def loginPage(request):
   if request.method=='POST':
      username=request.POST.get('username')
      pass1=request.POST.get('pass')
      user=authenticate(request,username=username,password=pass1)
      if user is not None:
         login(request,user)
         return redirect('home')
      else:
         return HttpResponse("invalid data")  
    
   return render (request,'login.html')