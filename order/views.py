from django.shortcuts import render,redirect
from basket.basket import Basket
from account.forms import Addressform
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