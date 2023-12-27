from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from . models import Emp
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def user(request):
    return HttpResponse("Hello World")

def user(request):
    if request.method == 'POST':
        empname = request.POST['name']
        empemail = request.POST['email']
        emppass= request.POST['password']
        data = Emp(Emp_name=empname,Emp_email=empemail,Emp_password=emppass)
        data.save()
        return render(request,'index.html')
    return render(request,'index.html')


def details(request):
    if request.method == "GET":
        a = Emp.objects.all()
        return render(request,"data.html",{'data':a})
    elif request.method == "POST":
        return HttpResponseRedirect(request.path)    

def Update_record(request):
    if request.method == "POST":
        id = request.POST['id']  
        name = request.POST['name']   
        email = request.POST['email']   
        password = request.POST['password'] 

        b = get_object_or_404(Emp,pk=id)
        b.Emp_name = name
        b.Emp_email = email
        b.Emp_password = password
        b.save()
        return HttpResponseRedirect('/data/')

def Delete_record(request,id):
    if request.method == "POST":
        a = Emp.objects.get(pk=id)
        a.delete()
        return redirect('/data/')

def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        # print(uname,email,pass1,pass2)
        if pass1 != pass2:
            return HttpResponse("Password does not match")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
        # return HttpResponse("User has been created Succesfully")
            return redirect('login')
    return render(request,'signup.html')

def LoginPage(request):
    if request.method =="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        # print(username,pass1)
        user = authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')    
        else:
            return HttpResponse("Username or password is incorrect")

    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')