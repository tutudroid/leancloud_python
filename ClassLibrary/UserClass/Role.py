from ClassLibrary.BaseClass.Object import *


class _Role(Object):
    def __init__(self):
        super(_Role, self).__init__()
        self.className = self.__class__.__name__

    def set_attribute_users(self, value):
        if self.instance:
            relation = self.instance.relation(attribute_users)
            relation.add(value)
            if self.__save_instance__():
                return True
        return None

    def get_attribute_users(self, page=1):
        if self.instance:
            users_with_role = Base.get_relation_data(self.get_attribute_objectId(), self.__class__.__name__, attribute_users, page)
            if users_with_role:
                return users_with_role
        return []
