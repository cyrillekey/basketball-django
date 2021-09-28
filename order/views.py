from django.shortcuts import render,redirect
from basket.basket import Basket
# Create your views here
#.
def checkout(request):
    if request.user.is_authenticated:
        basket=Basket(request)
        return render(request,"order/checkout.html",{'basket':basket})
    else:    
        return redirect('login')