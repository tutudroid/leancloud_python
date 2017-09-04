import re

import leancloud
from Product.library.base import sys_log, get_relation_data, queryInstanceThroughId, \
    set_image, save_data, queryInstanceThroughName
from Product.library import base

# 类名
CLASS_STORE_CATEGORY_FIRST = 'StoreCategoryFirst'
CLASS_STORE_CATEGORY_SECOND = 'StoreCategorySecond'
CLASS_STORE_CATEGORY_THIRD = 'StoreCategoryThird'
CLASS_CATEGORY_IMAGE = 'CategoryImage'

CLASS_SALE_CATEGORY_FIRST = 'SaleCategoryFirst'
CLASS_SALE_CATEGORY_SECOND = 'SaleCategorySecond'
CLASS_PRODUCT_GROUP = 'ProductGroup'

# 删除状态
DELETE_STATE = 2


def getSaleCategory():
    """
    获得销售分类表
    :return: 
    """
    saleCategoryFirst = base.queryInstanceAttribute_and_sort_uniqueId(CLASS_SALE_CATEGORY_FIRST, 'state', 0)
    if saleCategoryFirst:
        saleCategoryList = [
            {
                'objectId': first.get('objectId'),
                'name': first.get('name'),
                'value': [
                    {
                        'objectId': second.get('objectId'),
                        'name': second.get('name'),
                    } for second in base.get_relation_data_and_attribute_and_sort_uniqueId(first.get('objectId'), CLASS_SALE_CATEGORY_FIRST, 'saleCategorySecond', 'state', 0)
                ],
            } for first in saleCategoryFirst if first.get('categoryType') == 0
        ]
        return saleCategoryList
    return None


def getSaleCategory_All():
    """
    获得销售分类表
    :return: 
    """
    saleCategoryFirst = base.queryInstanceAttribute_and_sort_uniqueId(CLASS_SALE_CATEGORY_FIRST, 'state', 0)
    if saleCategoryFirst:
        saleCategoryList = [
            {
                'objectId': first.get('objectId'),
                'name': first.get('name'),
                'briefDescription': first.get('briefDescription'),
                'mainImage': first.get('mainImage'),
                'value': [
                    {
                        'objectId': second.get('objectId'),
                        'name': second.get('name'),
                        'briefDescription': second.get('briefDescription'),
                        'mainImage': second.get('mainImage'),
                    } for second in base.get_relation_data_and_attribute_and_sort_uniqueId(first.get('objectId'), CLASS_SALE_CATEGORY_FIRST, 'saleCategorySecond', 'state', 0)
                ],
            } for first in saleCategoryFirst
        ]
        return saleCategoryList
    return None


def saveSaleCategory(saleCategoryList):
    """
    创建销售分类表
    :param saleCategoryList: 
    :return: 
    """
    SaleCategoryFirst = leancloud.Object.extend(CLASS_SALE_CATEGORY_FIRST)

    for first in saleCategoryList:
        result = queryInstanceThroughName(CLASS_SALE_CATEGORY_FIRST, 'name', first['name'])
        if result is None:
            # 该元素不存在
            saleCategoryFirst = SaleCategoryFirst()
            saleCategoryFirst.set('name', first['name'])
            saleCategoryFirst.set('briefDescription', first['briefDescription'])
            set_image(saleCategoryFirst, first['firstLevelImage'], 'mainImage')
            saleCategoryFirst.set('state', 0)
            if save_data(saleCategoryFirst):
                # 第一级数据保存成功，保存第二级的数据
                sys_log('save success')
            else:
                sys_log('save fail')
        else:
            sys_log('该元素存在')


def saveSecondSaleCategory(categoryList):
    """
    保存增加的第二级销售分类数据
    :param categoryList: 
    :return: 
    """
    SaleCategorySecond = leancloud.Object.extend(CLASS_SALE_CATEGORY_SECOND)
    CategoryImage = leancloud.Object.extend(CLASS_CATEGORY_IMAGE)

    for first in categoryList:
        # 获得第一级和第二级的关联表
        saleCategoryFirst = queryInstanceThroughId(CLASS_SALE_CATEGORY_FIRST, first['objectId'])
        relation = saleCategoryFirst.relation('saleCategorySecond')

        # 保存第二级的数据
        for second in first['value']:
            if second['name'] and 0 < len(second['briefDescription']) < 40 and second['secondLevelImage']:
                result = queryInstanceThroughName(CLASS_SALE_CATEGORY_SECOND, 'name', second['name'])
                if result is None:
                    # 该元素不存在
                    saleCategorySecond = SaleCategorySecond()
                    saleCategorySecond.set('name', second['name'])
                    saleCategorySecond.set('briefDescription', second['briefDescription'])
                    set_image(saleCategorySecond, second['secondLevelImage'], 'mainImage')
                    saleCategorySecond.set('saleCategoryFirst', saleCategoryFirst)
                    saleCategorySecond.set('state', 0)
                    state = save_data(saleCategorySecond)
                    # 记录返回的状态
                    relation.add(saleCategorySecond)
                    if state:
                        categoryImage = CategoryImage()
                        categoryImage.set('imageFile', saleCategorySecond.get('mainImage'))
                        categoryImage.set('saleCategorySecond', saleCategorySecond)
                        save_data(categoryImage)
                else:
                    sys_log('this item exists')
            else:
                sys_log('name or briefDescription or image is null')
        save_data(saleCategoryFirst)


def getStoreCategory():
    """
    获得库存分类表
    :return: 
    """
    # storeCategoryFirst = queryAllInstance(CLASS_STORE_CATEGORY_FIRST, 'objectId')
    storeCategoryFirst = base.queryInstanceAttribute(CLASS_STORE_CATEGORY_FIRST, 'state', 0)
    if storeCategoryFirst:
        storeCategoryList = [
            {
                'objectId': first.get('objectId'),
                'name': first.get('name'),
                'value': [
                    {
                        'objectId': second.get('objectId'),
                        'name': second.get('name'),
                        'value': [
                            {
                                'objectId': third.get('objectId'),
                                'name': third.get('name'),
                            } for third in base.get_relation_data_and_attribute(second.get('objectId'), CLASS_STORE_CATEGORY_SECOND, 'storeCategoryThird', 'state', 0)
                        ]
                    } for second in base.get_relation_data_and_attribute(first.get('objectId'), CLASS_STORE_CATEGORY_FIRST, 'storeCategorySecond', 'state', 0)
                ]
            } for first in storeCategoryFirst
        ]
        return storeCategoryList
    return None


def saveStoreCategory(storeCategoryList):
    """
    创建库层分类表
    :param storeCategoryList: 
    :return: 
    """
    StoreCategoryFirst = leancloud.Object.extend(CLASS_STORE_CATEGORY_FIRST)
    StoreCategorySecond = leancloud.Object.extend(CLASS_STORE_CATEGORY_SECOND)
    StoreCategoryThird = leancloud.Object.extend(CLASS_STORE_CATEGORY_THIRD)
    sys_log(storeCategoryList)

    for first in storeCategoryList:
        # 检查该元素是否已经存在
        result = queryInstanceThroughName(CLASS_STORE_CATEGORY_FIRST, 'name', first['name'])
        if result:
            sys_log('first element is existed')
        else:
            storeCategoryFirst = StoreCategoryFirst()
            storeCategoryFirst.set('name', first['name'])
            storeCategoryFirst.set('state', 0)
            # 保存所有第二级数据，并将第二级数据加入到第一级数据
            storeCategoryFirst.save()
            relationFirst = storeCategoryFirst.relation('storeCategorySecond')
            print(first['value'])
            for second in first['value']:
                result = queryInstanceThroughName(CLASS_STORE_CATEGORY_SECOND, 'name', second['name'])
                if result:
                    sys_log('second element is existed')
                else:
                    storeCategorySecond = StoreCategorySecond()
                    storeCategorySecond.set('name', second['name'])
                    storeCategorySecond.set('state', 0)
                    storeCategorySecond.set('storeCategoryFirst', storeCategoryFirst)
                    storeCategorySecond.save()
                    relationSecond = storeCategorySecond.relation('storeCategoryThird')
                    # 保存所有的第三级数据，并同时将该关系加入到第二级数据中
                    for third in second['value']:
                        result = queryInstanceThroughName(CLASS_STORE_CATEGORY_THIRD, 'name', third)
                        if result:
                            sys_log('third element is existed')
                        else:
                            storeCategoryThird = StoreCategoryThird()
                            storeCategoryThird.set('name', third)
                            storeCategoryThird.set('state', 0)
                            storeCategoryThird.set('storeCategorySecond', storeCategorySecond)
                            if save_data(storeCategoryThird):
                                relationSecond.add(storeCategoryThird)

                    # 保存第二级数据
                    if save_data(storeCategorySecond):
                        # 添加关系
                        relationFirst.add(storeCategorySecond)
            save_data(storeCategoryFirst)


def searchProductGroupWithSaleTag(objectId):
    """
    查找符合销售策略的所有商品组
    :param objectId: 
    :return: 
    """
    queryList = get_relation_data(objectId, CLASS_SALE_CATEGORY_SECOND, 'productGroup')
    sys_log(queryList)
    return queryList


def newStoreCategoryItem(className: object, value: object, className2: object = None, objectId: object = None, relationName: object = None, pointName=None):
    """
    增加新的库存分类项
    :rtype: object
    """
    if className and value:
        StoreCategory = leancloud.Object.extend(className)
        storeCategory = StoreCategory()
        storeCategory.set('name', value)
        storeCategory.set('state', 0)
        if save_data(storeCategory):
            if className2 and objectId and relationName:
                instance = queryInstanceThroughId(className2, objectId)
                relation = instance.relation(relationName)
                relation.add(storeCategory)
                save_data(instance)
                storeCategory.set(pointName, instance)
                save_data(storeCategory)
    else:
        sys_log('parameter is null')


def delStoreCategoryItem(className, objectId):
    if className and objectId:
        instance = queryInstanceThroughId(className, objectId)
        instance.set('state', 2)
        save_data(instance)
    else:
        sys_log('parameter is null')


def saveStoreCategoryItem(className, objectId, value):
    if className and objectId and value:
        instance = queryInstanceThroughId(className, objectId)
        instance.set('name', value)
        save_data(instance)
    else:
        sys_log('parameter is null')


def getStoreCategoryItem(className, objectId):
    if className and objectId:
        instance = queryInstanceThroughId(className, objectId)
        return instance.get('name')
    else:
        sys_log('parameter is null')
        return None


def getStoreCategoryThroughProductGroup(thirdObjectId):
    third = queryInstanceThroughId(CLASS_STORE_CATEGORY_THIRD, thirdObjectId)
    if third:
        second = queryInstanceThroughId(CLASS_STORE_CATEGORY_SECOND, third.get('storeCategorySecond').id)

        if second:
            first = queryInstanceThroughId(CLASS_STORE_CATEGORY_FIRST, second.get('storeCategoryFirst').id)
            if first:
                tag = first.get('objectId') + ' ' + second.get('objectId') + ' ' + third.get('objectId')
                sys_log(tag)
                return tag
            else:
                sys_log('firstCategory is null')
        else:
            sys_log('second is null')
    else:
        sys_log('firstCategory is null')
    return None


def getSaleCategoryThroughProductGroup(productGroupObjectId):
    secondList = get_relation_data(productGroupObjectId, 'ProductGroup', 'saleCategory')
    if secondList:
        tagList = []
        for second in secondList:
            first = queryInstanceThroughId(CLASS_SALE_CATEGORY_FIRST, second.get('saleCategoryFirst').id)
            if first:
                tag = first.get('objectId') + ' ' + second.get('objectId')
                tagList.append(tag)
            else:
                sys_log('firstCategory is null')
        if len(tagList) > 0:
            return tagList
        else:
            sys_log('taglist is null')
    else:
        sys_log('seconlist is not exist')
    return None


def getProductGroupInStoreCategoryFirst(objectId):
    """
    获得库存分类表
    :return: 
    """
    if objectId:
        storeCategoryList = []
        secondList = get_relation_data(objectId, CLASS_STORE_CATEGORY_FIRST, 'storeCategorySecond')
        sys_log(secondList)
        for second in secondList:
            if second.get('state') != DELETE_STATE:
                for third in get_relation_data(second.get('objectId'), CLASS_STORE_CATEGORY_SECOND, 'storeCategoryThird'):
                    if third.get('state') != DELETE_STATE:
                        tmpList = get_relation_data(third.get('objectId'), CLASS_STORE_CATEGORY_THIRD, 'productGroup')
                        sys_log(tmpList)
                        storeCategoryList += tmpList
        sys_log(storeCategoryList)
        return storeCategoryList
    return None


def getProductGroupInStoreCategorySecond(objectId):
    """
    获得库存分类表
    :return: 
    """
    if objectId:
        storeCategoryList = []
        thirdList = get_relation_data(objectId, CLASS_STORE_CATEGORY_SECOND, 'storeCategoryThird')
        for third in thirdList:
            if third.get('state') != DELETE_STATE:
                tmpList = get_relation_data(third.get('objectId'), CLASS_STORE_CATEGORY_THIRD, 'productGroup')
                storeCategoryList += tmpList
        sys_log(storeCategoryList)
        return storeCategoryList
    else:
        sys_log('second is null')
    return None


def getProductGroupInStoreCategoryThird(objectId):
    """
    获得库存分类表
    :return: 
    """
    if objectId:
        storeCategoryList = get_relation_data(objectId, CLASS_STORE_CATEGORY_THIRD, 'productGroup')
        sys_log(storeCategoryList)
        return storeCategoryList
    return None


def getProductGroupSaleCategoryFirst(objectId):
    """
    获得销售分类表
    :return: 
    """
    if objectId:
        saleCategoryList = []
        secondList = get_relation_data(objectId, CLASS_SALE_CATEGORY_FIRST, 'saleCategorySecond')
        for second in secondList:
            if second.get('state') != DELETE_STATE:
                tmpList = get_relation_data(second.get('objectId'), CLASS_SALE_CATEGORY_SECOND, 'productGroup')
                saleCategoryList += tmpList
        sys_log(saleCategoryList)
        return saleCategoryList
    return None


def getProductGroupSaleCategorySecond(objectId):
    """
    获得销售分类表
    :return: 
    """
    if objectId:
        saleCategoryList = get_relation_data(objectId, CLASS_SALE_CATEGORY_SECOND, 'productGroup')
        sys_log(saleCategoryList)
        return saleCategoryList
    return None


def filterSaleCategory(productGroupList, tagSale):
    """
    在组合搜索中过滤掉sale标签
    :param productGroupList: 
    :param tagSale: 
    :return: 
    """
    productGroupList2 = []
    if tagSale and productGroupList:
        for foo in productGroupList:
            tagList1 = getSaleCategoryThroughProductGroup(foo.get('objectId'))
            if tagList1:
                for tag in tagList1:
                    if tag and re.match(tagSale, tag):
                        productGroupList2.append(foo)
                        break
    else:
        sys_log('tagSale or productGroup is null')
    return productGroupList
