# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='static_generation_admin_index'),
    url(r'^generate/$', views.generate, name='generate')
]
