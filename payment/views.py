from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def mpesa_callback(request):
    result=request.body
    result=json.loads(result.decode("utf-8"))
    checkoutid=(result["Body"]["stkCallback"]["MerchantRequestID"])
    amount=(result["Body"]["stkCallback"]["CallbackMetadata"]["Item"][0]['Value'])
    reference=(result["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]['Value'])
    phonenumber=(result["Body"]["stkCallback"]["CallbackMetadata"]["Item"][4]['Value'])
    paymnet_method="mpesa"
    time=(result["Body"]["stkCallback"]["CallbackMetadata"]["Item"][3]['Value'])
    return HttpResponse(time)