from django.db import models
from order.models import Order
from account.models import Account
# Create your models here.
class Paymentinfo(models.Model):
    payment_reference_id=models.CharField(max_length=50)
    payment_platform=models.CharField(max_length=50)
    payment_amount=models.IntegerField()
    payment_status=models.BooleanField()
    order_id=models.ForeignKey(Order,on_delete=models.CASCADE)
    paymnet_date=models.DateTimeField(auto_now=True)
    #request_id=models.CharField(max_length=52,unique=True)
