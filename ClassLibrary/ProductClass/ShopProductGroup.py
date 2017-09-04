from ClassLibrary.BaseClass.Object import Class_Name_ShopProduct
from ClassLibrary.ProductClass.ProductGroup_New import ProductGroup



class ShopProductGroup(ProductGroup):
    def __init__(self):
        super(ShopProductGroup, self).__init__()
        self.className = self.__class__.__name__
        # 用于区分商家商品和上线商品
        self.productName = Class_Name_ShopProduct
"""
    def count_ProductGroup_All_Audit(self, shop):
        
        统计店铺中所有自己创建的待审计商品个数
        :param shop: 
        :return: 
        
        self.instance = self.instance
        count = Base.queryInstanceAttribute1_Attribute2_Count(self.__class__.__name__, attribute_shop, shop, attribute_state, 0)
        if count:
            return count
        else:
            return 0

    def get_ProductGroup_All_Audit(self, shop, skip=None, limit=None):
        
        获得店铺中所有自己创建的待审计商品
        :param shop: 
        :param skip: 
        :param limit: 
        :return: 
        
        productGroupList = Base.queryInstanceAttribute1_Attribute2(self.__class__.__name__,attribute_shop, shop, attribute_state, 0, skip, limit)
        if productGroupList:
            a = [
                self.output_ProductGroup_Simple(foo)for foo in productGroupList
            ]
            return a

"""
