from django.shortcuts import render,redirect

# Create your views here.
def home(requests):
    return render(requests,'mainpage/home.html')