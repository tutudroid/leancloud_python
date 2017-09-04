from ClassLibrary.BaseClass.Object import *
from ClassLibrary.ShopClass.Shop_New import Shop
from ClassLibrary.UserClass.Role import _Role


class _User(Object):
    def __init__(self):
        super(_User, self).__init__()
        self.className = self.__class__.__name__

    def create_Object(self, username='username2'):
        if self.className:
            INSTANCE = leancloud.Object.extend(self.className)
            instance = INSTANCE()
            instance.set(attribute_state, STATE_OK)
            instance.set(attribute_username, username)
            instance.set(attribute_password, 'password')
            self.instance = instance
            return self.__save_instance__()
        self.__print_msg__('create object fail')
        return None

    def get_User_phoneNumber(self, phoneNumber):
        if self.className and phoneNumber:
            self.instance = Base.queryInstanceAttribute(self.className, attribute_mobilePhoneNumber, phoneNumber)
            return self.instance
        return None


    def get_attribute_username(self):
        if self.instance:
            return self.instance.get(attribute_username)
        return None

    def get_attribute_mobilePhoneNumber(self):
        if self.instance:
            return self.instance.get(attribute_mobilePhoneNumber)
        return None

    def get_attribute_avatar(self):
        if self.instance and self.instance.get(attribute_avatar) == "{'provider': 'qiniu'}":
            return self.instance.get(attribute_avatar).url
        return None

    def get_avatar(self):
        if self.instance and self.instance.get(attribute_avatar):
            return self.instance.get(attribute_avatar)
        return None

    def get_attribute_shop(self):
        if self.instance and self.instance.get(attribute_shop):
            shop = Shop()
            shop.get_Object(self.instance.get(attribute_shop).id)
            return shop.output_Shop()
        return None

    def get_shop(self):
        if self.instance and self.instance.get(attribute_shop):
            return self.instance.get(attribute_shop).id
        return None

    def get_attribute_nikeName(self):
        if self.instance:
            return self.instance.get(attribute_nikeName)
        return None

    def get_attribute_role(self):
        if self.instance:
            role = Base.get_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_role)
            if role:
                returnList = []
                for foo in role:
                    returnList.append(foo.get(attribute_name))
                return returnList
        return None

    def get_attribute_sex(self):
        if self.instance:
            return self.instance.get(attribute_sex)
        return None

    def get_attribute_birthday(self):
        if self.instance:
            return self.instance.get(attribute_birthday)
        return None


    def get_attribute_forbidden(self):
        if self.instance:
            return self.instance.get(attribute_forbidden)
        return None

    def set_attribute_shop(self, shop):
        if self.instance and shop:
            self.instance.set(attribute_shop, shop)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_forbidden(self, value):
        if self.instance:
            self.instance.set(attribute_forbidden, value)
            self.__save_instance__()
            return True
        return None


    def set_attribute_username(self, value):
        if self.instance and value:
            self.instance.set(attribute_username, value)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_password(self, password):
        if self.instance and password:
            self.instance.set(attribute_password, password)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_mobilePhoneNumber(self, mobilePhoneNumber):
        if self.instance and mobilePhoneNumber:
            self.instance.set(attribute_mobilePhoneNumber, mobilePhoneNumber)
            if self.__save_instance__():
                return True
        return None


    def set_attribute_sys_Role(self):
        if self.instance:
            role = _Role()
            role.get_Object_name(ROLE_SYS)
            if role.set_attribute_users(self.instance):
                return True
        return None

    def set_attribute_role(self, name):
        if self.instance and name:
            role = _Role()
            role.get_Object_attribute_name(attribute_name, name)
            relation = self.instance.relation(attribute_role)
            relation.add(role.get_instance())
            if self.__save_instance__():
                role.set_attribute_users(self.instance)
                return True
        return None

    def set_attribute_avator(self, value):
        if self.instance and value:
            avator = Base.save_image(value)
            self.instance.set(attribute_avatar, avator)
            if self.__save_instance__():
                return True
        return None

    def count_App_User(self):
        self.instance = self.instance
        app = Base.queryInstanceAttribute(Class_Name_Role, attribute_name, ROLE_APP)
        if app:
            count = Base.count_relation_data(app.get(attribute_objectId), Class_Name_Role, attribute_users)
            return count
        return 0

    def get_App_User(self, skip):
        self.instance = self.instance
        app = Base.queryInstanceAttribute(Class_Name_Role, attribute_name, ROLE_APP)
        if app:
            appList = Base.get_relation_data(app.get(attribute_objectId), Class_Name_Role, attribute_users, skip)
            returnList = []
            if appList:
                for foo in appList:
                    user = _User()
                    user.set_instance(foo)
                    returnList.append(user.output_User())
            return returnList
        return []

    def output_User(self):
        if self.instance:
            data = {
                attribute_avatar: self.get_attribute_avatar(),
                attribute_nikeName: self.get_attribute_nikeName(),
                attribute_mobilePhoneNumber: self.get_attribute_mobilePhoneNumber(),
                attribute_role: self.get_attribute_role(),
                attribute_state: self.get_attribute_state(),
                attribute_username: self.get_attribute_username(),
                attribute_forbidden: self.get_attribute_forbidden(),
                attribute_sex: self.get_attribute_sex(),
                attribute_birthday: self.get_attribute_birthday(),
                attribute_createdAt: self.get_attribute_createdAt(),
            }
            return data

    def input_User(self, request):
        self.instance = self.instance
        data = {
            attribute_username: request.POST.get(attribute_username, ''),
            attribute_password: request.POST.get(attribute_password, ''),
            attribute_passwordSure: request.POST.get(attribute_passwordSure, ''),
            attribute_role: request.POST.get(attribute_role, ''),
            attribute_mobilePhoneNumber: request.POST.get(attribute_phoneNumber, ''),
            attribute_avatar: request.FILES.get(attribute_avatar, '')
        }
        print(data)
        return data


    def create_User(self, data):
        if data[attribute_username]:
            username = data[attribute_username]
            if self.get_Object_attribute_name(attribute_username, username):
                return False
            self.create_Object(username)
        else:
            self.create_Object()
        if data[attribute_role]:
            self.set_attribute_role(data[attribute_role])
            self.set_attribute_sys_Role()
        if data[attribute_password] and data[attribute_password] != data[attribute_passwordSure]:
            self.set_attribute_password(data[attribute_password])
        if data[attribute_mobilePhoneNumber]:
            self.set_attribute_mobilePhoneNumber(data[attribute_mobilePhoneNumber])
        if data[attribute_avatar]:
            self.set_attribute_avator(data[attribute_avatar])
        return True

    def get_User_Role_All(self, name, page):
        """
        获得某角色的所有用户
        :param name:
        :param page:
        :return:
        """
        self.instance = self.instance
        if name:
            role = _Role()
            role.get_Object_name(name)
            users_with_role = role.get_attribute_users(page)
            if users_with_role:
                returnList = []
                print(users_with_role)
                for foo in users_with_role:
                    user = _User()
                    user.set_instance(foo)
                    returnList.append(user.output_User())
                return returnList
        return []

    def count_User_Role_All(self, name):
        """
        获得某角色的所有用户
        :param name:
        :return:
        """
        self.instance = self.instance
        if name:
            role = _Role()
            role.get_Object_name(name)
            return Base.count_relation_data(role.get_attribute_objectId(), Class_Name_Role, attribute_users)
        return 0

    def logout(self):
        if self.instance:
            self.instance.logout()
        return None
