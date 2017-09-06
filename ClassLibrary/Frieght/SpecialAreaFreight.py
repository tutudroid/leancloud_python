from ClassLibrary.BaseClass.Object import *


class SpecialAreaFreight(Object):
    def __init__(self):
        super(SpecialAreaFreight, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_cityList(self):
        query = Base.get_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_cityList)
        if query:
            result_list = []
            for foo in query:
                result_list.append(foo)
            return result_list
        return []

    def output_SpecialAreaFreight(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_startNum: self.get_attribute(attribute_startNum),
                attribute_startCost: self.get_attribute(attribute_startCost),
                attribute_addNum: self.get_attribute(attribute_addNum),
                attribute_addCost: self.get_attribute(attribute_addCost),
                attribute_cityList: self.get_attribute_cityList()
            }
            return data
        return None

