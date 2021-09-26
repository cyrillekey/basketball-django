from django.contrib import admin
from .models import  Category,Product
from django.utils.text import slugify
# Register your models here.
admin.site.register(Category)
#@admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={"product_slug":(slugify("(product_name)"),)}
admin.site.register(Product,ProductAdmin)    