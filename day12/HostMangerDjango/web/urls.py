"""HostMangerDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from web import views
urlpatterns = [
    url(r'^$', views.Login),
    url(r'^login.html/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^register.html', views.Register),
    url(r'^index.html', views.Index),
    url(r'^host_list.html/(\d*)', views.Host_list),
    url(r'^host_add.html', views.host_add),
    url(r'^host_del.html', views.host_del),
    url(r'^host_mod.html', views.host_mod),
    url(r'^type_add.html', views.type_add),
    url(r'^type_del.html', views.type_del),
    url(r'^type_mod.html', views.type_mod),
    url(r'^type_get.html', views.type_get),
    url(r'^user_add.html', views.user_add),
    url(r'^user_del.html', views.user_del),
    url(r'^user_get.html', views.user_get),
    url(r'^user_mod.html', views.user_mod),
    url(r'^group_add.html', views.group_add),
    url(r'^group_get.html', views.group_get),
    url(r'^group_del.html', views.group_del),
    url(r'^group_mod.html', views.group_mod), 
]
