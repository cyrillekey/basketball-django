from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainpage import views
app_name = 'mainpage'
urlpatterns=[
    path('single/<slug>/',views.singleproduct,name='single')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)