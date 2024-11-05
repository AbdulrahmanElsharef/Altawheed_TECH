"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Technical.views import *
from DELVERY.views import car_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('print/', print,name='print'),
    path('print/invoice/<int:id>/', invoice,name='invoice'),
    path('print/credit_note/<int:id>/', credit_note,name='credit_note'),
    path('print/replacement/<int:id>/', replacement,name='replacement'),
    path('report/', report,name='report'),
    path('report/<int:id>/', technical,name='technical'),
    path('cars/', car_list,name='car_list'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
