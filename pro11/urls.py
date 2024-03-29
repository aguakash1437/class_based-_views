"""pro11 URL Configuration

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
from django.urls import path,re_path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Schoollist/',Schoollist.as_view(),name='Schoollist'),
    path('SchoolCreate/',SchoolCreate.as_view(),name='SchoolCreate'),

    re_path('^SchoolUpdate(?P<pk>\d+)/',SchoolUpdate.as_view(),name='SchoolUpdate'),
    re_path('^SchoolDelete(?P<pk>\d+)/',SchoolDelete.as_view(),name='SchoolDelete'),
    re_path('(?P<pk>\d+)/',SchoolDetail.as_view(),name='detail'),


]
