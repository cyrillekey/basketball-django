from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import checkout,add,track
app_name="order"

urlpatterns=[
    path("",checkout,name="checkout"),
    path("add/",add,name="add"),
    path("success/",add,name="success"),
    path("track/",track,name="track"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)