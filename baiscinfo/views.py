from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def homepage(request):
    return render(request,"info.html")
def getdata(request):
    un = request.GET['uname']
    p = request.GET['pass']
    pn = request.GET['phno']
    ad = request.GET['addr']
    s1 = models.Student(Username = un, Password = p, Phone_number = pn, Address = ad)
    s1.save()
    return render(request, "display.html", {"Username": un, "Password": p, "Phone_number": pn, "Address": ad})
