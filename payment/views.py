from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from order.models import Order
from payment.models import Paymentinfo
from django.db import transaction
# Create your views here.
@csrf_exempt
@transaction.non_atomic_requests
def mpesa_callback(request):

    result=request.body
    result=json.loads(result.decode("utf-8"))
    desc=str(result["Body"]["stkCallback"]["ResultCode"])
    if desc!="0":
        key=str(result["Body"]["stkCallback"]["MerchantRequestID"])
        Order.objects.filter(order_key=key).delete()
        return HttpResponse("Tranaction was cancelled")
    else:    
        checkoutid=str(result["Body"]["stkCallback"]["MerchantRequestID"])
        amount=int(result["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]['Value'])
        reference=str(result["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]['Value'])
        phonenumber=str(result["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]['Value'])
        paymnet_method="mpesa"
        time=str(result["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]['Value'])
        order=Order.objects.get(order_key=checkoutid)
        order.payment_status=True
        order.order_status="Waiting Shipping"
        order.save()
        payment=Paymentinfo.objects.create(payment_reference_id=checkoutid,payment_platform="mpesa",payment_amount=amount,payment_status=True,order_id=order)
        return HttpResponse(time)