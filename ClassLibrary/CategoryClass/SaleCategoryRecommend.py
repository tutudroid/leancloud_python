from ClassLibrary.BaseClass.Object import *
from ClassLibrary.ProductClass.ProductGroup_New import ProductGroup

class SaleCategoryRecommend(Object):
    def __init__(self):
        super(SaleCategoryRecommend, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_productGroup(self):
        if self.instance:
            return self.instance.get(attribute_productGroup)
        return None

    def set_attribute_productGroup(self, value):
        if self.instance and value:
            self.instance.set(attribute_productGroup, value)
            self.__save_instance__()
            return True
        return None

    def output_SaleCategoryRecommend(self):
        if self.instance:
            A = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_mainImage: self.get_attribute_mainImage(),
                attribute_productGroup: self.get_attribute_productGroup(),
            }
            return A
        return {}

    def output_Class_Name_SaleCategoryRecommend(self):
        self.instance = self.instance
        if self.instance:
            productGroupId = self.instance.get(attribute_productGroup).id
            product = ProductGroup()
            product.get_Object(productGroupId)
            A = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_mainImage: self.get_attribute_mainImage(),
                attribute_productGroup: product.get_attribute_uniqueId(),
            }
            return A
        return {}
