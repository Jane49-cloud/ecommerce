from django.contrib import admin
from django.urls import path

from . import views
from django.urls import include, re_path

urlpatterns = [
    # path('', views.index),
    re_path(r'^$', views.index, name='home'),
    

]
