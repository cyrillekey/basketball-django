from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'basket'
urlpatterns=[
    path('',views.basket_summary,name='basket_summary'),
    path('add/',views.basket_add,name='basket_add'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)