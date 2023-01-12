"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views
from notes import views as notesviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',views.loginuser,name="login" ),
    path('register/',views.register,name="register" ),
    path('',views.index,name="index"),
    path('logout/',views.logoutuser,name="logout"),
    path('dashboard/',notesviews.dashboard,name="dashboard"),
    path('detail/<int:id>', notesviews.detail,name="detail"),
    path('note/update/<int:id>',notesviews.update,name="update"),
    path('addnote/',notesviews.addnote,name="addnote"),
    path('deletenote/<int:id>',notesviews.delete,name="delete"),
    path("allnotes/",notesviews.allnotes,name="allnotes")
]
