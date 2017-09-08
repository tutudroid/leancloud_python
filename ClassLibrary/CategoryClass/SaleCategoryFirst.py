from ClassLibrary.BaseClass.Object import *
from ClassLibrary.CategoryClass.SaleCategory import SaleCategory
from ClassLibrary.CategoryClass.SaleCategorySecond import SaleCategorySecond



class SaleCategoryFirst(SaleCategory):

    def __init__(self):
        super(SaleCategoryFirst, self).__init__()
        self.className = self.__class__.__name__
        print(self.className)

    def get_attribute_saleCategorySecond(self):
        if self.instance:
            sale = Base.get_relation_data_and_attribute(self.instance.get(attribute_objectId), Class_Name_SaleCategoryFirst, attribute_saleCategorySecond, attribute_state, STATE_OK, 1, limit=100)
            if sale:
                returnList = []
                for foo in sale:
                    second = SaleCategorySecond()
                    second.set_instance(foo)
                    returnList.append(second.output_SaleCategory())
                return returnList
        return None

    def output_SaleCategoryFirst(self):
        if self.instance:
            data = self.output_SaleCategory()
            data.update({attribute_saleCategorySecond: self.get_attribute_saleCategorySecond()})
            return data
        return None

    def get_Category_Recommend(self):
        """
        获得销售分类表
        :return: 
        """
        self.instance = self.instance
        saleCategoryFirst = Base.queryInstanceAttribute1_Attribute2(Class_Name_SaleCategoryFirst, attribute_state, STATE_OK, attribute_categoryType, TYPE_RECOMMEND)
        if saleCategoryFirst:
            print(saleCategoryFirst)
            saleCategoryList = []
            for first in saleCategoryFirst:
                secondList = []
                for second in Base.get_relation_data_and_attribute_and_sort_uniqueId(first.get(attribute_objectId), Class_Name_SaleCategoryFirst, attribute_saleCategorySecond, attribute_state, STATE_OK):
                    B = {
                        attribute_objectId: second.get(attribute_objectId),
                        attribute_name: second.get(attribute_name),
                        attribute_briefDescription: second.get(attribute_briefDescription),
                        attribute_mainImage: second.get(attribute_mainImage),
                    }
                    secondList.append(B)
                A = {
                    attribute_objectId: first.get(attribute_objectId),
                    attribute_name: first.get(attribute_name),
                    attribute_briefDescription: first.get(attribute_briefDescription),
                    attribute_mainImage: first.get(attribute_mainImage),
                    'value': secondList,
                }
                saleCategoryList.append(A)
            return saleCategoryList
        return None

    def count_Category_Recommend(self):
        """
        获得销售分类表
        :return: 
        """
        self.instance = self.instance
        count = Base.queryInstanceAttribute1_Attribute2_Count(Class_Name_SaleCategoryFirst, attribute_state, STATE_OK, attribute_categoryType, TYPE_RECOMMEND)
        return count


def get_SaleCategory_All():
    """
    获得销售分类表
    :return: 
    """
    saleCategoryFirst = Base.queryInstanceAttribute_and_sort_uniqueId(Class_Name_SaleCategoryFirst, attribute_state, STATE_OK, 1, limit=100)
    if saleCategoryFirst:
        saleCategoryList = []
        for foo in saleCategoryFirst:
            first = SaleCategoryFirst()
            first.set_instance(foo)
            saleCategoryList.append(first.output_SaleCategoryFirst())
        return saleCategoryList
    return None
