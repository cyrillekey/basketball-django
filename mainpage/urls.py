from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'mainpage'
urlpatterns=[
    path('',views.home,name="home"),
    
    path('single/<slug>/',views.singleproduct,name='single'),
    path('faq/',views.faq,name='faq'),
    path('allproduct/',views.allproducts,name='allproducts')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)