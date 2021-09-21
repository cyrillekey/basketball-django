from django.shortcuts import render,redirect
from base.models import Product
# Create your views here.
def home(requests):
    products=Product.objects.all()
    return render(requests,'mainpage/home.html',{'products':products})
    
def singleproduct(requests,slug):
    singleproduct=Product.objects.all().filter(product_slug=slug)    

    return render(requests,'mainpage/single_product.html',{'products':singleproduct})