from ClassLibrary.BaseClass.Attribute_Parameter import *
from ClassLibrary.ProductClass.ProductGroupBase import ProductGroupBase
from ClassLibrary.ProductClass.ShopProduct import ShopProduct


class ShopProductGroup(ProductGroupBase):
    def __init__(self):
        super(ShopProductGroup, self).__init__()
        self.className = self.__class__.__name__
        # 用于区分商家商品和上线商品
        self.productName = Class_Name_ShopProduct

    def set_attribute_shop(self, shopInstance):
        if self.instance and shopInstance:
            self.instance.set(attribute_shop, shopInstance)
            if self.__save_instance__():
                product = self.get_attribute_relation(attribute_product)
                if product:
                    self.__print_msg__error( product )
                    for foo in product:
                        product = ShopProduct()
                        product.get_Object(foo.get(attribute_objectId))
                        product.set_attribute_value(attribute_shop, shopInstance)
                return True
        return None

