from ClassLibrary.ImageClass.Image import *


class ProductCommentImage(ImageBase):
    def __init__(self):
        super(ProductCommentImage, self).__init__()
        self.className = self.__class__.__name__


    def get_ProductImage(self, mainImage):
        productImage = Base.queryInstanceAttributeFirst(self.__class__.__name__, attribute_imageFile, mainImage)
        if productImage:
            self.instance = productImage
            return productImage
        return None
