from ast import keyword
from dis import show_code
from email import message
from pyexpat.errors import messages
from turtle import title
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse
from notes.forms import Listeform
from notes.models import Notes
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime

@login_required(login_url="/login/")
def dashboard(request):
    keyword=request.GET.get("keyword")
    notes = Notes.objects.filter(author = request.user, notes_show=True)
    if keyword:
        notes=Notes.objects.filter(title__contains=keyword,notes_show=True)
        
        context={
        "notes":notes
        }




        return render(request,"dashboard.html",context)


    
    context={
        "notes":notes
    }




    return render(request,"dashboard.html",context)
@login_required(login_url="/login/")
def detail(request,id):
    d=datetime.datetime.now()
    note=Notes.objects.filter(id=id , notes_show=True).first()
    if note:
        return render(request,"detail.html",{"note":note})
    messages.info(request,"Böyle Bir Notunuz Bulunmamaktadır...")
    return redirect(reverse("dashboard"))




@login_required(login_url="/login/")
def update(request,id):
    note=get_object_or_404(Notes,id=id,author = request.user)
    form= Listeform(request.POST or None,request.FILES or None,instance=note)
    if form.is_valid():
  
        note = form.save(commit=False)
        note.author=request.user
        note.save()



        messages.success(request,"Not Başarıyla Değiştirildi..")
        return redirect(reverse("detail", kwargs ={"id":id}))


    context={
        "form":form
    }
  

    messages.success(request,"Böyle Bir Not Bulunmuyorr...")
    return render(request,"addnote.html",context)
    


@login_required(login_url="/login/")
def addnote(request):
    form= Listeform(request.POST or None,request.FILES or None)
    if form.is_valid():

        note = form.save(commit=False)
        note.author=request.user
        note.save()



        messages.success(request,"Makale Başarıyla Oluşturuldu")
        return redirect(reverse("dashboard"))


    context={
        "form":form
    }
  


    return render(request,"addnote.html",context)

@login_required(login_url="/login/")
def delete(request,id):
     note=get_object_or_404(Notes,id=id,author = request.user)
     note.deleted_date=datetime.datetime.now()
     note.notes_show=False
     note.save()

     messages.success(request,"Not Başarı İle Silinmiştir....")
     return redirect("dashboard")
def allnotes(request):
    notes=Notes.objects.filter(notes_show=True)
    context={
        "notes":notes
    }
    return render(request,"dashboard.html",context)