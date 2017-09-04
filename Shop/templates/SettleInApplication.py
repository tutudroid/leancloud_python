from ClassLibrary.BaseClass.Object import *


class SettleIn(Object):
    def __init__(self):
        super(SettleIn, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_user(self):
        if self.instance:
            return self.instance.get(attribute_user)
        return None

    def get_attribute_type(self):
        if self.instance:
            return self.instance.get(attribute_type)
        return None

    def get_attribute_infoCompany(self):
        if self.instance:
            return self.instance.get(attribute_infoCompany)
        return None

    def get_attribute_infoPersonal(self):
        if self.instance:
            return self.instance.get(attribute_infoPersonal)
        return None
