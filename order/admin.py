from django.contrib import admin
from order.models import OrderItem,Order,OrderShipping
# Register your models here.
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderShipping)