"""
create in 2017-8-25

function：
    基类
        每个类具有基本参数：uniqueId, objectId, state
        每方法：
            创建类
            获得类的实例
            获得类的属性
            修改类的属性
            删除类
            销毁类
        每个类的内部方法：
            __save_instance__()
            __print_msg__()
"""
from ClassLibrary import Base
import leancloud
import logging
from ClassLibrary.BaseClass.Attribute_Parameter import *


class Object(object):
    def __init__(self):
        self.className = self.__class__.__name__
        self.instance = None
        self.state = STATE_OK

    def create_Object(self):
        if self.className:
            INSTANCE = leancloud.Object.extend(self.className)
            instance = INSTANCE()
            instance.set(attribute_state, STATE_OK)
            self.instance = instance
            return self.__save_instance__()
        self.__print_msg__('create object fail')
        return None

    def delete_Object(self):
        if self.instance:
            self.instance.set(attribute_state, STATE_DELETE)
            return self.__save_instance__()
        return None

    def destroy_Object(self):
        if self.instance:
            try:
                self.instance.destroy()
                return True
            except leancloud.LeanCloudError as e:
                self.__print_msg__(e.error)
            return True
        return None

    def get_Object(self, objectId):
        if self.className and objectId:
            self.instance = Base.queryInstanceThroughId(self.className, objectId)
            print(self.instance)
            return self.instance
        print('null')
        return None

    def get_Object_UniqueId(self, uniqueId):
        if self.className and uniqueId:
            self.instance = Base.queryInstanceAttribute(self.className, attribute_uniqueId, uniqueId)
            return self.instance
        return None

    def get_Object_name(self, name):
        if self.className and name:
            self.instance = Base.queryInstanceAttributeFirst(self.className, attribute_name, name)
            return self.instance
        return None

    def get_Object_attribute_name(self, attribute, name):
        if self.className and name and attribute:
            self.instance = Base.queryInstanceAttributeFirst(self.className, attribute, name)
            return self.instance
        return None

    def get_instance(self):
        return self.instance

    def set_instance(self, instance):
        self.instance = instance

    def get_attribute_className(self):
        return self.className

    def get_attribute_uniqueId(self):
        if self.instance:
            return self.instance.get(attribute_uniqueId)
        return None

    def get_attribute_state(self):
        if self.instance:
            return self.instance.get(attribute_state)
        return None

    def get_attribute_createdAt(self):
        if self.instance:
            return Base.change_timeZone(self.instance.get(attribute_createdAt))
        return None


    def get_attribute_objectId(self):
        if self.instance:
            return self.instance.get(attribute_objectId)
        return None

    def get_attribute_mainImage(self):
        if self.instance and self.instance.get(attribute_mainImage):
            return self.instance.get(attribute_mainImage).url

    def set_attribute_mainImage(self, value):
        if self.instance and value:
            if self.instance.get(attribute_mainImage):
                self.instance.get(attribute_mainImage).destory()
            self.instance.set(attribute_mainImage, value)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_state(self, state):
        if self.instance:
            if state != self.instance.get(attribute_state):
                self.instance.set(attribute_state, state)
                if self.__save_instance__():
                    return True
        return None


    def __save_instance__(self):
        """
        保存对象实例到 lean cloud
        :return: 
        """
        if self.instance:
            try:
                self.instance.save()
                return self.instance
            except leancloud.LeanCloudError as e:
                self.__print_msg__(e.error)
        return None

    def __print_msg__(self, msg):
        """
        输出错误信息
        :param msg: 
        :return: 
        """
        print('------start---------------------------------------------------------------------')
        logging.error(self.className)
        logging.error(msg)
        print('--------------------------------------------------------------------------------')

    def __output_Object__(self, instance):
        """
        用于输出point对象的基本数据
        :param instance: 当前对象中指针指向的对象
        :return: 
        """
        if instance:
            A = {
                attribute_objectId: instance.get(attribute_objectId),
                attribute_name: instance.get(attribute_name)
            }
            return A
        return None

    def get_attribute_name(self):
        if self.instance:
            return self.instance.get(attribute_name)
        return None

    def set_attribute_name(self, name):
        if self.instance and name:
            self.instance.set(attribute_name, name)
            self.__save_instance__()

    def remove_attribute_relation(self, attribute_relation, value):
        if self.instance and value:
            relation = self.instance.relation(attribute_relation)
            relation.remove(value)
            self.__save_instance__()
            return True
        return None

    def add_attribute_relation(self, attribute_relation, value):
        if self.instance and attribute_relation and value:
            relation = self.instance.relation(attribute_relation)
            relation.add(value)
            self.__save_instance__()
            return True
        return None

    def get_attribute_relation(self, attribute):
        if self.instance:
            data = Base.get_relation_data(self.instance.get(attribute_objectId), self.className, attribute)
            return data
        return []

    def get_attribute(self, attribute):
        if self.instance:
            return self.instance.get(attribute)
        return None

    def set_attribute_value(self, attribute, value):
        if self.instance and attribute and value is not None:
            self.instance.set(attribute, value)
            if self.__save_instance__():
                return True
        self.__print_msg__(attribute + ' or ' + str(value) + 'is null')
        return False

    def get_attribute_Object_Id(self, attribute):
        if self.instance and self.instance.get(attribute):
            return self.instance.get(attribute).id
        return None

    def get_attribute_image_url(self, attribute):
        if self.instance and self.instance.get(attribute) and isinstance(self.instance.get(attribute), ISINSTANCE_FILE):
            return self.instance.get(attribute).url
        return None

    def destroy_attribute_image(self, attribute):
        if self.instance and attribute and self.instance.get(attribute) and isinstance(self.instance.get(attribute), ISINSTANCE_FILE):
            self.instance.get(attribute).destroy()
        return None
