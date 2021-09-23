from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .basket import Basket
from base.models import Product
from django.http import JsonResponse
# Create your views here.
def basket_summary(request):
    basket=Basket(request)

    return render(request,'basket/cart.html',{'basket':basket})

def basket_add(request):
    basket=Basket(request)
    if request.POST.get('action')=='post':
        product_id=int(request.POST.get('productid'))
        product=get_object_or_404(Product, id=product_id)
        basket.add(product=product)
        size=basket.__len__()

        response=JsonResponse({'test':size})
        return response
def basket_delete(request):
    basket=Basket(request)
    if request.POST.get('action')=='post':
        product_id=(request.POST.get('productid'))
        basket.delete(product=product_id)
        size=basket.__len__()
        response=JsonResponse({'test':size})
        return response

