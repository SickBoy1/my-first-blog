# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 17:18:57 2018

@author: a.terentev
"""

from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
]
