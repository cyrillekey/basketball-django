from django.contrib import admin
from order.models import OrderItem,Order
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)