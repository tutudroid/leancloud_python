# coding: utf-8

from django.conf.urls import url
from Shop import views, settleInViews,directShopViews

urlpatterns = [
    url(r'^Login/$', views.login, name='Login'),
    url(r'^Register/$', views.register, name='Register'),
    url(r'^changePhoneNumber/$', views.changePhoneNumber, name='changePhoneNumber'),
    url(r'^modifyPassword/$', views.modifyPassword_Username, name='modifyPassword'),

    url(r'^ShopDetail/$', views.ShopDetail, name='ShopDetail'),
    url(r'^EditShopDetail/$', views.EditShopDetail, name='EditShopDetail'),
    url(r'^ShopAfterSale/$', views.shopAfterSale, name='ShopAfterSale'),

    # 所有品牌
    url(r'^AllBrand/$', views.AllBrand, name='AllBrand'),
    url(r'^EditBrand/$', views.EditBrand, name='EditBrand'),
    # 所有运费模版
    url(r'^AllFreightModel/$', views.AllFreight, name='AllFreightModel'),
    url(r'^EditFreightModel/$', views.EditFreight, name='EditFreightModel'),

    # 所有活动
    url(r'^AllActivities/$', views.AllActivities, name='AllActivities'),
    url(r'^EditActivities/$', views.EditActivities, name='EditActivities'),

    url(r'^AllForbiddenShop/$', views.AllForbiddenShop, name='AllForbiddenShop'),

    url(r'^CreateSettleIn/$', settleInViews.CreateSettleIn, name='CreateSettleIn'),
    url(r'^ReviewSettleIn/$', settleInViews.ReviewSettleIn, name='ReviewSettleIn'),
    url(r'^AllSettleIn/$', settleInViews.AllSettleIn, name='AllSettleIn'),
    url(r'^SettleModifyPhoneNumber/$', settleInViews.SettleModifyPhoneNumber, name='SettleModifyPhoneNumber'),

    # 自营店铺
    url(r'^DirectShop/$', directShopViews.DirectShop, name='DirectShop'),
    url(r'^InitiateDirectShop/$', directShopViews.InitiateDirectShop, name='InitiateDirectShop'),
    url(r'^EditDirectShop/$', directShopViews.EditDirectShop, name='EditDirectShop'),


    url(r'^(?P<shopObjectId>[0-9a-z]+)/brand/$', views.brand.as_view(), name='brand'),
    url(r'^(?P<shopObjectId>[0-9a-z]+)/brand/(?P<objectId>[0-9a-z]+)$', views.brandDetail.as_view(), name='brand'),
    url(r'^/shop/$', views.shop.as_view(), name='shop'),
    url(r'^/shopDetail/(?P<shopObjectId>[0-9a-z]+)/$', views.shopDetail.as_view(), name='shopDetail'),
    url(r'^SettleInDetail/$', settleInViews.SettleInDetail.as_view(), name='SettleInDetail'),
    url(r'^SettleIn/$', settleInViews.SettleIn.as_view(), name='SettleIn'),


]
