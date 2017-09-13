from ClassLibrary.BaseClass.Object import *


class WebPageConfigure(Object):
    def __init__(self):
        super(WebPageConfigure, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_code(self):
        if self.instance:
            return self.instance.get(attribute_code)
        return None

    def get_attribute_url(self):
        if self.instance:
            return self.instance.get(attribute_url)
        return None

    def set_attribute_code(self, value):
        if self.instance and value:
            self.instance.set(attribute_code, value)
            self.save_instance()
            return True
        return None

    def set_attribute_url(self, value):
        if self.instance and value:
            self.instance.set(attribute_url, value)
            self.save_instance()
            return True
        return None

    def create_WebPageConfigure(self, data):
        self.create_Object()
        self.set_attribute_name(data[attribute_name])
        self.set_attribute_code(data[attribute_code])
        self.set_attribute_url(data[attribute_url])
        return True

    def output_WebPageConfigure(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_url: self.get_attribute_url(),
                attribute_name: self.get_attribute_name(),
                attribute_code: self.get_attribute_code(),
            }
            return data

    def output_WebPageConfigure_All(self):
        web = Base.queryAllInstance(self.className, attribute_objectId, limit=100)
        if web:
            returnList = []
            for foo in web:
                webTmp = WebPageConfigure()
                webTmp.set_instance(foo)
                returnList.append(webTmp.output_WebPageConfigure())
            return returnList
        return []

    def clear_all_WebPageConfigure(self):
        self.instance = self.instance
        web = Base.queryAllInstance(self.className, attribute_objectId, limit=100)
        if web:
            returnList = []
            for foo in web:
                webTmp = WebPageConfigure()
                webTmp.set_instance(foo)
                webTmp.destroy_Object()
            return returnList
        return []
