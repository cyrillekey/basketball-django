from decouple import config
import requests
import json
response=requests.get(
    "https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id="+config('FACEBOOK_APP_ID')+"&client_secret="+config('FACEBOOK_APP_SECRET')+"&fb_exchange_token=EAADAKrb7sm0BAHni0z1bOnaHds2xgPKho0ypuiYk7MoIU6gQ2TJYQEiqve7EyVhNtslYAACW1HoZBWX1HTcZCoTjC6VMsK926EoXTGGGucTHtLBQIRT6i0KSIesYNV5pNUOSOUAn7TKoDv3dRmjC4pkO6MmJzgmmJILRtPfDOgL3RDesMyZC5SeT2Ycm7sZAv5lL666FfAZDZD"
        )
response=json.loads(response.text)
access=response['access_token']

#response=requests.post("https://graph.facebook.com/"+config("PAGE_ID")+"/feed?message=Hello World!&access_token="+access)
response=requests.post("https://graph.facebook.com/"+config("PAGE_ID")+"/photos?url=https://st2.depositphotos.com/thumbs/1007959/image/5441/54416831/api_thumb_450.jpg&access_token="+access)
print(response.text)