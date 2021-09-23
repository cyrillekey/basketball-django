from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from account import views as accountview
urlpatterns = [
   
    path('admin/', admin.site.urls),

    path('login/',accountview.login_view,name='login'),
    path("account/",accountview.account,name="account"),
    path('logout/',accountview.logout_view,name='logout'),
    path('signup/',accountview.signup_view,name='signup'),
    path('basket/',include('basket.urls',namespace='basket')),
    path("",include('mainpage.urls',namespace='mainpage')),

   
    
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
