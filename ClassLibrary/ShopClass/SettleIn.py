from ClassLibrary.BaseClass.Object import *


class SettleIn(Object):
    def __init__(self):
        super(SettleIn, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_alipay(self):
        if self.instance:
            return self.instance.get(attribute_alipay)
        return None

    def get_attribute_shop(self):
        if self.instance:
            return self.instance.get(attribute_shop)
        return None

    def get_attribute_shopName(self):
        if self.instance:
            return self.instance.get(attribute_shopName)
        return None

    def get_attribute_brandName(self):
        if self.instance:
            return self.instance.get(attribute_brandName)
        return None

    def get_attribute_brandLogo(self):
        if self.instance:
            return self.instance.get(attribute_brandLogo)
        return None

    def get_attribute_brandDescription(self):
        if self.instance:
            return self.instance.get(attribute_brandDescription)
        return None

    def set_attribute_alipay(self, value):
        if self.instance:
            if value != self.instance.get(attribute_alipay):
                self.instance.set(attribute_alipay, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_shop(self, shop):
        if self.instance and shop:
            self.instance.set(attribute_shop, shop)
            if self.className == Class_Name_SettleInUser:
                shop.set(attribute_settleInUser, self.instance)
            else:
                shop.set(attribute_settleInCompany, self.instance)
            if self.__save_instance__() and Base.save_data(shop):
                return True
        return None


    def set_attribute_shopName(self, value):
        if self.instance:
            if value != self.instance.get(attribute_shopName):
                self.instance.set(attribute_shopName, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_brandName(self, value):
        if self.instance:
            if value != self.instance.get(attribute_brandName):
                self.instance.set(attribute_brandName, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_brandLogo(self, value):
        if self.instance:
            if value != self.instance.get(attribute_brandLogo):
                self.instance.set(attribute_brandLogo, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_brandDescription(self, value):
        if self.instance:
            if value != self.instance.get(attribute_brandDescription):
                self.instance.set(attribute_brandDescription, value)
                if self.__save_instance__():
                    return True
        return None

    def output_SettleIn(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_state: self.get_attribute_state(),

                attribute_alipay: self.get_attribute_alipay(),
                attribute_shopName: self.get_attribute_shopName(),
                attribute_brandName: self.get_attribute_brandName(),
                attribute_brandLogo: self.get_attribute_brandLogo(),
                attribute_brandDescription: self.get_attribute_brandDescription(),
            }
            return data

    def create_SettleInBase(self, data):
        if data[attribute_objectId]:
            self.instance = Base.queryInstanceThroughId(self.__class__.__name__, data[attribute_objectId])
        else:
            self.instance = self.create_Object()
        if data[attribute_alipay]:
            self.set_attribute_alipay(data[attribute_alipay])
        if data[attribute_shopName]:
            self.set_attribute_shopName(data[attribute_shopName])
        if data[attribute_brandName]:
            self.set_attribute_brandName(data[attribute_brandName])
        if data[attribute_brandLogo]:
            self.set_attribute_brandLogo(data[attribute_brandLogo])
        if data[attribute_brandDescription]:
            self.set_attribute_brandDescription(data[attribute_brandDescription])
