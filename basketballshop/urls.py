from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from mainpage import views as homepageviews
from account import views as accountview
urlpatterns = [
    path('',homepageviews.home,name="home"),
    path('admin/', admin.site.urls),
    path('login/',accountview.login_view,name='login'),
    path('signup/',accountview.signup_view,name='signup'),
    path('basket/',include('basket.urls',namespace='basket')),
    path('mainpage/',include('mainpage.urls'),name='mainpage'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
