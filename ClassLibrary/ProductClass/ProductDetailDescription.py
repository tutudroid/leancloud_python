# import io
import urllib.request
from PIL import Image

from ClassLibrary.ImageClass.Image import *

attribute_imageHeight = 'imageHeight'
attribute_imageWidth = 'imageWidth'


class ProductDetailDescription(ImageBase):
    def __init__(self):
        super(ProductDetailDescription, self).__init__()
        self.className = self.__class__.__name__
        self.imageHeight = None
        self.imageWidth = None

    def get_imageHeight(self):
        if self.instance:
            return self.instance.get(attribute_imageHeight)

    def get_imageWidth(self):
        if self.instance:
            return self.instance.get(attribute_imageWidth)


    def set_attribute_height_and_width(self):
        if self.instance:
            url = self.get_attribute_imageFile()
            if url:
                #file = urllib.request.urlopen(url)
                #tmpIm = io.BytesIO(file.read())
                #im = Image.open(tmpIm)
                #self.instance.set(attribute_imageWidth, int(im.size[0]))
                #self.instance.set(attribute_imageHeight, int(im.size[1]))
                self.__save_instance__()

    def output_productDetailDescription(self):
        if self.instance:
            data = {
                attribute_imageFile: self.get_attribute_imageFile(),
                attribute_objectId: self.get_attribute_objectId(),
                attribute_imageWidth: self.get_imageWidth(),
                attribute_imageHeight: self.get_imageHeight(),
            }
            return data

    def copy_ProductDetailDescription(self, detail):
        self.set_attribute_value(attribute_imageFile, detail.get(attribute_imageFile))
        self.set_attribute_value(attribute_imageWidth, detail.get(attribute_imageWidth))
        self.set_attribute_value(attribute_imageHeight, detail.get(attribute_imageHeight))



def output_productDetailDescription(detail):
    if detail:
        data = {
            attribute_imageFile: detail.get(attribute_imageFile).url,
            attribute_objectId: detail.get(attribute_objectId),
            attribute_imageWidth: detail.get(attribute_imageWidth),
            attribute_imageHeight: detail.get(attribute_imageHeight)
        }
        return data
