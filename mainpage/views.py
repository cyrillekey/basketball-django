from django.shortcuts import render,redirect
from base.models import Product
# Create your views here.
def home(requests):
    products=Product.objects.all()
    return render(requests,'mainpage/home.html',{'products':products})
