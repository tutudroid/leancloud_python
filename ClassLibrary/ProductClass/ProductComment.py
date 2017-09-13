from ClassLibrary.BaseClass.Object import *
from ClassLibrary.ImageClass.ProductCommentImage import ProductCommentImage

class ProductComment(Object):
    def __init__(self):
        super(ProductComment, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_user(self):
        if self.instance:
            return self.instance.get(attribute_user)
        return None

    def get_attribute_orderProduct(self):
        if self.instance:
            return self.instance.get(attribute_orderProduct)
        return None

    def get_attribute_priority(self):
        if self.instance:
            return self.instance.get(attribute_priority)
        return None

    def get_attribute_userAvatar(self):
        if self.instance and self.instance.get(attribute_userAvatar) and isinstance(self.instance.get(attribute_userAvatar), ISINSTANCE_FILE):
            return self.instance.get(attribute_userAvatar).url
        return None

    def get_attribute_userNickName(self):
        if self.instance:
            return self.instance.get(attribute_userNickName)
        return None

    def get_attribute_content(self):
        if self.instance:
            return self.instance.get(attribute_content)
        return None

    def get_attribute_productStyle(self):
        if self.instance:
            return self.instance.get(attribute_productStyle)
        return None

    def get_attribute_imageList(self):
        if self.instance:
            imageList = Base.get_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_imageList)
            if imageList:
                returnList = []
                for foo in imageList:
                    if isinstance(foo.get(attribute_imageFile), ISINSTANCE_FILE):
                        data = {
                            attribute_imageFile: foo.get(attribute_imageFile).url,
                        }
                        returnList.append(data)
                return returnList
        return None

    def output_ProductComment(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_priority: self.get_attribute_priority(),
                attribute_userAvatar: self.get_attribute_userAvatar(),
                attribute_userNickName: self.get_attribute_userNickName(),
                attribute_imageList: self.get_attribute_imageList(),
                attribute_content: self.get_attribute_content(),
                attribute_productStyle: self.get_attribute_productStyle(),
            }
            return data
        return None

    def set_attribute_priority(self, value):
        if self.instance:
            self.instance.set(attribute_priority, value)
            if self.save_instance():
                return True
        return None

    def set_attribute_userAvatar(self, value):
        if self.instance:
            self.instance.set(attribute_userAvatar, value)
            if self.save_instance():
                return True
        return None

    def set_attribute_userNickName(self, value):
        if self.instance:
            self.instance.set(attribute_userNickName, value)
            if self.save_instance():
                return True
        return None

    def set_attribute_content(self, value):
        if self.instance:
            self.instance.set(attribute_content, value)
            if self.save_instance():
                return True
        return None

    def set_attribute_productStyle(self, value):
        if self.instance:
            self.instance.set(attribute_productStyle, value)
            if self.save_instance():
                return True
        return None

    def set_attribute_imageList(self, value):
        if self.instance:
            relation = self.instance.relation(attribute_imageList)
            relation.add(value)
            if self.save_instance():
                return True
        return None


    def set_attribute_user(self, value):
        if self.instance:
            self.instance.set(attribute_user, value)
            if self.save_instance():
                return True
        return None

    def set_attribute_orderProduct(self, value):
        if self.instance:
            self.instance.set(attribute_orderProduct, value)
            if self.save_instance():
                return True
        return None

    def create_ProductComment(self, data):
        self.create_Object()
        self.set_attribute_userNickName(data[attribute_userNickName])
        self.set_attribute_content(data[attribute_content])
        self.set_attribute_productStyle(data[attribute_productStyle])
        self.set_attribute_priority(data[attribute_priority])
        if data[attribute_imageList]:
            for foo in data[attribute_imageList]:
                image = ProductCommentImage()
                image.create_Image(foo)
                self.set_attribute_imageList(image.get_instance())
