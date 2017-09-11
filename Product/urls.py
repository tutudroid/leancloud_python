# coding: utf-8

from django.conf.urls import url
from Product import productViews, categoryViews
from Product import shopProductViews, productOtherViews

urlpatterns = [

    # product Management
    # product manage
    url(r'^ProductGroupDetail/$', productViews.ProductGroupDetail, name='ProductGroupDetail'),

    url(r'^AuditProductGroup/$', productViews.AuditProductGroup, name='AuditProductGroup'),
    url(r'^ShopAllProductGroup/$', productViews.ShopAllProductGroup, name='ShopAllProductGroup'),
    url(r'^ShopAllShopProductGroup/$', productViews.ShopAllShopProductGroup, name='ShopAllShopProductGroup'),

    url(r'^CreateProductGroup/$', productViews.CreateProductGroup, name='CreateProductGroup'),
    url(r'^EditProductGroup/$', productViews.EditProductGroup, name='EditProductGroup'),
    url(r'^SearchProductGroup/$', productViews.SearchProductGroup, name='SearchProductGroup'),
    url(r'^ProductGroupBriefDetail/$', productViews.ProductGroupBriefDetail, name='ProductGroupBriefDetail'),
    url(r'^DisposeProductGroup/$', productViews.DisposeProductGroup, name='DisposeProductGroup'),

    # 店铺创建，修改，显示未审核商品
    url(r'^CreateShopProductGroup/$', shopProductViews.CreateShopProductGroup, name='CreateShopProductGroup'),
    url(r'^EditShopProductGroup/$', shopProductViews.EditShopProductGroup, name='EditShopProductGroup'),
    url(r'^ShopProductGroupDetail/$', shopProductViews.ShopProductGroupDetail, name='ShopProductGroupDetail'),

    url(r'^ShowComments/$', productViews.ShowComments, name='ShowComments'),

    url(r'^CreateStoreCategory/$', categoryViews.createStoreCategory, name='CreateStoreCategory'),
    url(r'^ShowStoreCategory/$', categoryViews.ShowStoreCategory, name='ShowStoreCategory'),
    url(r'^DelStoreCategory/$', categoryViews.DelStoreCategory, name='DelStoreCategory'),
    url(r'^SearchStoreCategory/$', categoryViews.SearchStoreCategory, name='SearchStoreCategory'),

    url(r'^ShowSaleCategory/$', categoryViews.ShowSaleCategory, name='ShowSaleCategory'),
    url(r'^CreateSaleCategory/$', categoryViews.createSaleCategory, name='CreateSaleCategory'),
    url(r'^DelSaleCategory/$', categoryViews.DelSaleCategory, name='DelSaleCategory'),
    url(r'^SearchSaleCategory/$', categoryViews.SearchSaleCategory, name='SearchSaleCategory' ),
    # 销售分类排序
    url(r'^sortSaleCategorySecond/$', categoryViews.sortSaleCategorySecond, name='sortSaleCategorySecond'),
    url(r'^sortSaleCategoryFirst/$', categoryViews.sortSaleCategoryFirst, name='sortSaleCategoryFirst'),

    url(r'^SaleCategoryRecommend/$', categoryViews.SaleCategoryRecommend, name='SaleCategoryRecommend'),
    url(r'^DelSaleCategoryRecommend/$', categoryViews.DelSaleCategoryRecommend, name='DelSaleCategoryRecommend'),

    # 商品服务
    url(r'^AllProductService/$', productOtherViews.AllProductService, name='AllProductService'),
    url(r'^EditProductService/$', productOtherViews.EditProductService, name='EditProductService'),
]
