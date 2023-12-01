from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request,'index.html')
def aboutus(request):
    return render(request,'aboutus.html')
def check(request):
    return render(request,'check.html')
def policy(request):
    return render(request,'policy.html')
def terms(request):
    return render(request,'terms.html')
def upload(request):
    return render(request,'upload.html')

def agree(request):
    return render(request,'agree.html')
