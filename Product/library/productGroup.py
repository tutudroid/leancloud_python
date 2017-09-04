"""
Standard Product Unit
2017-5-2更新了库存和销售分类的存储策略
"""
from Product.library.base import sys_log


def outputProductGroup(productGroupList):
    if productGroupList:
        productGroup = [
            {
                'name': foo.get('name'),
                'mainImage': foo.get('mainImage'),
                'objectId': foo.get('objectId'),
                'briefDescription': foo.get('briefDescription'),
            } for foo in productGroupList if foo.get('state') != 1
        ]
        sys_log(productGroup)
        return productGroup
    else:
        sys_log('productGroupList is null')
        return None
