# coding: utf-8

from django.conf.urls import url

from Admin import views

urlpatterns = [
    # app用户相关
    url(r'^AppUser/$', views.AppUser, name='AppUser'),

    # 等待审计店铺
    url(r'^ShopUser/$', views.ShopUser, name='ShopUser'),
    url(r'^AuditShopUser/$', views.audit_shop, name='AuditShopUser'),

    # 系统用户相关
    url(r'^AddUser/$', views.AddUser, name='AddUser'),
    url(r'^SysUser/$', views.sysUser, name='SysUser'),
    url(r'^SysUserManager/$', views.SysUserManager, name='SysUserManager'),

    # 重置密码
    url(r'^ResetUserPassword/$', views.ResetUserPassword, name="ResetUserPassword"),

    # 客户端网页配置
    url(r'^WebPageConfigure/$', views.WebPage, name='WebPageConfigure'),
]
