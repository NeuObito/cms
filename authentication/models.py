#-*- coding=utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class CmsUser(AbstractUser):
	AGE_CHOICES = (
		('MALE', "男"),
		('FEMALE', "女")
	)
	password = models.CharField(_('密码'), blank=False, null=False, max_length=16, default="")
	phone = models.IntegerField(_('手机号'), blank=True, unique=True)
	age = models.CharField(_('性别'), max_length=2, blank=True, choices=AGE_CHOICES)
	portrait = models.ImageField(_('用户头像路径'), upload_to='./user/portrait/%Y/%m/%d')
	presentation = models.CharField(_('一句话介绍自己'), max_length=100)

	def __str__(self):
		return self.username

	class Meta:
		db_table = 'cmsuser'
