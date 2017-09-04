from ClassLibrary.BaseClass.Object import *


class LogisticsInfo( Object ):
    def __init__(self, shipperCode=None, shipperName=None, logisticsCode=None, traces=None, state=None):
        super(LogisticsInfo, self).__init__()
        self.className = self.__class__.__name__
        self.shipperCode = shipperCode
        self.shipperName = shipperName
        self.logisticsCode = logisticsCode
        self.traces = traces
        self.state = state

    def update_logistics(self, logisticInfo):
        if self.instance:
            self.instance.set(attribute_shipperCode, logisticInfo.shipperCode)
            self.instance.set(attribute_shipperName, logisticInfo.shipperName)
            self.instance.set(attribute_logisticCode, logisticInfo.logisticsCode)
            self.instance.set(attribute_state, STATE_OK)
            self.__save_instance__()
            return True
        return None

    def get_attribute_shipperCode(self):
        if self.instance:
            return self.instance.get(attribute_shipperCode)
        return None

    def get_attribute_shipperName(self):
        if self.instance:
            return self.instance.get(attribute_shipperName)
        return None

    def get_attribute_logisticCode(self):
        if self.instance:
            return self.instance.get(attribute_logisticCode)
        return None

    def get_attribute_traces(self):
        if self.instance:
            return self.instance.get(attribute_traces)
        return None

    def get_attribute_createdAt(self):
        if self.instance:
            return Base.change_timeZone(self.instance.get(attribute_createdAt))
        return None

    def output_Logistic(self):
        if self.instance:
            A = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_state: self.get_attribute_state(),
                attribute_createdAt: self.get_attribute_createdAt(),
                attribute_logisticCode: self.get_attribute_logisticCode(),
                attribute_shipperName: self.get_attribute_shipperName(),
                attribute_shipperCode: self.get_attribute_shipperCode(),
                attribute_traces: self.get_attribute_traces(),
            }
            return A
        return None

    def set_attribute_shipperCode(self, value):
        if self.instance:
            self.instance.set(attribute_shipperCode, value)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_shipperName(self, value):
        if self.instance:
            self.instance.set(attribute_shipperName, value)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_logisticsCode(self, value):
        if self.instance:
            self.instance.set(attribute_logisticCode, value)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_traces(self, value):
        if self.instance:
            self.instance.set(attribute_traces, value)
            if self.__save_instance__():
                return True
        return None

    def create_LogisticInfo(self, data):
        self.create_Object()
        self.set_attribute_state(data[attribute_state])
        self.set_attribute_shipperCode(data[attribute_shipperCode])
        self.set_attribute_shipperName(data[attribute_shipperName])
        self.set_attribute_logisticsCode(data[attribute_logisticCode])
        self.set_attribute_traces(data[attribute_traces])