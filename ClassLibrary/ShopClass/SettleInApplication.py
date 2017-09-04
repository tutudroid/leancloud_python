from ClassLibrary.BaseClass.Object import *
from ClassLibrary.ShopClass.SettleInCompany import SettleInCompany
from ClassLibrary.ShopClass.SettleInUser import SettleInUser


class SettleInApplication(Object):
    def __init__(self):
        super(SettleInApplication, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_infoCompany(self):
        if self.instance and self.instance.get(attribute_infoCompany):
            settleIn = SettleInCompany()
            settleIn.get_Object(self.instance.get(attribute_infoCompany).id)
            return settleIn.output_SettleIn()

    def get_attribute_user(self):
        if self.instance and self.instance.get(attribute_user):
            return self.instance.get(attribute_user).id

    def get_attribute_infoPersonal(self):
        if self.instance and self.instance.get(attribute_infoPersonal):
            settleIn = SettleInUser()
            settleIn.get_Object(self.instance.get(attribute_infoPersonal).id)
            return settleIn.output_SettleIn()

    def get_user(self):
        if self.instance:
            return self.instance.get(attribute_user)

    def get_infoPersonal(self):
        if self.instance:
            return self.instance.get(attribute_infoPersonal)

    def get_infoCompany(self):
        if self.instance:
            return self.instance.get(attribute_infoCompany)

    def get_attribute_type(self):
        if self.instance:
            return self.instance.get(attribute_type)

    def set_attribute_type(self, value):
        if self.instance:
            self.instance.set(attribute_type, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_user(self, value):
        if self.instance:
            self.instance.set(attribute_user, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_InfoPersonal(self, value):
        if self.instance:
            self.instance.set(attribute_infoPersonal, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_InfoCompany(self, value):
        if self.instance:
            self.instance.set(attribute_infoCompany, value)
            self.__save_instance__()
            return True
        return None

    def output_SettleInApplication(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_state: self.get_attribute_state(),
                attribute_infoPersonal: self.get_attribute_infoPersonal(),
                attribute_infoCompany: self.get_attribute_infoCompany(),
            }
            return data

    def find_User(self, user):
        result = Base.queryInstanceAttribute(self.__class__.__name__, attribute_user, user)
        if result:
            return True
        return None