# coding: utf-8

from django.conf.urls import url

from AfterSale import views

urlpatterns = [
    url(r'^AfterSale/$', views.afterSale, name='AfterSale'),
    url(r'^DisposeAfterSale/$', views.disposeAfterSale, name='DisposeAfterSale'),
    url(r'^disposeRefund/$', views.disposeRefund, name='disposeRefund'),
    url(r'^CancelDisplacedRefund/$', views.CancelDisplacedRefund, name='CancelDisplacedRefund')
]
