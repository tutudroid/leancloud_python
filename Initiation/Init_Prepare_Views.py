# -*- coding: UTF-8 -*-
from Error_Page import *
import os

BaseAddress = "/Users/kang/Desktop/"

SecondAddress = BaseAddress + "repertory"

Store_File = SecondAddress + "/JSON/库存分类.json"
Sale_File = SecondAddress + "/JSON/销售分类.json"
JSONFile_ProductService = SecondAddress + "/JSON/商品服务.json"
JSONFile_IPTable = SecondAddress + "/JSON/IP.json"
JSONFile_BandTable = SecondAddress + "/JSON/品牌.json"
JSONFile_Product = SecondAddress + "/JSON/商品.json"
JSONFile_ProductDir = SecondAddress + "/商品/"


JSONFile_ProductGroup = BaseAddress + "repertory/JSON/.json"



def error_message(name, address):
    if not os.path.exists(BaseAddress + address):
        A = {
            'name': name,
            'message': ['找不到' + BaseAddress + address],
            'error': True,
        }
        return A



def Init_index(request):
    return render(request, 'Init_index.html')
