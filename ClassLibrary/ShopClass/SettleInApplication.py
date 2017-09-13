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

    def get_attribute_user_id(self):
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
            self.save_instance()
            return True
        return None

    def set_attribute_user(self, value):
        if self.instance:
            self.instance.set(attribute_user, value)
            self.save_instance()
            return True
        return None

    def set_attribute_InfoPersonal(self, value):
        if self.instance:
            self.instance.set(attribute_infoPersonal, value)
            self.save_instance()
            return True
        return None

    def set_attribute_InfoCompany(self, value):
        if self.instance:
            self.instance.set(attribute_infoCompany, value)
            self.save_instance()
            return True
        return None

    def output_SettleInApplication(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_state: self.get_attribute_state(),
                attribute_infoPersonal: self.get_attribute_infoPersonal(),
                attribute_infoCompany: self.get_attribute_infoCompany(),
                attribute_type: self.get_attribute_type(),
            }
            return data

    def find_User(self, user):
        result = Base.queryInstanceAttribute(self.__class__.__name__, attribute_user, user)
        if result:
            return True
        return None

    def get_SettleInApplication_All(self, state, type1=None, page=1):

        print(state)
        if state is not None and page:
            if 0 == int(state):
                query = Base.queryInstanceAttribute(self.__class__.__name__, attribute_state, int(state), page)
            else:
                query = Base.queryInstanceAttribute1_Attribute2(self.__class__.__name__, attribute_type, int(type1), attribute_state, int(state), page)
            if query:
                settle = []
                for foo in query:
                    settleApplication = SettleInApplication()
                    settleApplication.set_instance(foo)
                    settle.append(settleApplication.output_SettleInApplication())
                return settle
        return []

    def count_SettleInApplication_All(self, state, type1):
        if state is not None:
            if 0 == int(state):
                count = Base.queryInstanceAttributeCount(self.__class__.__name__, attribute_state, int(state))
            else:
                count = Base.queryInstanceAttribute1_Attribute2_Count(self.__class__.__name__, attribute_type, int(type1), attribute_state, int(state))
            return count
        self.print_msg__error( 'parameter is null' )
        return 0
