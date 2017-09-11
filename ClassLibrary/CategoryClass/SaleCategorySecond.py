from ClassLibrary.CategoryClass.SaleCategory import SaleCategory
from ClassLibrary.BaseClass.Attribute_Parameter import *
from ClassLibrary import Base


class SaleCategorySecond(SaleCategory):
    def __init__(self):
        super(SaleCategorySecond, self).__init__()
        self.className = self.__class__.__name__
        print(self.className)

    def output_SaleCategorySecond(self):
        if self.instance:
            return self.output_SaleCategory()
        return None

    def create_SaleCategorySecond(self, data, first):
        self.create_SaleCategory(data)
        self.set_attribute_value(attribute_saleCategoryFirst, first)

    def delete_SaleCategory(self):
        self.set_attribute_state(STATE_DELETE)
        saleFirst = SaleCategory(Class_Name_SaleCategoryFirst)
        firstInstance = self.get_attribute_saleCategoryFirst()
        if firstInstance:
            saleFirst.get_Object(firstInstance.id)
            saleFirst.remove_attribute_relation(attribute_saleCategorySecond, self.instance)
            return True
        return None

    def get_attribute_productGroup(self, page):
        if self.instance:
            tmpList = Base.get_relation_data(self.instance.get(attribute_objectId), Class_Name_SaleCategorySecond, attribute_productGroup, page)
            return tmpList
        return None

    def count_attribute_productGroup(self):
        if self.instance:
            count = Base.count_relation_data(self.instance.get(attribute_objectId), Class_Name_SaleCategorySecond, attribute_productGroup)
            return count
        return None