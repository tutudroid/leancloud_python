from ClassLibrary.BaseClass.Object import *
import ClassLibrary.ProductClass.ProductGroup_New


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
            store = Base.get_relation_data_and_attribute(self.instance.get(attribute_objectId), Class_Name_StoreCategoryFirst, attribute_storeCategorySecond, attribute_state, STATE_OK)
            if store:
                returnList = []
                for foo in store:
                    second = StoreCategory(Class_Name_StoreCategorySecond)
                    second.set_instance(foo)
                    returnList.append(second.output_StoreCategorySecond())
                return returnList
        return None

    def get_attribute_storeCategoryThird(self):
        if self.instance:
            store = Base.get_relation_data_and_attribute(self.instance.get(attribute_objectId), Class_Name_StoreCategorySecond, attribute_storeCategoryThird, attribute_state, STATE_OK)
            if store:
                returnList = []
                for foo in store:
                    third = StoreCategory(Class_Name_StoreCategoryThird)
                    third.set_instance(foo)
                    returnList.append(third.output_StoreCategory())
                print(returnList)
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
            self.set_attribute_value(attribute_name, data[attribute_name])
            return True

    def update_Category(self, data):
        if data:
            if data[attribute_objectId]:
                self.get_Object(data[attribute_objectId])
            self.set_attribute_name(data[attribute_name])
            if data[attribute_state] and int(data[attribute_state]) == -1:
                self.set_attribute_state(data[attribute_state])
                self.delete_Category()
            return True
        return None

    def delete_Category(self):
        self.set_attribute_state(STATE_DELETE)
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

