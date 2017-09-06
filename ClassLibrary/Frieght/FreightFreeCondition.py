from ClassLibrary.BaseClass.Object import *


class FreightFreeCondition(Object):
    def __init__(self):
        super(FreightFreeCondition, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_cityList(self):
        query = Base.get_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_cityList)
        if query:
            result_list = []
            for foo in query:
                result_list.append(foo)
            return result_list
        return []

    def output_FreightFreeCondition(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_option: self.get_attribute(attribute_option),
                attribute_freeNum: self.get_attribute(attribute_freeNum),
                attribute_freeSum: self.get_attribute(attribute_freeSum),
                attribute_cityList: self.get_attribute_cityList()
            }
            return data
        return None
