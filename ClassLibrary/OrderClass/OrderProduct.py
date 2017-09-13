from ClassLibrary.BaseClass.Object import *
from ClassLibrary.ImageClass.Image import ImageBase


class OrderProduct(Object):
    def __init__(self):
        super(OrderProduct, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_productGroup(self):
        if self.instance:
            return self.instance.get(attribute_productGroup)

    def get_attribute_groupName(self):
        if self.instance:
            return self.instance.get(attribute_groupName)

    def get_attribute_product(self):
        if self.instance:
            return self.instance.get(attribute_product)

    def get_attribute_productStyle(self):
        if self.instance:
            return self.instance.get(attribute_productStyle)

    def get_attribute_productMainImage(self):
        if self.instance and isinstance(self.instance.get(attribute_productMainImage), ISINSTANCE_FILE):
            return self.instance.get(attribute_productMainImage).url

    def get_attribute_productPrice(self):
        if self.instance:
            return self.instance.get(attribute_productPrice)

    def get_attribute_productCount(self):
        if self.instance:
            return self.instance.get(attribute_productCount)

    def set_attribute_productGroup(self, value):
        if self.instance and value:
            self.instance.set(attribute_productGroup, value)
            self.save_instance()
            return True
        return None

    def set_attribute_groupName(self, value):
        if self.instance and value:
            self.instance.set(attribute_groupName, value)
            self.save_instance()
            return True
        return None

    def set_attribute_product(self, value):
        if self.instance and value:
            self.instance.set(attribute_product, value)
            self.save_instance()
            return True
        return None

    def set_attribute_productStyle(self, value):
        if self.instance and value:
            self.instance.set(attribute_productStyle, value)
            self.save_instance()
            return True
        return None

    def set_attribute_productMainImage(self, value):
        if self.instance and value:
            self.instance.set(attribute_productMainImage, value)
            self.save_instance()
            return True
        return None

    def set_attribute_productPrice(self, value):
        if self.instance and value:
            self.instance.set(attribute_productPrice, value)
            self.save_instance()
            return True
        return None

    def set_attribute_productCount(self, value):
        if self.instance and value:
            self.instance.set(attribute_productCount, value)
            self.save_instance()
            return True
        return None

    def output_OrderProduct(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_productGroup: self.get_attribute_Object_Id(attribute_productGroup),
                attribute_product: self.get_attribute_Object_Id(attribute_product),
                attribute_groupName: self.get_attribute_groupName(),
                attribute_productStyle: self.get_attribute_productStyle(),
                attribute_productMainImage: self.get_attribute_image_url( attribute_productMainImage ),
                attribute_productPrice: self.get_attribute_productPrice(),
                attribute_productCount: self.get_attribute_productCount(),
                attribute_state: self.get_attribute_state(),
            }
            return data

    def create_OrderProduct(self, data):
        self.create_Object()
        self.set_attribute_state(data[attribute_state])
        self.set_attribute_groupName(data[attribute_groupName])
        self.set_attribute_productStyle(data[attribute_productStyle])
        image = ImageBase()
        productMainImage = image.save_ImageFile(data[attribute_productMainImage])
        self.set_attribute_productMainImage(productMainImage)
        self.set_attribute_productPrice(data[attribute_productPrice])
        self.set_attribute_productCount(data[attribute_productCount])
