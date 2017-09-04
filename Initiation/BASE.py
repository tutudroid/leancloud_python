# -*- coding: UTF-8 -*-

import json
from Initiation.header import *


def load(filename):
    with open(filename) as json_file:
        data1 = json.load(json_file, strict=False)
        data1 = json.dumps(data1, ensure_ascii=False, indent=4)
        data1 = json.loads(data1)
        return data1

CLASS_NAME_IP = 'IPTable'
attribute_uniqueId = 'uniqueId'
attribute_name = 'name'
attribute_image = 'imageFile'
attribute_briefDescription = 'briefDescription'

CLASS_NAME_BRAND = 'BrandTable'


CLASS_NAME_PRODUCT_SERVICE = 'ProductService'


def create_IP(data):
    if data:
        find = get_IP(data[attribute_uniqueId])
        if find:
            return False

        Instance = leancloud.Object.extend(CLASS_NAME_IP)
        ip = Instance()
        ip.set(attribute_name, data[attribute_name])
        ip.set(attribute_uniqueId, data[attribute_uniqueId])
        ip.set(attribute_briefDescription, data[attribute_briefDescription])
        base.save_data(ip)
        base.local_image(ip, data[attribute_image], attribute_image)


def create_brand(data):
    if data:

        find = get_Brand(data[attribute_uniqueId])
        if find:
            return False

        Instance = leancloud.Object.extend( CLASS_NAME_BRAND )
        brand = Instance()
        brand.set(attribute_name, data[attribute_name])
        brand.set(attribute_uniqueId, data[attribute_uniqueId])
        brand.set(attribute_briefDescription, data[attribute_briefDescription])
        base.save_data(brand)
        base.local_image(brand, data[attribute_image], attribute_image)


def create_product_service(data):
    if data:
        Instance = leancloud.Object.extend(CLASS_NAME_PRODUCT_SERVICE)
        find = get_ProductService(data[attribute_uniqueId])
        if find:
            return False
        productService = Instance()
        productService.set(attribute_name, data[attribute_name])
        productService.set(attribute_uniqueId, data[attribute_uniqueId])
        productService.set(attribute_briefDescription, data[attribute_briefDescription])
        base.save_data(productService)



def get_IP(uniqueId):
    if uniqueId is not None:
        ip = base.queryInstanceAttributeFirst(CLASS_NAME_IP, attribute_uniqueId, uniqueId)
        return ip
    return None


def get_Brand(uniqueId):
    if uniqueId is not None:
        brand = base.queryInstanceAttributeFirst(CLASS_NAME_BRAND, attribute_uniqueId, uniqueId)
        return brand
    return None


def get_ProductService(uniqueId):
    if uniqueId is not None:
        productService = base.queryInstanceAttributeFirst(CLASS_NAME_PRODUCT_SERVICE, attribute_uniqueId, uniqueId)
        return productService
    return None


def get_attribute_name(instance):
    if instance:
        return instance.get(attribute_name)
    return None
