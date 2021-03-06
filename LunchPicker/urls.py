"""LunchPicker URL Configuration

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
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
import picker.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', picker.views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'auth/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'auth/logout.html'}, name='logout'),
    url(r'^reset/confirm/(?P<user>[0-9A-Za-z]+)-(?P<token>.+)/$',picker.views.reset_confirm, name='password_reset_confirm'),
    url(r'^reset/$', picker.views.reset, name='reset'),
    url(r'^$', picker.views.main, name='main'),
    url(r'^vote/$', picker.views.vote, name='vote'),
    url(r'^veto/$', picker.views.veto, name='veto'),
]
