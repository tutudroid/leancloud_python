from ClassLibrary.ProductClass.Product import Product


class ShopProduct(Product):
    def __init__(self):
        super(ShopProduct, self).__init__()
        self.className = self.__class__.__name__
