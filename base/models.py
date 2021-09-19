from django.db import models

# Create your models here.
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
    stock=models.IntegerField()
    is_new=models.BooleanField(default=False)
    product_size=models.CharField(max_length=255,choices=SIZE)  
    category=models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural="Products"
        ordering=('-created',)  
    def __str__(self):
        return self.product_name

class Order(models.Model):
    pass

