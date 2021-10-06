from decouple import config
import requests
import json
#response=requests.get(
#    "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id="+config('FACEBOOK_APP_ID')+"&client_secret="+config('FACEBOOK_APP_SECRET')+"&fb_exchange_token=EAADAKrb7sm0BALWuskBZBy19F914NvaO9tJBSazkt1hkbnMMRQEaAIHG2wZBQ9VXn8IVAOSdZCGSpukZCQb9aWNpdH6ReS3fonrXqXidgZCEy7IgtrZCvuHfUryRwTdtlRx16DRZAQX3JGJH5BBSIc66o1viZAEbdYZCvEyGgCTqFrln3ZAg17YsW5tCmuigWGDNArYM5HtAMtBgZDZD"
 #       )
#response=json.loads(response.text)
#access=response['access_token']

#response=requests.post("https://graph.facebook.com/"+config("PAGE_ID")+"/feed?message=Hello World!&access_token="+config("FACEBOOK_ACCESS_TOKEN"))

response=requests.post("https://graph.facebook.com/"+config("PAGE_ID")+"/photos?url=https://st2.depositphotos.com/thumbs/1007959/image/5441/54416831/api_thumb_450.jpg&access_token="+access)
#response=requests.get("https://graph.facebook.com/v3.2/me?access_token="+access)
response=json.loads(response.text)
#id_=response['id']
print(response)

#response=requests.get("https://graph.facebook.com/v3.2/"+id_+"/accounts?access_token="+access)
#response=json.loads(response.text)
#print(response['data'][0]['access_token'])