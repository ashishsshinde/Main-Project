from email import message
from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from home.models import contactForm
from rest_framework.renderers import JSONRenderer
from rest_framework import serializers
from .serializers import contactForm
from .serializers import call


# Create your views here.

def index(request):
    return render(request,'home/register.html')


    # view for user registration
def UserRegistration(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password= request.POST['password']
        cpassword= request.POST['cpassword']

        # first we will valiadate that user already exist
        user = User.objects.filter(Email=email)

        if user:
            message = "User Already Exist"
            return render(request,'home/register.html',{'msg' : message})
        else:
            if password == cpassword:
                newuser = User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message = "User register Successfully"
                return render(request,"home/login.html",{'msg' : message})
            else:
                message = "Password and Confirm password Does Not Match"
                return render(request,"home/register.html",{'msg' : message})


#login view
def loginpage(request):
    return render(request,'home/login.html')

def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        #Checking the email id with database
        user = User.objects.get(Email = email)
        if user:
            if user.Password == password:
                # We are getting user data in session
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = user.Email
                return render(request,'home/home.html')
            else:
                message = "Password Does Not Match"
                return render(request,'home/login.html',{'msg':message})
        else:
            message = "User Does Not Exist"
            return render(request,'home/register.html',{'msg':message})

def student(request):
    return redirect('https://studentlearningbca.github.io/T/index.html')

def buy(request):
    return render(request,'home/buy.html')



def contact1(request):
    if request.method == "POST":
        names = request.POST.get('name')
        emailAddress = request.POST.get('emailAddress')
        message = request.POST.get('message')
        
        # return HttpResponse(fromdate)
        Visit111 = contactForm(names=names, emailAddress=emailAddress,
                         message=message)
        Visit111.save()

    return render(request,'home/contact1.html')




# def contact(request):       
#     if request.method == "POST":
#         username = request.POST.get('username')
#         email = request.POST.get('email')               
#         query = request.POST.get('query')               
#         Visitlll = contact(username=username, email=email,query=query)                         
#         Visitlll.save()


#     # data = {
#     #     "title": "Home Page",
#     #     "description": "BAAP AGRO!!!"
#     # }3
#     return render(request,'home/contact.html')


def visit(request):
    # return HttpResponse("Hello!! I am on homepage")
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('email')
        
        # return HttpResponse(fromdate)
        Visit11 = call(name=name, surname=surname)
                         
        Visit11.save()
    
    return render(request, 'home/call.html')
