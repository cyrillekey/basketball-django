from django.shortcuts import render,redirect
from basket.basket import Basket
from order.models import Order,OrderItem
from account.forms import Addressform
from django.http import JsonResponse
# Create your views here
#.
def checkout(request):
    context={}
    if request.user.is_authenticated:
        basket=Basket(request)
        if request.POST:
            form=Addressform(request.POST)
            context['item']=basket.__len__()
        else:
            form=Addressform()
            context['addressform']=form
            context['item']=basket.__len__()    
        return render(request,"order/checkout.html",context)
    else:    
        return redirect('login')
def add(request):
    basket=Basket(request)
    user_id=request.user.id
    baskettotal=basket.get_total_price()
    order_key=""
    if Order.objects.filter(order_key=order_key).exists():
        pass
    else:
        order=Order.objects.create()
        order_id=order.pk
        for item in basket:
            OrderItem.objects.create(order=order_id,product=item['product'],price=item['price'],quantity=item['qty'])
    response=JsonResponse({'success':'Order Created'})    
    return response    
