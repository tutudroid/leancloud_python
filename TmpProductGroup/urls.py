# coding: utf-8

from django.conf.urls import url
from TmpProductGroup import productViews

urlpatterns = [

    # product Management
    # product manage
    url(r'^AllShopProductGroup/$', productViews.Shop_All_ShopProductGroup, name='AllShopProductGroup'),
    url(r'^AllProductGroup/$', productViews.Shop_All_ProductGroup, name='AllProductGroup'),
    url(r'^CreateProductGroup/$', productViews.createProductGroup, name='CreateProductGroup'),
    url(r'^EditProductGroup/$', productViews.editProductGroup, name='EditProductGroup'),
    url(r'^ProductGroupDetail/$', productViews.productGroupDetail, name='ProductGroupDetail'),
]