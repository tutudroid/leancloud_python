from ClassLibrary.ImageClass.Image import *
from ClassLibrary.ProductClass.ProductService import *


class Table(ProductService, ImageBase):
    def __init__(self):
        super(Table, self).__init__()
        self.className = self.__class__.__name__

    def output_Table(self):
        if self.instance:
            data = {
                attribute_imageFile: self.get_attribute_imageFile(),
                attribute_objectId: self.get_attribute_objectId(),
                attribute_name: self.get_attribute_name(),
                attribute_briefDescription: self.get_attribute_briefDescription()
            }
            return data

    def input_Table(self, request):
        self.instance = self.instance
        data = {
            attribute_objectId: request.POST.get(attribute_objectId, ''),
            attribute_name: request.POST.get(attribute_name, ''),
            attribute_briefDescription: request.POST.get(attribute_briefDescription,''),
            attribute_imageFile: request.FILES.get(attribute_imageFile, ''),
        }
        return data

    def update_Table(self, data):
        if data[attribute_objectId]:
            self.instance = Base.queryInstanceThroughId(self.className, data[attribute_objectId])
        else:
            self.instance = self.create_Object()

        if data[attribute_name]:
            self.set_attribute_name(data[attribute_name])
        if data[attribute_briefDescription]:
            self.set_attribute_briefDescription(data[attribute_briefDescription])

        if data[attribute_imageFile]:
            imageFile = Base.save_image_data(data[attribute_imageFile])
            self.set_attribute_imageFile(imageFile)

    def create_Table(self, data):
        if data:
            self.create_Object()
            self.set_attribute_name(data[attribute_name])
            self.set_attribute_briefDescription(data[attribute_briefDescription])
            imageFile = self.save_ImageFile(data[attribute_imageFile])
            self.set_attribute_imageFile(imageFile)