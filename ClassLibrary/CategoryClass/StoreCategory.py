from ClassLibrary.BaseClass.Object import *


class StoreCategory(Object):

    def __init__(self, name=None):
        super(StoreCategory, self).__init__()
        if name:
            self.className = name
        else:
            self.className = self.__class__.__name__
        print(self.className)


    def get_StoreCategoryFirst(self, objectId):
        if objectId:
            store = Base.queryInstanceThroughId(Class_Name_StoreCategoryFirst, objectId)
            self.instance = store
            return store
        return None


    def check_StoreCategoryFirst(self, name):
        self.instance = self.instance
        if name:
            first = Base.queryInstanceAttribute1_Attribute2_First(Class_Name_StoreCategoryFirst, attribute_name, name, attribute_state, 0)
            self.instance = first
            if first:
                return first
        return None


    def check_StoreCategorySecond(self, name, first):
        self.instance = self.instance
        if name and first:
            second = Base.queryInstance_A1_A2_A3_First(Class_Name_StoreCategorySecond, attribute_name, name, attribute_storeCategoryFirst, first, attribute_state, 0)
            self.instance = second
            if second:
                return second
        return None


    def check_StoreCategoryThird(self, name, second):
        self.instance = self.instance
        if name and second:
            third = Base.queryInstance_A1_A2_A3_First(Class_Name_StoreCategoryThird, attribute_name, name, attribute_storeCategorySecond, second, attribute_state, 0)
            self.instance = third
            if third:
                return third
        return None

    def get_StoreCategorySecond(self, objectId):
        if objectId:
            store = Base.queryInstanceThroughId(Class_Name_StoreCategorySecond, objectId)
            self.instance = store
            return store
        return None

    def get_StoreCategoryThird(self, objectId):
        if objectId:
            store = Base.queryInstanceThroughId(Class_Name_StoreCategoryThird, objectId)
            self.instance = store
            return store
        return None

    def get_attribute_storeCategorySecond(self):
        if self.instance:
            second = StoreCategory(Class_Name_StoreCategorySecond)
            second.set_instance(self.instance)
            return second.output_StoreCategorySecond()
        return None

    def get_attribute_storeCategoryThird(self):
        if self.instance:
            store = Base.get_relation_data_and_attribute(self.instance.get(attribute_objectId), self.className, attribute_storeCategoryThird, attribute_state, STATE_OK)
            if store:
                returnList = []
                for foo in store:
                    second = StoreCategory(Class_Name_StoreCategoryThird)
                    second.set_instance(foo)
                    returnList.append(second.output_StoreCategory())
                return returnList
        return None


    def get_attribute_storeCategoryFirst(self):
        self.instance = self.instance
        if self.instance:
            return self.instance.get(attribute_storeCategoryFirst)
        return None


    def get_attribute_productGroup(self):
        if self.instance:
            tmpList = Base.get_relation_data(self.instance.get(attribute_objectId), Class_Name_StoreCategoryThird, attribute_productGroup)
            return tmpList
        return None

    def remove_attribute_productGroup(self, productGroup):
        self.instance = self.instance
        if productGroup and self.instance:
            relation = self.instance.relation(attribute_productGroup)
            relation.remove(productGroup)
            if self.__save_instance__():
                return True
        return None


    def create_StoreCategory(self, data):
        if data:
            if data[attribute_objectId]:
                self.get_Object(data[attribute_objectId])
            else:
                self.create_Object()
            self.set_attribute_name(data[attribute_name])

    def update_Category(self, data):
        if data:
            if data[attribute_objectId]:
                self.get_Object(data[attribute_objectId])
            self.set_attribute_name(data[attribute_name])
            if data[attribute_state] != '':
                self.set_attribute_state(data[attribute_state])
                self.delete_Category()
            return True
        return None

    def delete_Category(self):
        if self.className == Class_Name_StoreCategorySecond:
            First = StoreCategory(Class_Name_StoreCategoryFirst)
            firstInstance = self.get_attribute_storeCategoryFirst()
            if firstInstance:
                First.get_Object(firstInstance.id)
                First.remove_attribute_relation(attribute_storeCategorySecond, self.instance)
                return True
        if self.className == Class_Name_StoreCategoryThird:
            second = StoreCategory(Class_Name_StoreCategorySecond)
            secondInstance = self.instance.get(attribute_storeCategorySecond)
            if secondInstance:
                second.get_Object(secondInstance.id)
                second.remove_attribute_relation(attribute_storeCategoryThird, self.instance)
                return True
        return None

    def create_StoreCategoryFirst(self, data):
        if data:
            self.create_StoreCategory(data)
            return True
        return None

    def create_StoreCategorySecond(self, data, storeCategoryFirst):
        if data:
            self.create_StoreCategory(data)
            self.set_attribute_storeCategoryFirst(storeCategoryFirst)
            return True
        return None

    def create_StoreCategoryThird(self, data, storeCategorySecond):
        if data and storeCategorySecond:
            self.create_StoreCategory(data)
            self.set_attribute_storeCategorySecond(storeCategorySecond)
            return True
        return None

    def output_StoreCategory(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_name: self.get_attribute_name(),
                attribute_state: self.get_attribute_state(),
            }
            return data
        return None

    def output_StoreCategorySecond(self):
        if self.instance:
            data = self.output_StoreCategory()
            data.update({attribute_storeCategoryThird: self.get_attribute_storeCategoryThird()})
            return data
        return None

    def output_StoreCategoryFirst(self):
        if self.instance:
            data = self.output_StoreCategory()
            data.update({attribute_storeCategorySecond: self.get_attribute_storeCategorySecond()})
            return data
        return None

    def create_Store_Category(self, storeCategoryList):
        """
        创建库层分类表
        :param storeCategoryList: 
        :return: 
        """
        self.instance = self.instance
        if storeCategoryList:
            for first in storeCategoryList:
                storeCategoryFirst = self.check_StoreCategoryFirst(first[attribute_name])
                if not storeCategoryFirst:
                    storeCategoryFirst = self.create_StoreCategoryFirst(first['name'])

                relationFirst = storeCategoryFirst.relation('storeCategorySecond')
                for second in first['value']:
                    # 检查该元素是否存在
                    storeCategorySecond = self.check_StoreCategorySecond(second['name'], storeCategoryFirst)
                    if not storeCategorySecond:
                        storeCategorySecond = self.create_StoreCategorySecond(second['name'], storeCategoryFirst)

                    relationSecond = storeCategorySecond.relation('storeCategoryThird')
                    # 保存所有的第三级数据，并同时将该关系加入到第二级数据中
                    for third in second['value']:
                        storeCategoryThird = self.check_StoreCategoryThird(third, storeCategorySecond)
                        if not storeCategoryThird:
                            storeCategoryThird = self.create_StoreCategoryThird(third, storeCategorySecond)
                        relationSecond.add(storeCategoryThird)

                    # 保存第二级数据
                    if Base.save_data(storeCategorySecond):
                        # 添加关系
                        relationFirst.add(storeCategorySecond)
                Base.save_data(storeCategoryFirst)
        else:
            Base.sys_log('storeCategoryList is null')


    def set_attribute_productGroup(self, productGroup):
        if self.instance and productGroup:
            relationProductGroup = self.instance.relation(attribute_productGroup)
            relationProductGroup.add(productGroup)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_storeCategoryFirst(self, first):
        if self.instance and first:
            self.instance.set(attribute_storeCategoryFirst, first)
            self.__save_instance__()
            return True
        return None

    def set_attribute_storeCategorySecond(self, second):
        if self.instance and second:
            if self.className == Class_Name_StoreCategoryFirst:
                relation = self.instance.relation(attribute_storeCategorySecond)
                relation.add(second)
                if self.__save_instance__():
                    return True
            if self.className == Class_Name_StoreCategoryThird:
                self.instance.set(attribute_storeCategorySecond, second)
                self.__save_instance__()
            return True
        return None

    def set_attribute_storeCategoryThird(self, third):
        if self.instance and third:
            relation = self.instance.relation(attribute_storeCategoryThird)
            relation.add(third)
            self.__save_instance__()
            return True
        return None

    def get_StoreCategory_All(self):
        """
        获得库存分类表
        :return: 
        """
        self.instance = self.instance
        storeCategoryFirst = Base.queryInstanceAttribute(Class_Name_StoreCategoryFirst, attribute_state, 0)
        if storeCategoryFirst:
            storeCategoryList = []
            for foo in storeCategoryFirst:
                first = StoreCategory(Class_Name_StoreCategoryFirst)
                first.set_instance(foo)
                storeCategoryList.append(first.output_StoreCategoryFirst())
            return storeCategoryList
        return None

    def input_Category(self, request):
        self.instance = self.instance
        data = {
            attribute_name: request.POST.get(attribute_name, ''),
            attribute_objectId: request.POST.get(attribute_objectId, ''),
        }
        return data

