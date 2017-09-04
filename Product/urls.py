# coding: utf-8

from django.conf.urls import url
from Product import productViews, categoryViews

urlpatterns = [

    # product Management
    # product manage
    url(r'^ShopProductGroup/$', productViews.shop_ProductGroup, name='ShopProductGroup'),
    url(r'^CreateProductGroup/$', productViews.createProductGroup, name='CreateProductGroup'),
    url(r'^ProductGroupDetail/$', productViews.productGroupDetail, name='ProductGroupDetail'),
    url(r'^EditProductGroup/$', productViews.editProductGroup, name='EditProductGroup'),
    url(r'^SearchProductGroup/$', productViews.SearchProductGroup, name='SearchProductGroup'),
    url(r'^ProductGroupBriefDetail/$', productViews.ProductGroupBriefDetail, name='ProductGroupBriefDetail'),
    url(r'^DisposeProductGroup/$', productViews.DisposeProductGroup, name='DisposeProductGroup'),
    url(r'^AuditProductGroup/$', productViews.AuditProductGroup, name='AuditProductGroup'),



    url(r'^CreateStoreCategory/$', categoryViews.createStoreCategory, name='CreateStoreCategory'),
    url(r'^ShowStoreCategory/$', categoryViews.ShowStoreCategory, name='ShowStoreCategory'),
    url(r'^EditStoreCategory/$', categoryViews.EditStoreCategory, name='EditStoreCategory'),

    url(r'^ShowSaleCategory/$', categoryViews.ShowSaleCategory, name='ShowSaleCategory'),
    url(r'^CreateSaleCategory/$', categoryViews.createSaleCategory, name='CreateSaleCategory'),
    url(r'^EditSaleCategory/$', categoryViews.EditSaleCategory, name='EditSaleCategory'),

    # 销售分类排序
    url(r'^sortSaleCategorySecond/$', categoryViews.sortSaleCategorySecond, name='sortSaleCategorySecond'),
    url(r'^sortSaleCategoryFirst/$', categoryViews.sortSaleCategoryFirst, name='sortSaleCategoryFirst'),

    url(r'^ShowComments/$', productViews.ShowComments, name='ShowComments'),
    url(r'^SaleCategoryRecommend/$', categoryViews.SaleCategoryRecommend, name='SaleCategoryRecommend'),
    url(r'^DelSaleCategoryRecommend/$', categoryViews.DelSaleCategoryRecommend, name='DelSaleCategoryRecommend'),
]
