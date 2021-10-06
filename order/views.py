from django.shortcuts import render,redirect,HttpResponse
from basket.basket import Basket
from order.models import Order,OrderItem
from account.forms import Addressform
from django.http import JsonResponse
from account.models import shipping
from django.db import transaction
from payment import mpesa_payment
import random,string
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
@transaction.non_atomic_requests
def add(request):
    basket=Basket(request)
    user_id=request.user.id
    baskettotal=basket.get_total_price()     
    
    if 'mpesa' in request.POST:
        form=Addressform(request.POST)
        if form.is_valid():
            mpesa=mpesa_payment.mpesa()
            order_key=mpesa.simulate_customer_to_account(254708073370,10)
            print(order_key)
            fullname=form.cleaned_data['fullnames']
            county=form.cleaned_data['county']
            city=form.cleaned_data['city']
            area=form.cleaned_data['area']
            email=form.cleaned_data['email']
            phone=form.cleaned_data['phone_number']
            try:
                address=shipping.objects.create(fullnames=fullname,county=county,city=city,area=area,email=email,phone_number=phone,user=request.user)
                #order section
                order=Order.objects.create(user=request.user,total_paid=float(basket.get_total_price()),order_key=order_key,order_status="created",payment_status=False,voucher_code=False)
                #order_id=order.pk
                for item in basket:
                    OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['qty'])
                response=JsonResponse({'success':'Order Created'})  
                return HttpResponse("Order created succesfully")
            except:
                return HttpResponse("Order Not created")    
        else:
            redirect("checkout")
    elif 'delivery' in request.POST:
        #will handle the user pay on delivery
        order_key=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            form=Addressform(request.POST)
            if form.is_valid():
                fullname=form.cleaned_data['fullnames']
                county=form.cleaned_data['county']
                city=form.cleaned_data['city']
                area=form.cleaned_data['area']
                email=form.cleaned_data['email']
                phone=form.cleaned_data['phone_number']
                try:
                    address=shipping.objects.create(fullnames=fullname,county=county,city=city,area=area,email=email,phone_number=phone,user=request.user)
                    #order section
                    order=Order.objects.create(user=request.user,total_paid=float(basket.get_total_price()),order_key=order_key,order_status="created",payment_status=False,voucher_code=False)
                    #order_id=order.pk
                    for item in basket:
                        OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['qty'])
                    response=JsonResponse({'success':'Order Created'})  
                    return HttpResponse("Order created succesfully")
                except:
                    return HttpResponse("An error occured")
            else:
                return HttpResponse("Form is invalid")    
    else:
        pass   