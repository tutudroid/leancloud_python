from ClassLibrary.BaseClass.Object import Class_Name_ShopProduct
from ClassLibrary.ProductClass.ProductGroupBase import ProductGroupBase



class ShopProductGroup(ProductGroupBase):
    def __init__(self):
        super(ShopProductGroup, self).__init__()
        self.className = self.__class__.__name__
        # 用于区分商家商品和上线商品
        self.productName = Class_Name_ShopProduct

