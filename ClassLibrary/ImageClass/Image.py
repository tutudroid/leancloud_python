from ClassLibrary.BaseClass.Object import *


class ImageBase(Object):
    def __init__(self):
        super(ImageBase, self).__init__()
        self.className = self.__class__.__name__

    def output_Image(self):
        if self.instance and isinstance(self.instance.get(attribute_imageFile), ISINSTANCE_FILE):
            data = {
                attribute_imageFile: self.instance.get(attribute_imageFile).url,
            }
            return data

    def get_imageFile(self):
        if self.instance:
            return self.instance.get(attribute_imageFile)

    def get_attribute_imageFile(self):
        if self.instance and isinstance(self.instance.get(attribute_imageFile), ISINSTANCE_FILE):
            return self.instance.get(attribute_imageFile).url

    def set_attribute_imageFile(self, imageFile):
        if self.instance and imageFile:
            self.instance.set(attribute_imageFile, imageFile)
            if self.save_instance():
                return True
        return None

    def save_ImageFile(self, data):
        if data:
            self.instance = self.instance
            return Base.save_image(data)

    def create_Image(self, data):
        if data:
            imageFile = self.save_ImageFile(data)
            INSTANCE = leancloud.Object.extend(self.className)
            instance = INSTANCE()
            instance.set(attribute_state, self.state)
            instance.set(attribute_imageFile, imageFile)
            self.instance = instance
            return self.save_instance()
        return None
