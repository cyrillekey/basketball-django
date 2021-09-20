import requests
import base64
from decouple import config
import json
from datetime import datetime
class mpesa():
    def __init__(self):
        self.userpassword=config('MPESA_CONSUMER_KEY')+':'+config('MPESA_CONSUMER_SECRET_KEY')
        self.secretkey=self.userpassword.encode("ascii")
        self.secretkey=base64.b64encode(self.secretkey).decode("utf-8")
    def get_token(self):

        url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

        payload={}
        headers = {
        'Authorization': 'Basic %s' % self.secretkey
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response_json=json.loads(response.text)
        return ((response_json['access_token']))

    def simulate_customer_to_account(self):
        
        timestamp=datetime.now()   
        
        password=base64.b64encode((config("MPESA_SHORTCODE")+config('MPESA_PASSKEY')+(timestamp.strftime("%Y%m%d%H%M%S"))).encode('utf-8')).decode()
        headers = {
        'Authorization': 'Bearer '+self.get_token()
        }

        payload = {
            "BusinessShortCode": config('MPESA_SHORTCODE'),
            "Password": password,
            "Timestamp": datetime.now().strftime("%Y%m%d%H%M%S"),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": 1,
            "PartyA": 254708374149,
            "PartyB": 174379,
            "PhoneNumber": 254708073370,
            "CallBackURL": "https://mydomain.com/path",
            "AccountReference": "CompanyXLTD",
            "TransactionDesc": "Payment of X" 
        }

        response = requests.post('https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, json = payload)
        response=json.loads(response.text)
        print(response)
        
        


mango=mpesa()
#print(mango.get_token())
print(mango.simulate_customer_to_account())


