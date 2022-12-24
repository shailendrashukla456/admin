from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def signuppage(request):
    if request.method=="POST":
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        try:
            user=User.objects.get(email=email)
            return render(request,"signup.html")
        except:
            user=User.objects.create_user(first_name=fname,last_name=lname,username=username,email=email,password=password)
            user.save()
            return render(request,'login.html')
    else:
        return render(request,'signup.html')

def loginpage(request):
    if request.method=="POST":
       username=request.POST['username']
       password=request.POST['password']
       user = auth.authenticate(username=username,password=password)
       if user is not None:
            auth.login(request,user)
            return render(request,'home.html')
       else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def home(request):
    return render(request,'home.html')

def logout(request):
    auth.logout(request)
    return render(request,'signup.html')