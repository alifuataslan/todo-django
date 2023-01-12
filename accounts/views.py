from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from accounts.forms import Loginform,Registerform
from django.contrib import messages



def loginuser(request):
    form=Loginform(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        username= form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user =  authenticate(username=username,password=password)
       

        if user is None:
            messages.info(request,"Kullanıcı veya Parola hatalı....")
            
            return render(request,"login.html",context)
        messages.success(request,"Başarıyla Giriş Yapıldı...")
        login(request,user)
        return redirect("index")


    return render(request,"login.html",context)
def register(request):
    if request.method=="POST":
       form = Registerform(request.POST)
       if form.is_valid():
           username=form.cleaned_data.get("username")
           password=form.cleaned_data.get("password")
           newUser=User(username = username)
           newUser.set_password(password)
           newUser.save()
           login(request,newUser)
           messages.success(request,"Kayıt işlemi Başarılı")
           messages.info(request,"Kayıt işlemi Başarılı")
           return redirect("index")
       context ={
            "form": form
        }
       return render(request,"register.html",context)
        

        
       
    else:
        form=Registerform()
        context ={
            "form": form
        }
        return render(request,"register.html",context)
def index(request):

    return render(request,"index.html")
def logoutuser(request):
        logout(request)
        messages.success(request,"Başarı ile çıkış sağladınız....")
        return redirect("index")