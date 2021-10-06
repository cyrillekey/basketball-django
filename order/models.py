from django.db import models
from decimal import Decimal
from django.conf import settings
from django.db import models
from base.models import Product


class Order(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='order_user')
    #full_name=models.CharField(max_length=50)
    #town=models.CharField(max_length=250)
    #phone=models.CharField(max_length=14)
    #post_code=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    total_paid=models.IntegerField()
    order_key=models.CharField(max_length=250)
    order_status=models.CharField(max_length=25)
    payment_status=models.BooleanField(default=False)
    voucher_code=models.CharField(max_length=250)

    class Meta():
        ordering=('-created',)
    def __str__(self):
        return str(self.order_key)    


class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product=models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price=models.IntegerField()
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
