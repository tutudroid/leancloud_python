from ClassLibrary.BaseClass.Object import *
from ClassLibrary.ProductClass.ProductGroup_New import ProductGroup


class SaleCategoryRecommend(Object):
    def __init__(self):
        super(SaleCategoryRecommend, self).__init__()
        self.className = self.__class__.__name__

    def set_attribute_productGroup(self, value):
        if self.instance and value:
            self.instance.set(attribute_productGroup, value)
            self.save_instance()
            return True
        return None

    def output_SaleCategoryRecommend(self):
        if self.instance:
            A = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_mainImage: self.get_attribute_image_url(attribute_mainImage),
                attribute_productGroup: self.get_attribute_Object_Id(attribute_productGroup),
                attribute_productGroupUniqueId: self.get_attribute(attribute_productGroupUniqueId)
            }
            return A
        return {}

    def create_SaleCategoryRecommend(self, data):
        if data[attribute_objectId]:
            self.get_Object(data[attribute_objectId])
        else:
            self.create_Object()
        self.set_attribute_value(attribute_productGroup, data[attribute_productGroup])
        self.set_attribute_value(attribute_mainImage, data[attribute_mainImage])
        self.set_attribute_value(attribute_state, int(data[attribute_state]))
