#-*- coding=utf-8 -*-
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls.resolvers import get_resolver

from .models import CmsUser
from .forms import LoginForm


def index(request):
	return render(request, "login.html")


class LoginView(FormView):
	template_name = "login.html"
	form_class = LoginForm
	success_url = get_resolver('success')

	def get_context_data(self, *args, **kwargs):
		"""
		可以传递一些额外的内容到页面。
		"""
		print("==============")
		context = super(LoginView, self).get_context_data(*args, **kwargs)
		context['active_page'] = 'login'
		print(context)

		return context

	def form_invalid(self, form):
		print("3333")

	def form_valid(self, form):
		print("2")
		user = form.login()

		if user:
			if user.is_active:
				login(self.request, user)
				return super(LoginView, self).form_valid()
			else:
				return self.response_error_page('你的账户未激活')
		else:
			return self.response_error_page('用户名或者密码错误')

	def response_error_page(self, msg):
		return render(self.request, 'error_page.html', {'message': msg})

	# def get(self, request):
	# 	print("44")

	# 	return None
