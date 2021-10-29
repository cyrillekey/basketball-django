from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from account import views as accountview
from payment.views import mpesa_callback
from dashboard.views import dashboard
urlpatterns = [
   
    path('admin/', admin.site.urls),

    path('login/',accountview.login_view,name='login'),
    path("account/",accountview.account,name="account"),
    path('logout/',accountview.logout_view,name='logout'),
    path('signup/',accountview.signup_view,name='signup'),
    path('basket/',include('basket.urls',namespace='basket')),
    path("",include('mainpage.urls',namespace='mainpage')),
    path("checkout/",include("order.urls",namespace="order")),
    path("mpesacall/",mpesa_callback,name="mpesa"),
    path("dashboard/",dashboard)
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
