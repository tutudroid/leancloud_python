# coding: utf-8

from django.conf.urls import url

from Order import views

urlpatterns = [
    url(r'^AllOrder/$', views.AllOrder, name='AllOrder'),
    url(r'^SearchOrder/$', views.SearchOrder, name='SearchOrder'),
    url(r'^Displace/$', views.displaceOrder, name='Displace'),
]