from ClassLibrary.BaseClass.Object import *
from ClassLibrary.CategoryClass.StoreCategory import StoreCategory


class StoreCategorySecond(StoreCategory):

    def __init__(self):
        super(StoreCategorySecond, self).__init__()
        self.className = self.__class__.__name__

    def output_StoreCategorySecond(self):
        if self.instance:
            data = self.output_StoreCategory()
            data.update({attribute_storeCategoryThird: self.get_attribute_storeCategoryThird()})
            return data
        return None

    def get_attribute_storeCategoryThird(self):
        if self.instance:
            store = Base.get_relation_data_and_attribute(self.instance.get(attribute_objectId), Class_Name_StoreCategorySecond, attribute_storeCategoryThird, attribute_state, STATE_OK, 1, limit=100)
            if store:
                returnList = []
                for foo in store:
                    third = StoreCategory(Class_Name_StoreCategoryThird)
                    third.set_instance(foo)
                    returnList.append(third.output_StoreCategory())
                print(returnList)
                return returnList
        return None

    def delete_Category(self):
        self.set_attribute_state(STATE_DELETE)
        First = StoreCategory(Class_Name_StoreCategoryFirst)
        firstInstance = self.get_attribute_storeCategoryFirst()
        if firstInstance:
            First.get_Object(firstInstance.id)
            First.remove_attribute_relation(attribute_storeCategorySecond, self.instance)
            return True

        return None

    def create_StoreCategorySecond(self, data, storeCategoryFirst):
        if data:
            self.create_StoreCategory(data)
            self.set_attribute_storeCategoryFirst(storeCategoryFirst)
            return True
        return None
