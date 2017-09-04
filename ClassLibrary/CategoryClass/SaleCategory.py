from ClassLibrary.BaseClass.Object import *


class SaleCategory(Object):

    def __init__(self, name=None):
        super(SaleCategory, self).__init__()
        if name:
            self.className = name
        else:
            self.className = self.__class__.__name__
        self.saleCategoryFirst = None
        self.saleCategorySecond = None
        self.mainImage = None
        self.productGroup = None
        self.briefDescription = None
        self.categoryType = None
        self.saleCategoryRecommend = None
        print(self.className)

    def get_SaleCategoryFirst(self, objectId):
        if objectId:
            first = Base.queryInstanceThroughId(Class_Name_SaleCategoryFirst, objectId)
            self.instance = first
            return first
        return None

    def check_SaleCategoryFirst(self, name):
        if name:
            first = Base.queryInstanceAttribute1_Attribute2_First(Class_Name_SaleCategoryFirst, attribute_name, name, attribute_state, 0)
            self.instance = first
            if first:
                return first
        return False

    def check_SaleCategorySecond(self, name, first):
        if name and first:
            second = Base.queryInstance_A1_A2_A3_First(Class_Name_SaleCategorySecond, attribute_name, name, attribute_saleCategoryFirst, first, attribute_state, 0)
            self.instance = second
            if second:
                return second
        return False


    def get_SaleCategorySecond(self, objectId):
        if objectId:
            second = Base.queryInstanceThroughId(Class_Name_SaleCategorySecond, objectId)
            self.instance = second
            return second
        return None


    def get_SaleCategoryRecommend(self, objectId):
        self.instance = self.instance
        if objectId:
            recommend = Base.queryInstanceThroughId(Class_Name_SaleCategoryRecommend, objectId)
            self.instance = recommend
            return recommend
        return None

    def get_attribute_briefDescription(self):
        if self.instance:
            return self.instance.get(attribute_briefDescription)
        return None

    def get_attribute_saleCategoryFirst(self):
        if self.instance:
            return self.instance.get(attribute_saleCategoryFirst)
        return None

    def set_attribute_saleCategoryFirst(self, first):
        if self.instance and first:
            self.instance.set(attribute_saleCategoryFirst, first)
            self.__save_instance__()
            return True
        return None

    def set_attribute_saleCategorySecond(self, second):
        if self.instance and second:
            relation = self.instance.relation(attribute_saleCategorySecond)
            relation.add(second)
            self.__save_instance__()
            return True
        return None

    def get_attribute_categoryType(self):
        if self.instance:
            return self.instance.get(attribute_categoryType)
        return None

    def set_attribute_uniqueId(self, uniqueId):
        if self.instance and uniqueId:
            self.instance.set(attribute_uniqueId, int(uniqueId))
            if self.__save_instance__():
                return True
        return None


    def set_attribute_briefDescription(self, briefDescription):
        if self.instance and briefDescription:
            self.instance.set(attribute_briefDescription, briefDescription)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_categoryType(self, categoryType):
        if self.instance:
            self.instance.set(attribute_categoryType, int(categoryType))
            if self.__save_instance__():
                return True
        return None

    def remove_attribute_productGroup(self, productGroup):
        if self.instance and productGroup:
            relation = self.instance.relation(attribute_productGroup)
            relation.remove(productGroup)
            self.__save_instance__()
            return True
        Base.sys_log('sale or productGroup is null')
        return None

    def remove_attribute_saleCategorySecond(self, saleSecond):
        if self.instance and saleSecond:
            relation = self.instance.relation(attribute_productGroup)
            relation.remove(saleSecond)
            self.__save_instance__()
            return True
        return None

    def set_attribute_productGroup(self, productGroup):
        if self.instance and productGroup:
            # 将商品组写入到对应的销售关系中
            relationProductGroup = self.instance.relation(attribute_productGroup)
            relationProductGroup.add(productGroup)
            if self.__save_instance__():
                return True
        return None

    def get_first_sale_category(self):
        """
        得到第一级状态为0的所有销售分类
        :return: 
        """
        self.instance = self.instance
        first = Base.queryInstanceAttribute_and_sort_uniqueId(Class_Name_SaleCategoryFirst, attribute_state, STATE_OK)
        if first:
            firstSale = []
            for foo in first:
                sale = SaleCategory().set_instance(foo)
                A = {
                    attribute_objectId: sale.get_attribute_objectId(),
                    attribute_name: sale.get_attribute_name(),
                    attribute_uniqueId: sale.get_attribute_uniqueId(),
                    attribute_categoryType: sale.get_attribute_categoryType(),
                }
                firstSale.append(A)
            return firstSale
        return None

    def set_attribute_saleCategoryRecommend(self, mainImage, productGroup):
        if self.instance and mainImage and productGroup:
            SaleRecommend = leancloud.Object.extend(Class_Name_SaleCategoryRecommend)
            saleRecommend = SaleRecommend()
            saleRecommend.set(attribute_productGroup, productGroup)
            Base.set_image(saleRecommend, mainImage, attribute_mainImage)
            Base.save_data(saleRecommend)
            relation = self.instance.relation(attribute_saleCategoryRecommend)
            relation.add(saleRecommend)
            self.__save_instance__()

            CategoryImage = leancloud.Object.extend(Class_Name_SaleCategoryImage)
            categoryImage = CategoryImage()
            categoryImage.set(attribute_imageFile, saleRecommend.get(attribute_mainImage))
            Base.save_data(categoryImage)
        else:
            Base.sys_log('parameter is null')


    def get_attribute_saleCategoryRecommend(self):
        saleCategoryRecommend = Base.get_relation_data_and_attribute(self.instance.get(attribute_objectId), Class_Name_SaleCategoryFirst, attribute_saleCategoryRecommend, attribute_state, STATE_OK)
        if saleCategoryRecommend:
            saleRecommend = []
            for foo in saleCategoryRecommend:
                sale = SaleCategory().set_instance(foo)
                saleRecommend.append(sale.output_Class_Name_SaleCategoryRecommend())
            return saleRecommend
        Base.sys_log('saleCategoryRecommend is null')
        return None

    def get_attribute_saleCategorySecond(self):
        if self.instance:
            sale = Base.get_relation_data_and_attribute(self.instance.get(attribute_objectId), Class_Name_SaleCategoryFirst, attribute_saleCategorySecond, attribute_state, STATE_OK)
            if sale:
                returnList = []
                for foo in sale:
                    second = SaleCategory(Class_Name_SaleCategorySecond)
                    second.set_instance(foo)
                    returnList.append(second.output_SaleCategorySecond())
                return returnList
        return None


    def get_second_sale_category(self):
        """
        通过第一级的objectId获得第二级的销售分类
        :return: 
        """
        if self.instance:
            second = Base.get_relation_data_and_attribute_and_sort_uniqueId(self.instance.get(attribute_objectId), Class_Name_SaleCategoryFirst, attribute_saleCategorySecond, attribute_state, STATE_OK)
            if second:
                secondSale = []
                for foo in second:
                    sale = SaleCategory(Class_Name_SaleCategorySecond)
                    sale.set_instance(foo)
                    A = {
                        attribute_objectId: sale.get_attribute_objectId(),
                        attribute_name: sale.get_attribute_name(),
                        attribute_uniqueId: sale.get_attribute_uniqueId(),
                    }
                    secondSale.append(A)
                return secondSale
            else:
                Base.sys_log('second sale is null')
        else:
            Base.sys_log('first sale object id is null')
        return None

    def create_SaleCategory(self, data, first=None):
        if data:
            if attribute_objectId in data and data[attribute_objectId]:
                self.get_Object(data[attribute_objectId])
            else:
                self.create_Object()
            self.set_attribute_name(data[attribute_name])
            self.set_attribute_briefDescription(data[attribute_briefDescription])
            mainImage = Base.save_image(data[attribute_mainImage])
            self.set_attribute_mainImage(mainImage)
            if first:
                self.set_attribute_value(attribute_saleCategoryFirst, first)
            return True
        return None

    def update_SaleCategory(self, data):
        if data:
            if data[attribute_objectId]:
                self.get_Object(data[attribute_objectId])
            self.set_attribute_name(data[attribute_name])
            self.set_attribute_briefDescription(data[attribute_briefDescription])
            mainImage = Base.save_image(data[attribute_mainImage])
            self.set_attribute_mainImage(mainImage)
            if data[attribute_state]:
                self.set_attribute_state(data[attribute_state])
                self.delete_SaleCategory()
            return True
        return None

    def delete_SaleCategory(self):
        if self.className == Class_Name_SaleCategorySecond:
            saleFirst = SaleCategory(Class_Name_SaleCategoryFirst)
            firstInstance = self.get_attribute_saleCategoryFirst()
            if firstInstance:
                saleFirst.get_Object(firstInstance.id)
                saleFirst.remove_attribute_saleCategorySecond(self.instance)
                return True
        return None

    def output_SaleCategorySecond(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_name: self.get_attribute_name(),
                attribute_uniqueId: self.get_attribute_uniqueId(),
                attribute_briefDescription: self.get_attribute_briefDescription(),
                attribute_mainImage: self.get_attribute_mainImage(),
            }
            return data
        return None

    def output_SaleCategoryFirst(self):
        if self.instance:
            data = self.output_SaleCategorySecond()
            data.update({attribute_saleCategorySecond: self.get_attribute_saleCategorySecond()})
            return data
        return None

    def get_Category_Recommend(self):
        """
        获得销售分类表
        :return: 
        """
        self.instance = self.instance
        saleCategoryFirst = Base.queryInstanceAttribute1_Attribute2(Class_Name_SaleCategoryFirst, attribute_state, STATE_OK, attribute_categoryType, TYPE_RECOMMEND)
        if saleCategoryFirst:
            print(saleCategoryFirst)
            saleCategoryList = []
            for first in saleCategoryFirst:
                secondList = []
                for second in Base.get_relation_data_and_attribute_and_sort_uniqueId(first.get(attribute_objectId), Class_Name_SaleCategoryFirst, attribute_saleCategorySecond, attribute_state, STATE_OK):
                    B = {
                        attribute_objectId: second.get(attribute_objectId),
                        attribute_name: second.get(attribute_name),
                        attribute_briefDescription: second.get(attribute_briefDescription),
                        attribute_mainImage: second.get(attribute_mainImage),
                    }
                    secondList.append(B)
                A = {
                    attribute_objectId: first.get(attribute_objectId),
                    attribute_name: first.get(attribute_name),
                    attribute_briefDescription: first.get(attribute_briefDescription),
                    attribute_mainImage: first.get(attribute_mainImage),
                    'value': secondList,
                }
                saleCategoryList.append(A)
            return saleCategoryList
        return None

    def count_Category_Recommend(self):
        """
        获得销售分类表
        :return: 
        """
        self.instance = self.instance
        count = Base.queryInstanceAttribute1_Attribute2_Count(Class_Name_SaleCategoryFirst, attribute_state, STATE_OK, attribute_categoryType, TYPE_RECOMMEND)
        return count


    def get_SaleCategory_All(self):
        """
        获得销售分类表
        :return: 
        """
        self.instance = self.instance
        saleCategoryFirst = Base.queryInstanceAttribute_and_sort_uniqueId(Class_Name_SaleCategoryFirst, attribute_state, STATE_OK)
        if saleCategoryFirst:
            saleCategoryList = []
            for foo in saleCategoryFirst:
                first = SaleCategory(Class_Name_SaleCategoryFirst)
                first.set_instance(foo)
                saleCategoryList.append(first.output_SaleCategoryFirst())
            return saleCategoryList
        return None

    def input_SaleCategory(self, request):
        self.instance = self.instance
        data = {
            attribute_name: request.POST.get(attribute_name, ''),
            attribute_objectId: request.POST.get(attribute_objectId, ''),
            attribute_briefDescription: request.POST.get(attribute_briefDescription, ''),
            attribute_mainImage: request.FILES.get(attribute_mainImage, ''),
        }
        return data
