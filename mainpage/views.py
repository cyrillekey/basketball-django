from django.shortcuts import render,redirect,HttpResponse
from base.models import Product,Category
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
def home(requests):
    products=Product.objects.all()[0:4]
    new_products=Product.objects.all().filter(is_new=True).order_by('?') & Product.objects.all().filter(stock__gte=1)[0:3]
    return render(requests,'mainpage/home.html',{'products':products,'new_products':new_products})
    
def singleproduct(requests,slug):
    singleproduct=Product.objects.all().filter(product_slug=slug)    

    return render(requests,'mainpage/single_product.html',{'products':singleproduct})
def faq(request):
    return render(request,'mainpage/faq.html')   
def allproducts(request):
    page=request.GET.get('page',1)
    product=Product.objects.all().filter(stock__gte=1)
    paginator=Paginator(product,12)
    categories=Category.objects.all()
    try:
        product_page=paginator.page(page)
    except PageNotAnInteger:
        product_page=paginator.page(1)
    except EmptyPage:
        product_page=paginator.page(paginator.num_pages)    
    print(categories)    
    return render(request,'mainpage/allproducts.html',{'products':product_page,'categories':categories})     
def search(request):
    
    searchword=request.GET.get('searchword') 
    product=Product.objects.filter(product_name__icontains=searchword) & Product.objects.all().filter(stock__gte=1)
   
    return render(request,'mainpage/allproducts.html',{'products':product})     
def filter(request,filtername):
    if filtername=="lowest":
        page=request.GET.get('page',1)
        product=Product.objects.all().filter(stock__gte=1).order_by("product_price")
        paginator=Paginator(product,12)
        categories=Category.objects.all()
        try:
            product_page=paginator.page(page)
        except PageNotAnInteger:
            product_page=paginator.page(1)
        except EmptyPage:
            product_page=paginator.page(paginator.num_pages)    
        print(categories)    
        return render(request,'mainpage/allproducts.html',{'products':product_page,'categories':categories})  
    elif filtername=='highest':
        page=request.GET.get('page',1)
        product=Product.objects.all().order_by("-product_price")
        paginator=Paginator(product,12)
        categories=Category.objects.all()
        try:
            product_page=paginator.page(page)
        except PageNotAnInteger:
            product_page=paginator.page(1)
        except EmptyPage:
            product_page=paginator.page(paginator.num_pages)    
        print(categories)    
        return render(request,'mainpage/allproducts.html',{'products':product_page,'categories':categories})  
    else:
        page=request.GET.get('page',1)
        product=Product.objects.filter(category=filtername)
        paginator=Paginator(product,12)
        categories=Category.objects.all()
        try:
            product_page=paginator.page(page)
        except PageNotAnInteger:
            product_page=paginator.page(1)
        except EmptyPage:
            product_page=paginator.page(paginator.num_pages)    
        print(categories)    
        return render(request,'mainpage/allproducts.html',{'products':product_page,'categories':categories})      