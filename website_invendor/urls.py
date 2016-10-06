"""website_invendor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from . import settings
from index import views
from alpha import views as v
from coords import views as coordviews

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^subscribe/$',views.subscribe),
    url(r'^query/$',views.query),
    url(r'^404/$',views.four),
    url(r'^status/$',v.status),
    url(r'^set_switch_status/$',v.set_status),
    url(r'^reg/', coordviews.reg_request),
    url(r'^auth/', coordviews.auth),
    url(r'^requests/', coordviews.get_requests),
    url(r'^set/', coordviews.set_status),
]
