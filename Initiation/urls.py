# coding: utf-8

from django.conf.urls import url
from Initiation import Init_Product_Views, Init_Prepare_Views, Test_example

urlpatterns = [

    #
    url(r'^$', Init_Prepare_Views.Init_index, name='Init'),
    url(r'^Check/$', Init_Prepare_Views.Init_index, name='Check'),
    url(r'^Check_Product/$', Init_Prepare_Views.Init_index, name='Check_Product'),
    url( r'^InitLoadData/$', Init_Prepare_Views.Init_index, name='InitLoadData' ),

    url(r'^InitPrerequisite/$', Init_Prepare_Views.Init_index, name='InitPrerequisite'),
    url(r'^CreateAdmin/$', Init_Product_Views.CreateAdmin, name='CreateAdmin'),
    url(r'^ClearAllData/$', Init_Product_Views.ClearAllData, name='ClearAllData'),
    url(r'^InjectData/$', Init_Product_Views.Inject_Data, name='Inject_Data'),

    # 测试接口
    url(r'^CreateAll/$', Test_example.CreateAll, name='CreateAll'),
    url(r'^Order_AfterSale/$', Test_example.AfterSale_Order, name='Order_AfterSale'),
    url(r'^Category/$', Test_example.Category, name='Category'),
    url(r'^AllCategory/$', Test_example.AllCategory, name='AllCategory'),
    url(r'^AllProduct/$', Test_example.AllProduct, name='AllProduct'),
    url(r'^AllOrder/$', Test_example.AllOrder, name='AllOrder'),
    url(r'^AllAfterSale/$', Test_example.AllAfterSale, name='AllAfterSale'),
]