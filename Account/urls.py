# coding: utf-8

from django.conf.urls import url

from Account import views

urlpatterns = [
    url(r'^$', views.login),
    url(r'^Profile/$', views.profile, name='Profile'),
    url(r'^Login/$', views.login, name='Login'),
    url(r'^Logout/$', views.logout, name='Logout'),
    url(r'^ResetPassword/$', views.resetPassword, name='ResetPassword'),
    url(r'^GetVerifyCode/$', views.getVerifyCode, name='GetVerifyCode'),
    url(r'^GetVerifyCode_Register/$', views.getVerifyCode_Register, name='GetVerifyCode_Register'),
    url(r'^GetVerifyCode_PhoneNumber/$', views.getVerifyCode_PhoneNumber, name='GetVerifyCode_PhoneNumber'),
]
