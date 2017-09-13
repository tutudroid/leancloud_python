from ClassLibrary.BaseClass.Object import *
from ClassLibrary.OrderClass.OrderProduct import OrderProduct


class AfterSaleSupport(Object):
    def __init__(self):
        super(AfterSaleSupport, self).__init__()

    def get_attribute_serviceState(self):
        if self.instance:
            return self.instance.get(attribute_serviceState)
        return None

    def get_attribute_order(self):
        if self.instance:
            return self.instance.get(attribute_order)
        return None

    def get_attribute_orderProduct(self):
        if self.instance and self.instance.get(attribute_orderProduct):
            orderProduct = OrderProduct()
            orderProduct.get_Object(self.instance.get(attribute_orderProduct).id)
            return orderProduct.output_OrderProduct()
        return None

    def set_attribute_serviceState(self, value):
        if self.instance and 0 <= int(value) <= 3:
            self.instance.set(attribute_serviceState, int(value))
            self.save_instance()
            return True
        return None

    def set_attribute_orderProduct(self, value):
        if self.instance and value:
            self.instance.set(attribute_orderProduct, value)
            self.save_instance()
            return True
        return None

    def set_attribute_order(self, value):
        if self.instance and value:
            self.instance.set(attribute_order, value)
            self.save_instance()
            return True
        return None

    def set_attribute_user(self, value):
        if self.instance and value:
            self.instance.set(attribute_user, value)
            self.save_instance()
            return True
        return None

    def set_attribute_shop(self, value):
        if self.instance and value:
            self.instance.set(attribute_shop, value)
            self.save_instance()
            return True
        return None
