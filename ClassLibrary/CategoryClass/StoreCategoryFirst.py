from ClassLibrary.BaseClass.Object import *
from ClassLibrary.CategoryClass.StoreCategory import StoreCategory
from ClassLibrary.CategoryClass.StoreCategorySecond import StoreCategorySecond



class StoreCategoryFirst(StoreCategory):

    def __init__(self):
        super(StoreCategoryFirst, self).__init__()
        self.className = self.__class__.__name__
        print(self.className)

    def get_attribute_storeCategorySecond(self):
        if self.instance:
            store = Base.get_relation_data_and_attribute(self.instance.get(attribute_objectId), Class_Name_StoreCategoryFirst, attribute_storeCategorySecond, attribute_state, STATE_OK)
            if store:
                returnList = []
                for foo in store:
                    second = StoreCategorySecond()
                    second.set_instance(foo)
                    returnList.append(second.output_StoreCategorySecond())
                return returnList
        return None

    def output_StoreCategoryFirst(self):
        if self.instance:
            data = self.output_StoreCategory()
            data.update({attribute_storeCategorySecond: self.get_attribute_storeCategorySecond()})
            return data
        return None

    def create_StoreCategoryFirst(self, data):
        if data:
            self.create_StoreCategory(data)
            return True
        return None

    def delete_Category(self):
        return None
