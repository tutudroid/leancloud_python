# coding: utf-8
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

import views


urlpatterns = [
    #成功页面
    url(r'^$', views.index, name='#'),
    url(r'^success/$', views.successPage, name='success'),
    url(r'^NoFound/$', views.NoFound, name='NoFound'),
    url(r'^PrivatePolicy/$', views.PrivatePolicy, name='PrivatePolicy'),
    url(r'^$', views.mainPage, name=''),
    # 订单管理
    url(r'^Order/', include('Order.urls', namespace='Order')),
    # 店铺管理
    url(r'^Shop/', include('Shop.urls', namespace='Shop')),
    #用户管理，包括登陆、注册、忘记密码。
    url(r'^Account/', include('Account.urls', namespace='Account')),
    url(r'^Admin/', include('Admin.urls', namespace='Admin')),
    # 商品管理
    url(r'^Product/', include('Product.urls', namespace='Product')),
    # 首页推荐
    url(r'^Recommendation/', include('Recommendation.urls', namespace='Recommendation')),
    # 售后
    url(r'^AfterSale/', include('AfterSale.urls', namespace='AfterSale')),
    # 初始化
    url(r'^Initiation/', include('Initiation.urls', namespace='Initiation')),

    # 店家上传商品
    url(r'^TmpProductGroup/', include('TmpProductGroup.urls', namespace='TmpProductGroup')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
