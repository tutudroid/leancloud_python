from ClassLibrary.BaseClass.Object import *
from ClassLibrary.CategoryClass.StoreCategory import StoreCategory


class StoreCategorySecond(StoreCategory):

    def __init__(self):
        super(StoreCategorySecond, self).__init__()
        self.className = self.__class__.__name__
        print(self.className)


    def output_StoreCategorySecond(self):
        if self.instance:
            data = self.output_StoreCategory()
            data.update({attribute_storeCategoryThird: self.get_attribute_storeCategoryThird()})
            return data
        return None

    def delete_Category(self):
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
