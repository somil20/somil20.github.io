from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib import auth
# Create your views here.
def index(request):
    context = {
        "variable":"Devansh Mourya",
        "variable2":"Ice-Cream",
        }
   # messages.success(request,"this is a test message")
    return render(request, "index.html", context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request,"about.html")
  

def services(request):
    return render(request,"services.html")
  

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,"contact.html")

def login(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        y = auth.authenticate(username = username1, password = password1)
        if y is None:
            return redirect('login')
        else :
            return redirect('/welcome')
   
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email_id')
        password = request.POST.get('password')
      

        x = User.objects.create_user(username = username, email = email, password = password)
        x.save()
       
        print("user created")
        return redirect('/login')

    else:
        return render(request, "signup.html")
def welcome(request):
    return render(request, "welcome.html")

def cuser(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        Mobile = request.POST.get('MobileNO.')
        aadhar = request.POST.get('AadharNo')
        email = request.POST.get('email_id')
        password = request.POST.get('password')
      

        x = User.objects.create_user(fname = firstname, lname = lastname, mobile = Mobile, aadhar = aadhar, email = email, password = password)
        x.save()
       
        print("user created")
        return redirect('/cuser')

    else:
        return render(request, "cuser.html")
