from django.conf import settings
from decouple import config
from django.shortcuts import redirect
from urllib.parse import urlencode
import requests,json,datetime
from humanfriendly import format_timespan
from django.http import JsonResponse

def directions(*args,**kwargs):
    lat_a=kwargs.get("lat_a")
    long_a=kwargs.get("long_a")
    lat_b=kwargs.get("lat_b")
    long_b=kwargs.get("long_b")
    lat_c=kwargs.get("lat_c")
    long_c=kwargs.get("long_c")
    lat_d=kwargs.get("lat_d")
    long_d=kwargs.get("long_d")

    origin=f'{lat_a},{long_a}'
    destination=f'{lat_b},{long_b}'
    result=requests.get("https://maps.googleapis.com/maps/api/directions/json?",params={'origin':origin,'destination':destination,"key":config("GOOGLE_API_KEY")})
    directions=result.json()
    if directions["status"]=="OK":
        routes=directions["routes"][0]["legs"]
        distance=0
        duration=0
        routes_list=[]
    return {
        "origin":origin,
        "destination":destination,
        "distance":f"{round(distance/1000,2)} Km",
        "duration":format_timespan(duration),
        "route":routes_list
    }    
