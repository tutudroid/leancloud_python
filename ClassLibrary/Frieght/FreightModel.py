from ClassLibrary.BaseClass.Object import *
from ClassLibrary.Frieght.FreightFreeCondition import FreightFreeCondition
from ClassLibrary.Frieght.SpecialAreaFreight import SpecialAreaFreight


class FreightModel(Object):
    def __init__(self):
        super(FreightModel, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_specialCities(self):
        query = Base.get_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_specialCities)
        if query:
            result_list = []
            for foo in query:
                freight = SpecialAreaFreight()
                freight.set_instance(foo)
                result_list.append(freight.output_SpecialAreaFreight())
            return result_list
        return []

    def get_attribute_freeConditionList(self):
        query = Base.get_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_freeConditionList)
        if query:
            result_list = []
            for foo in query:
                freight = FreightFreeCondition()
                freight.set_instance(foo)
                result_list.append(freight.output_FreightFreeCondition())
            return result_list
        return []

    def output_FreightModel(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute(attribute_objectId),
                attribute_isFreightFree: self.get_attribute(attribute_isFreightFree),
                attribute_shippingAddress: self.get_attribute(attribute_shippingAddress),
                attribute_startNum: self.get_attribute(attribute_startNum),
                attribute_startCost: self.get_attribute(attribute_startCost),
                attribute_addNum: self.get_attribute(attribute_addNum),
                attribute_addCost: self.get_attribute(attribute_addCost),
                attribute_specialCities: self.get_attribute_specialCities(),
                attribute_freeConditionList: self.get_attribute_freeConditionList(),

                # simple
                attribute_name: self.get_attribute(attribute_name),
                attribute_freight: self.get_attribute(attribute_freight),
            }
            return data
        return None

    def input_Freight(self, request):
        self.instance = self.instance
        data = {
            attribute_objectId: request.POST.get(attribute_objectId, ''),
            attribute_name: request.POST.get(attribute_name, ''),
            attribute_isFreightFree: request.POST.get(attribute_isFreightFree, ''),
            attribute_freight: request.POST.get(attribute_freight, ''),
            attribute_state: request.POST.get(attribute_state, '')
        }
        return data

    def update_Freight(self, data):
        if data[attribute_objectId]:
            self.get_Object(data[attribute_objectId])
        else:
            self.create_Object()
        self.set_attribute_value(attribute_name, data[attribute_name])
        self.set_attribute_value(attribute_isFreightFree, data[attribute_isFreightFree])
        self.set_attribute_value(attribute_freight, data[attribute_freight])
        if int(data[attribute_state]) == -1:
            self.destroy_Object()
