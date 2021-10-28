import requests
from decouple import config
from  django.core.mail import  send_mail
def sendsms(message):
    url='https://mysms.celcomafrica.com/api/services/sendsms/'
    message_data ={
        'partnerID':config('CELCOM_PARTNER_ID'),
        'apikey':config('CELCOM_API_KEY'),
        'mobile':'254708073370',
        'message':message,
        'shortcode':'CELCOM_SMS'
        ,'pass_type':'plain',
        }
    x=requests.post(url,data=message_data)
    print(x.text)
def send_email():
    send_mail('Hello Customer','Welcome to basketball','cyrilleotieno7@gmail.com',['cyrilleotieno83@gmail.com'])  

send_email()