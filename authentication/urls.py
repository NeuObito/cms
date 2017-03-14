#-*- coding=utf-8 -*-
from django.conf.urls import url, include

from authentication.views import LoginView
from authentication.views import index

urlpatterns = [
	url(r'^$', LoginView.as_view(), name="index"),
	url(r'^cmsuser/$', LoginView.as_view(), name="user-login"),
]