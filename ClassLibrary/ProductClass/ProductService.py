from ClassLibrary.BaseClass.Object import *


class ProductService(Object):
    def __init__(self):
        super(ProductService, self).__init__()
        self.className = self.__class__.__name__
        self.briefDescription = None

    def get_attribute_briefDescription(self):
        if self.instance:
            return self.instance.get(attribute_briefDescription)

    def set_attribute_briefDescription(self, brief):
        if self.instance and brief:
            self.instance.set(attribute_briefDescription, brief)
            self.save_instance()

    def get_ProductService_All(self):
        self.instance = self.instance
        productService = Base.queryAllInstance(self.__class__.__name__, attribute_objectId)
        if productService:
            productServiceList = []
            for foo in productService:
                tmp = ProductService()
                tmp.set_instance(foo)
                productServiceList.append(tmp.output_ProductService())
            return productServiceList
        return None

    def output_ProductService(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_name: self.get_attribute_name(),
                attribute_briefDescription: self.get_attribute_briefDescription(),
            }
            return data
        return None

    def create_ProductService(self, data):
        self.create_Object()
        self.set_attribute_name(data[attribute_name])
        self.set_attribute_briefDescription(data[attribute_briefDescription])
