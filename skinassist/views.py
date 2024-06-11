from django.http import HttpResponse
#from .models import FeedBack
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

def feedback(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        feedback=request.POST['feedback']
        obj=Feedback(name=name,email=email,feedback=feedback)
        obj.save()
        return HttpResponse("<h1>Form page submitted</h1>")

        
    return render(request,'feedback.html')
