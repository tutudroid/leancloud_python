from ClassLibrary.CategoryClass.SaleCategory import SaleCategory


class SaleCategorySecond(SaleCategory):

    def __init__(self):
        super(SaleCategorySecond, self).__init__()
        self.className = self.__class__.__name__
        print(self.className)

    def output_SaleCategorySecond(self):
        if self.instance:
            return self.output_SaleCategory()
        return None

    def create_SaleCategorySecond(self, data, first):
        self.create_SaleCategory(data)
        self.set_attribute_value( attribute_saleCategoryFirst, first )
