"""ders1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myApp.views import *
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('detail/<id>', detail, name='detail'),
    path('about/', about, name='about'),
    path('sepet/', sepet, name='sepet'),
    path('deleteSepet/<id>/', deleteSepet, name='deletesepet'),
    # USER
    path('login/', userLogin, name='userLogin'),
    path('logout/', userLogout, name='userLogout'),
    path('register/', userRegister, name='userRegister'),
    path('profile/', profile, name='profile'),
    path('changepassword/', userChangePassword, name='changepassword'),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
