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
    url(r'^AllFreight/$', views.AllFreight, name='AllFreight'),
    url(r'^EditFreight/$', views.EditFreight, name='EditFreight'),

    url(r'^AllForbiddenShop/$', views.AllForbiddenShop, name='AllForbiddenShop'),

    url(r'^CreateSettleIn/$', settleInViews.CreateSettleIn, name='CreateSettleIn'),
    url(r'^ReviewSettleIn/$', settleInViews.ReviewSettleIn, name='ReviewSettleIn'),
    url(r'^AllSettleIn/$', settleInViews.AllSettleIn, name='AllSettleIn'),
    url(r'^SettleModifyPhoneNumber/$', settleInViews.SettleModifyPhoneNumber, name='SettleModifyPhoneNumber'),

    # 自营店铺
    url(r'^DirectShop/$', directShopViews.DirectShop, name='DirectShop'),
    url(r'^InitiateDirectShop/$', directShopViews.InitiateDirectShop, name='InitiateDirectShop'),
    url(r'^EditDirectShop/$', directShopViews.EditDirectShop, name='EditDirectShop'),

]
