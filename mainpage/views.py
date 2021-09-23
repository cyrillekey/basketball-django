from django.shortcuts import render,redirect
from base.models import Product
# Create your views here.
def home(requests):
    products=Product.objects.all()[0:4]
    new_products=Product.objects.all().filter(is_new=True).order_by('?')[0:3]
    return render(requests,'mainpage/home.html',{'products':products,'new_products':new_products})
    
def singleproduct(requests,slug):
    singleproduct=Product.objects.all().filter(product_slug=slug)    

    return render(requests,'mainpage/single_product.html',{'products':singleproduct})
def faq(request):
    return render(request,'mainpage/faq.html')   
def allproducts(request):
    product=Product.objects.all()
    return render(request,'mainpage/allproducts.html',{'products':product})     