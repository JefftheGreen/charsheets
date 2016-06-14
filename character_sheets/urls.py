"""character_sheets URL Configuration

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
from django.conf.urls import *
from django.contrib import admin
from main import views

urlpatterns = patterns('',
    url(r'^$', views.home_view, name='home'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^password_reset/$', views.PasswordResetView.as_view(),
        name='pwd_reset'),
    url(r'^register/$', views.NewUserView.as_view(), name='register'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^sheet/(?P<id>[0-9]+)/$', views.SheetView.as_view(), name='sheet')
)