#-*- coding=utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.contrib.auth import authenticate
from django.utils.encoding import python_2_unicode_compatible


class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True)

	def login(self):
		user = authenticate(username=self.cleaned_data['username'], 
			password=self.cleaned_data['password']
		)

		return user
