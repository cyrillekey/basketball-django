from django.db import models
import requests
from decouple import config
import json
from urllib.parse import urljoin
# Create your models here.

class ProductManager():
    def get_queryset(self):
        return super(ProductManager,self).get_queryset().filter(is_active=True)

class Category(models.Model):
    category_name= models.CharField(max_length=255)
    category_type=models.CharField(max_length=255)
    class Meta:
        verbose_name_plural="categories"
    def __str__(self):
        return self.category_name    

class Product(models.Model):
    X="X"
    L="L"
    M="M"
    XL="XL"
    XLL="XXL"
    SIZE=[(X,"X"),(L,"L"),(M,"M"),(XL,"XL"),(XLL,"XXL")]
    product_name = models.CharField(max_length=25)
    product_description=models.CharField(max_length=200)
    product_price=models.IntegerField()
    product_slug=models.SlugField(max_length=255,unique=True)
    product_image=models.ImageField(upload_to="media/")
    product_image1=models.ImageField(upload_to="media/",null=True)
    product_image2=models.ImageField(upload_to="media/",null=True)
    product_image3=models.ImageField(upload_to="media/",null=True)
    stock=models.IntegerField()
    is_new=models.BooleanField(default=False)
    product_size=models.CharField(max_length=255,choices=SIZE)  
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    products=ProductManager()
    class Meta:
        verbose_name_plural="Products"
        ordering=('-created',)  
    def __str__(self):
        return self.product_name
    def save(self,*args,**kwargs):
        facebook(self.product_image)
        super(Product,self).save(*args,**kwargs)


def facebook(image):
    url=urljoin('http://3109-41-212-104-46.ngrok.io/media/',str(image))
    response=requests.post("https://graph.facebook.com/"+config("PAGE_ID")+"/photos?url="+str(url)+"&access_token="+config("FACEBOOK_ACCESS_TOKEN"))
    response=json.loads(response.text)
    print(response)
    print(url)
    
