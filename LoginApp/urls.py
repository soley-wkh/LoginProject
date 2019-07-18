# -*- coding:utf-8 -*-
"""
    version: 
    author : wkh
    time   : 2019/7/18 15:34
    file   : urls.py
    
"""
from django.urls import path
from LoginApp.views import *

urlpatterns = [
    path('index/', index),
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('au/', ajax_user_valid),
    path('tf/', temp_filter),
]
