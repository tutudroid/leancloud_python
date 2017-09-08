"""
create in 2017-8-25

function：
    基类
        每个类具有基本参数：uniqueId, objectId, state
        每个类的property方法：
            创建类
            获得类的实例
            获得类的属性
            修改类的属性
            删除类
            销毁类
        每个类的内部方法：
            __save_instance__()
            __print_msg__()
    派生类
"""
from ClassLibrary.BaseClass.Object import *


class Product(Object):
    def __init__(self):
        super(Product, self).__init__()
        self.className = self.__class__.__name__
        self.group = None
        self.shop = None
        self.stockCount = None
        self.style = None
        self.styleBackup = None
        self.comment = None
        self.limitCount = None
        self.mainImage = None
        self.price = None
        self.saleCount = None

    def get_attribute_group(self):
        if self.instance:
            return self.instance.get(attribute_group)
        return None

    def get_attribute_shop(self):
        if self.instance:
            return self.instance.get(attribute_shop)
        return None

    def get_attribute_stockCount(self):
        if self.instance:
            return self.instance.get(attribute_stockCount)
        return None

    def get_attribute_style(self):
        if self.instance:
            style = self.instance.get(attribute_style)
            data = {}
            if style:
                for foo in style:
                    if foo['PropertyId'] == '0':
                        data.update({'firstId': foo['OptionId']})
                    if foo['PropertyId'] == '1':
                        data.update({'secondId': foo['OptionId']})
                    if foo['PropertyId'] == '2':
                        data.update({'thirdId': foo['OptionId']})
            return data
        return None

    def get_attribute_styleBackup(self):
        if self.instance:
            return self.instance.get(attribute_styleBackUp)
        return None

    def get_attribute_comment(self, attribute, value, skip=None, limit=None):
        if self.instance:
            tmpList = Base.get_relation_data_and_attribute(self.get_attribute_objectId(), self.__class__.__name__, attribute_comment, attribute, value,
                                                           skip, limit)
            Base.sys_log(tmpList)
            return tmpList
        return None

    def get_attribute_comment_count(self, attribute, value):
        if self.instance and attribute:
            count = Base.count_relation_data_and_attribute(self.get_attribute_objectId(), self.__class__.__name__, attribute_comment, attribute, value)
            return count
        return None

    def get_attribute_limitCount(self):
        if self.instance:
            return self.instance.get(attribute_limitCount)
        return None

    def get_attribute_mainImage(self):
        if self.instance:
            if isinstance(self.instance.get(attribute_mainImage), ISINSTANCE_FILE):
                return self.instance.get(attribute_mainImage).url
        return None

    def get_attribute_price(self):
        if self.instance:
            return self.instance.get(attribute_price)
        return None

    def get_attribute_saleCount(self):
        if self.instance:
            return self.instance.get(attribute_saleCount)
        return None


    def destroy_Product(self):
        if self.instance:
            if self.instance.get(attribute_mainImage):
                self.instance.get(attribute_mainImage).destroy()
            self.instance.destroy()

    def set_attribute_group(self, productGroup):
        if productGroup and self.instance:
            self.instance.set(attribute_group, productGroup)
            if self.__save_instance__():
                return True
        return None


    def set_attribute_mainImage(self, mainImage):
        if mainImage and self.instance:
            self.instance.set(attribute_mainImage, mainImage)
            self.__save_instance__()

    def set_attribute_price(self, price):
        if price and self.instance:
            self.instance.set(attribute_price, float(price))
            self.__save_instance__()

    def set_attribute_stockCount(self, stockCount):
        if stockCount and self.instance:
            self.instance.set(attribute_stockCount, int(stockCount))
            self.__save_instance__()

    def set_attribute_limitCount(self, limitCount):
        if limitCount and self.instance:
            self.instance.set(attribute_limitCount, int(limitCount))
            self.__save_instance__()

    def set_attribute_style(self, style):
        if style and self.instance:
            self.instance.set(attribute_style, style)
            self.__save_instance__()


    def delete_Product(self, productGroup):
        """
        从商品组中删除一件商品，修改商品的state位为1。
        :param productGroup: 
        :return: 
        """
        if self.instance and productGroup:
            self.instance.set(attribute_state, STATE_DELETE)
            propertyOption = productGroup.get(attribute_propertyOption)
            style = self.instance.get(attribute_style)
            styleBackup = []
            if style and propertyOption:
                for foo in style:
                    for goo in propertyOption:
                        if foo['PropertyId'] == goo['PropertyId']:
                            if goo['PropertyOption']:
                                for koo in goo['PropertyOption']:
                                    if foo['OptionId'] == koo['OptionId']:
                                        A = {
                                            'PropertyName': goo['PropertyName'],
                                            'OptionName': koo['OptionName']
                                        }
                                        styleBackup.append(A)
            self.instance.set(attribute_styleBackUp, styleBackup)
            if self.__save_instance__():
                return True
            else:
                Base.sys_log('product delete failed')
        Base.sys_log('product or productGroup is null')
        return None

    def update_Product(self, data, imageFileList):
        if self.instance and data:
            if data[attribute_price] and float(self.instance.get(attribute_price)) != float(data[attribute_price]):
                self.instance.set(attribute_price, float(data[attribute_price]))
                self.__save_instance__()
            if data[attribute_stockCount] and int(self.instance.get(attribute_stockCount)) != int(data[attribute_stockCount]):
                self.instance.set(attribute_stockCount, int(data[attribute_stockCount]))
                self.instance.set(attribute_limitCount, int(data[attribute_stockCount]))
                self.__save_instance__()
            if data[attribute_style] and self.instance.get(attribute_style) != data[attribute_style]:
                self.instance.set(attribute_style, data[attribute_style])
                self.__save_instance__()
            # 写入主图片
            if data[attribute_mainImage]:
                for mainImage in imageFileList:
                    stringSeries = str(mainImage)
                    # 检查是否有新的图片
                    if stringSeries == data[attribute_mainImage].split('\\')[-1]:
                        if self.instance.get(attribute_mainImage):
                            # 检查是否有旧的图片存在，如果存在，则销毁
                            oldMainImage = self.instance.get(attribute_mainImage)
                            oldMainImage.destroy()
                        # 写入新的图片
                        if Base.set_image(self.instance, mainImage, attribute_mainImage) is False:
                            Base.sys_log('product save mainImage failed')
            return self.instance
        return None


    def find_Product(self, productGroup, style):
        if productGroup and style:
            product = Base.queryInstanceAttribute1_Attribute2(self.__class__.__name__, attribute_group, productGroup, attribute_style, style)
            if product:
                return product
        return None


    def create_Product(self, data, group, imageFileList):
        if data and group:
            if self.find_Product(group, data[attribute_style]):
                Base.sys_log('this product has existed')
                return None
            print(data)
            if self.create_Object():
                self.set_attribute_group(group)
                self.set_attribute_price(float(data[attribute_price]))
                self.set_attribute_stockCount(int(data[attribute_stockCount]))
                self.set_attribute_limitCount(int(data[attribute_stockCount]))
                self.set_attribute_style(data[attribute_style])
                # 写入主图片
                if data[attribute_mainImage]:
                    for mainImage in imageFileList:
                        stringSeries = str(mainImage)
                        if stringSeries == data[attribute_mainImage].split('\\')[-1]:
                            print('success')
                            if not Base.set_image(self.instance, mainImage, attribute_mainImage):
                                Base.sys_log('product save mainImage failed')
                                self.instance.destroy_Product()
                                return None
                else:
                    if group.get(attribute_mainImage) and isinstance(group.get(attribute_mainImage), ISINSTANCE_FILE):
                        img_url = group.get(attribute_mainImage).url
                        if img_url:
                            avatar = leancloud.File.create_with_url('default_image.jpg', img_url)
                            avatar.save()
                            self.set_attribute_mainImage(avatar)
                price = group.get(attribute_price)
                if not price or float(price) > float(data[attribute_price]):
                    group.set(attribute_price, float(data[attribute_price]))
                return self.instance
        return None


    def output_Product(self):
        # 用于编辑商品时的输出
        if self.instance:
            data = {
                attribute_style: self.get_attribute_style(),
                attribute_objectId: self.get_attribute_objectId(),
                attribute_mainImage: self.get_attribute_mainImage(),
                attribute_price: self.get_attribute_price(),
                attribute_stockCount: self.get_attribute_stockCount(),
                attribute_saleCount: self.get_attribute_saleCount(),
            }
            return data


def copy_Shop_Product(shopProduct):
    if shopProduct:
        product = Product()
        product.create_Object()
        product.set_attribute_value(attribute_price, float(shopProduct.get(attribute_price)))
        product.set_attribute_value(attribute_stockCount, int(shopProduct.get(attribute_stockCount)))
        product.set_attribute_value(attribute_limitCount, int(shopProduct.get(attribute_limitCount)))
        product.set_attribute_value(attribute_style, shopProduct.get(attribute_style))
        product.set_attribute_value(attribute_shop, shopProduct.get(attribute_shop))

        if shopProduct.get(attribute_mainImage):
            imageFile = Base.create_network_image(shopProduct, attribute_mainImage)
            product.set_attribute_value(attribute_mainImage, imageFile)
        return product
    return None
