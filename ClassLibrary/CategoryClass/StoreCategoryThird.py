from ClassLibrary.BaseClass.Object import *
from ClassLibrary.CategoryClass.StoreCategory import StoreCategory


class StoreCategoryThird(StoreCategory):

    def __init__(self):
        super(StoreCategoryThird, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_storeCategorySecond(self):
        if self.instance:
            return self.instance.get(attribute_storeCategorySecond)
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

    def delete_Category(self):
        self.set_attribute_state(STATE_DELETE)
        second = StoreCategory(Class_Name_StoreCategorySecond)
        secondInstance = self.instance.get(attribute_storeCategorySecond)
        if secondInstance:
            second.get_Object(secondInstance.id)
            second.remove_attribute_relation(attribute_storeCategoryThird, self.instance)
            return True
        return None

    def create_StoreCategoryThird(self, data, storeCategorySecond):
        if data and storeCategorySecond:
            self.create_StoreCategory(data)
            self.set_attribute_storeCategorySecond(storeCategorySecond)
            return True
        return None