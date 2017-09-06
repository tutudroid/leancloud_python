# coding: utf-8

from django.conf.urls import url
from Shop import views, settleInViews

urlpatterns = [
    url(r'^Login/$', views.login, name='Login'),
    url(r'^Register/$', views.register, name='Register'),
    url(r'^changePhoneNumber/$', views.changePhoneNumber, name='changePhoneNumber'),
    url(r'^modifyPassword/$', views.modifyPassword_Username, name='modifyPassword'),

    url(r'^ShopDetail/$', views.ShopDetail, name='ShopDetail'),
    url(r'^EditShopDetail/$', views.EditShopDetail, name='EditShopDetail'),
    url(r'^ShopAfterSale/$', views.shopAfterSale, name='ShopAfterSale'),

    url(r'^AllForbiddenShop/$', views.AllForbiddenShop, name='AllForbiddenShop'),

    url(r'^CreateSettleIn/$', settleInViews.CreateSettleIn, name='CreateSettleIn'),
    url(r'^ReviewSettleIn/$', settleInViews.ReviewSettleIn, name='ReviewSettleIn'),
    url(r'^AllSettleIn/$', settleInViews.AllSettleIn, name='AllSettleIn')
]
