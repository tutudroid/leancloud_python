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
import json
from ClassLibrary.BaseClass.Object import *
from ClassLibrary.ProductClass.ProductDetailDescription import ProductDetailDescription
from ClassLibrary.ProductClass.Product import Product
from ClassLibrary.CategoryClass.StoreCategory import StoreCategory
from ClassLibrary.CategoryClass.SaleCategory import SaleCategory
from ClassLibrary.ImageClass.ProductImage import ProductImage
from ClassLibrary.ProductClass.ProductService import ProductService
from ClassLibrary.ProductClass.ProductComment import ProductComment
from ClassLibrary.Frieght.FreightModel import FreightModel
from ClassLibrary.ProductClass.ShopProduct import ShopProduct


class ProductGroupBase(Object):
    def __init__(self):
        super(ProductGroupBase, self).__init__()
        self.className = self.className
        self.productName = Class_Name_Product
        print(self.className)

    def set_attribute_propertyOption(self, pro):
        if self.instance and pro:
            self.instance.set(attribute_propertyOption, pro)
            self.__save_instance__()
            return True
        return None

    def get_attribute_propertyOption(self):
        if self.instance:
            property1 = self.instance.get(attribute_propertyOption)
            propertyOption = {}
            if property1:
                for foo in property1:
                    if foo['PropertyOption']:
                        foo.update({'length': len(foo['PropertyOption'])})
                    if foo['PropertyId'] == '0':
                        propertyOption.update({'first': foo})
                    if foo['PropertyId'] == '1':
                        propertyOption.update({'second': foo})
                    if foo['PropertyId'] == '2':
                        propertyOption.update({'third': foo})
            print(propertyOption)
            return propertyOption
        return None

    def get_attribute_productService(self):
        if self.instance:
            productService = Base.get_relation_data(self.instance.get(attribute_objectId), self.className, attribute_productService)
            productServiceList = []
            if productService:
                for foo in productService:
                    service = ProductService()
                    productServiceList.append(service.__output_Object__(foo))
                return productServiceList
        return None

    def set_attribute_productService(self, productService):
        if self.instance and productService:
            relation = self.instance.relation(attribute_productService)
            relation.add(productService)
            self.__save_instance__()
            return True
        return None

    def get_attribute_ip(self):
        if self.instance and self.instance.get(attribute_ip):
            foo = Base.queryInstanceThroughId(Class_Name_IPTable, self.instance.get(attribute_ip).id)
            if foo:
                return self.__output_Object__(foo)
        return None

    def set_attribute_ip(self, ip):
        if self.instance and ip:
            self.instance.set(attribute_ip, ip)
            if self.__save_instance__():
                return True
        return None

    def get_attribute_dispatchPlace(self):
        if self.instance:
            dispatchPlace = self.instance.get(attribute_dispatchPlace)
            if dispatchPlace:
                address = {
                    'province': dispatchPlace.split(' ')[0],
                    'city': dispatchPlace.split(' ')[1],
                    'district': dispatchPlace.split(' ')[2]
                }
                return address
            return []
        return None

    def get_attribute_product(self):
        if self.instance:
            productList = Base.get_relation_data(self.instance.get(attribute_objectId), self.className, attribute_product)
            if productList:
                product = []
                for foo in productList:
                    tmp = Product()
                    tmp.set_instance(foo)
                    product.append(tmp.output_Product())
                return product
        return None

    def remove_attribute_product(self, product):
        if product and self.instance:
            relation = self.instance.relation(attribute_product)
            relation.remove(product)
            self.__save_instance__()

    def get_attribute_storeCategory(self):
        if self.instance and self.instance.get(attribute_storeCategory):
            storeInstance3 = StoreCategory(Class_Name_StoreCategoryThird)
            if storeInstance3.get_StoreCategoryThird(self.get_attribute_Object_Id(attribute_storeCategory)):
                storeInstance2 = StoreCategory(Class_Name_StoreCategorySecond)
                if storeInstance2.get_StoreCategorySecond(storeInstance3.get_attribute_Object_Id(attribute_storeCategorySecond)):
                    storeInstance1 = StoreCategory(Class_Name_StoreCategoryFirst)
                    if storeInstance1.get_StoreCategoryFirst(storeInstance2.get_attribute_Object_Id(attribute_storeCategoryFirst)):
                        A = {
                            attribute_storeCategoryFirst: storeInstance1.output_StoreCategory(),
                            attribute_storeCategorySecond: storeInstance2.output_StoreCategory(),
                            attribute_storeCategoryThird: storeInstance3.output_StoreCategory(),
                        }
                        return A
                    else:
                        self.__print_msg__error( 'storeCategoryFirst is not existed' )
                else:
                    self.__print_msg__error( 'storeCategorySecond is not existed' )
            else:
                self.__print_msg__error( 'storeCategoryThird is not existed' )
        self.__print_msg__error( 'parameter is null' )
        return None

    def get_attribute_saleCategory(self):
        if self.instance:
            saleList2 = Base.get_relation_data(self.instance.get(attribute_objectId), self.className, attribute_saleCategory)
            if saleList2:
                returnList = []
                for sale2 in saleList2:
                    saleTmp2 = SaleCategory(Class_Name_SaleCategorySecond)
                    saleTmp2.set_instance(sale2)

                    saleTmp1 = SaleCategory(Class_Name_SaleCategoryFirst)
                    if saleTmp2.get_attribute_saleCategoryFirst() and saleTmp1.get_SaleCategoryFirst(saleTmp2.get_attribute_saleCategoryFirst().id):
                        A = {
                            attribute_saleCategoryFirst: saleTmp1.output_SaleCategory(),
                            attribute_saleCategorySecond: saleTmp2.output_SaleCategory()
                        }
                        returnList.append(A)
                if len(returnList) > 0:
                    return returnList[0]
        return None

    def set_attribute_product(self, product):
        if self.instance and product:
            relation = self.instance.relation(attribute_product)
            relation.add(product)
            if self.__save_instance__():
                return True
        return None

    def get_attribute_brand(self):
        if self.instance and self.instance.get(attribute_brand):
            brand = Base.queryInstanceThroughId(Class_Name_BrandTable, self.instance.get(attribute_brand).id)
            return self.__output_Object__(brand)
        return None

    def set_attribute_brand(self, brand):
        if self.instance and brand:
            self.instance.set(attribute_brand, brand)
            if self.__save_instance__():
                return True
        return None

    def get_attribute_mainImage(self):
        if self.instance:
            if self.instance.get(attribute_mainImage) and isinstance(self.instance.get(attribute_mainImage), ISINSTANCE_FILE):
                return self.instance.get(attribute_mainImage).url
        return None

    def get_attribute_imageList(self):
        if self.instance:
            imageList = Base.get_relation_data(self.instance.get(attribute_objectId), self.className, attribute_imageList)
            if imageList:
                resultList = []
                for foo in imageList:
                    if isinstance(foo.get(attribute_imageFile), ISINSTANCE_FILE):
                        image = {
                            attribute_imageFile: foo.get(attribute_imageFile).url,
                            attribute_objectId: foo.get(attribute_objectId),
                        }
                        resultList.append(image)
                return resultList
        return None

    def get_attribute_collectionUser(self):
        if self.instance:
            return self.instance.get(attribute_collectionUser)
        return None

    def get_attribute_comment(self, attribute, value, skip=None, limit=None):
        if self.instance and attribute:
            tmpList = Base.get_relation_data_and_attribute(self.instance.get(attribute_objectId), self.className, attribute_comment,
                                                           attribute, value,
                                                           skip, limit)
            if tmpList:
                returnList = []
                for foo in tmpList:
                    comment = ProductComment()
                    comment.set_instance(foo)
                    returnList.append(comment.output_ProductComment())
                return returnList
        return None

    def get_attribute_comment_count(self, attribute, value):
        if self.instance and attribute:
            count = Base.count_relation_data_and_attribute(self.instance.get(attribute_objectId), self.className, attribute_comment,
                                                           attribute, value)
            return count
        return None

    def get_attribute_briefDescription(self):
        if self.instance:
            return self.instance.get(attribute_briefDescription)
        return None

    def get_attribute_detailDescription(self):
        if self.instance:
            imageList = Base.get_relation_data(self.instance.get(attribute_objectId), self.className, attribute_detailDescription)
            if imageList:
                image = []
                for foo in imageList:
                    description = ProductDetailDescription()
                    description.set_instance(foo)
                    image.append(description.output_productDetailDescription())
                return image
        return None

    def get_attribute_shop(self):
        if self.instance:
            return self.instance.get(attribute_shop)
        return None

    def get_attribute_saleCount(self):
        if self.instance:
            return self.instance.get(attribute_saleCount)
        return None

    def get_attribute_price(self):
        if self.instance:
            return self.instance.get(attribute_price)
        return None

    def get_attribute_spec(self):
        if self.instance:
            return self.instance.get(attribute_spec)
        return

    def set_attribute_spec(self, spec):
        if self.instance and spec:
            self.instance.set(attribute_spec, spec)
            return True
        return

    def set_attribute_dispatchPlace(self, spec):
        if self.instance and spec:
            self.instance.set(attribute_dispatchPlace, spec)
            return True
        return

    def get_attribute_freightModel(self):
        if self.instance and self.instance.get(attribute_freightModel):
            freight = FreightModel()
            freight.get_Object(self.instance.get(attribute_freightModel).id)
            return freight.output_FreightModel()
        return None

    def set_attribute_storeCategory(self, storeCategory):
        if self.instance and storeCategory:
            self.instance.set(attribute_storeCategory, storeCategory)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_saleCategory(self, saleCategory):
        if self.instance and saleCategory:
            relationSaleCategory = self.instance.relation(attribute_saleCategory)
            relationSaleCategory.add(saleCategory)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_imageList(self, image):
        if self.instance and image:
            relation = self.instance.relation(attribute_imageList)
            relation.add(image)
            if self.__save_instance__():
                return True
        return False

    def set_attribute_mainImage(self, mainImage):
        if self.instance and mainImage:
            self.instance.set(attribute_mainImage, mainImage)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_briefDescription(self, detail):
        if self.instance and detail:
            self.instance.set(attribute_briefDescription, detail)
            self.__save_instance__()

    def set_attribute_detailDescription(self, detail):
        if self.instance and detail:
            relation = self.instance.relation(attribute_detailDescription)
            relation.add(detail)
            self.__save_instance__()
            return True
        return None

    def set_attribute_shop(self, shopInstance):
        if self.instance and shopInstance:
            self.instance.set(attribute_shop, shopInstance)
            if self.__save_instance__():
                product = self.get_attribute_relation(attribute_product)
                if product:
                    self.__print_msg__error( product )
                    for foo in product:
                        product = Product()
                        product.get_Object(foo.get(attribute_objectId))
                        product.set_attribute_value(attribute_shop, shopInstance)
                return True
        return None

    def set_attribute_price(self, price):
        if self.instance:
            self.instance.set(attribute_price, int(price))
            self.__save_instance__()
            return True
        return None

    def set_attribute_comment(self, value):
        if self.instance and value:
            relation = self.instance.relation(attribute_comment)
            relation.add(value)
            self.__save_instance__()
            return True
        return None

    def output_ProductGroup(self):
        # 用于编辑商品时的输出
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_uniqueId: self.get_attribute_uniqueId(),
                attribute_propertyOption: self.get_attribute_propertyOption(),
                attribute_name: self.get_attribute_name(),
                attribute_productService: self.get_attribute_productService(),
                attribute_ip: self.get_attribute_ip(),
                attribute_product: self.get_attribute_product(),
                attribute_brand: self.get_attribute_brand(),
                attribute_saleCategory: self.get_attribute_saleCategory(),
                attribute_storeCategory: self.get_attribute_storeCategory(),
                attribute_mainImage: self.get_attribute_mainImage(),
                attribute_imageList: self.get_attribute_imageList(),
                attribute_comment: self.get_attribute_comment(attribute_state, STATE_OK, 1, 10),
                attribute_briefDescription: self.get_attribute_briefDescription(),
                attribute_detailDescription: self.get_attribute_detailDescription(),
                attribute_shop: self.get_attribute_Object_Id(attribute_shop),
                attribute_saleCount: self.get_attribute_saleCount(),
                attribute_price: self.get_attribute_price(),
                attribute_spec: self.get_attribute_spec(),
                attribute_freightModel: self.get_attribute_freightModel(),
                attribute_state: self.get_attribute_state(),
                attribute_collectionUser: self.get_attribute_collectionUser(),
                attribute_dispatchPlace: self.get_attribute_dispatchPlace(),
                attribute_commentCount: self.get_attribute_comment_count(attribute_state, STATE_OK)
            }
            return data
        return None

    def output_ProductGroup_Simple(self):
        # 用于编辑商品时的输出
        if self.instance:
            A = {
                attribute_uniqueId: self.instance.get(attribute_uniqueId),
                attribute_state: self.instance.get(attribute_state),
                attribute_objectId: self.instance.get(attribute_objectId),
                attribute_name: self.instance.get(attribute_name),
                attribute_briefDescription: self.instance.get(attribute_briefDescription),
                attribute_propertyOption: self.instance.get(attribute_propertyOption),
                attribute_mainImage: self.instance.get(attribute_mainImage),
                attribute_saleCount: self.instance.get(attribute_saleCount),
            }
            return A
        return None

    def update_attribute_price(self):
        if self.instance:
            productList = self.get_attribute_product()
            price = None
            if productList:
                for foo in productList:
                    if not price or price > float(foo[attribute_price]):
                        price = float(foo[attribute_price])
                if price is not None:
                    self.set_attribute_price(price)

    def destroy_ProductGroup(self):
        if self.instance:
            shopObjectId = self.get_attribute_Object_Id(attribute_shop)
            objectId = self.instance.get(attribute_objectId)
            Base.destroy_relation_imageList(objectId, self.className,
                                            attribute_imageList, Class_Name_ProductImage)
            Base.destroy_relation(objectId, self.className,
                                  attribute_product, self.productName)
            Base.destroy_relation(objectId, self.className,
                                  attribute_detailDescription, Class_Name_ProductDetailDescription)
            # if self.instance.get(attribute_mainImage):
            #    self.instance.get(attribute_mainImage).destroy()
            self.destroy_Object()
            return shopObjectId
        return None

    def delete_ProductGroup(self):
        if self.instance:
            self.delete_Object()


    def create_ProductGroup(self, data):
        state = STATE_SHELF_ON
        # 首先保存一份类实例
        self.create_Object()
        # 写入商品的静态信息
        self.set_attribute_name(data[attribute_name])
        self.set_attribute_briefDescription(data[attribute_briefDescription])
        self.set_attribute_spec(data[attribute_spec])
        self.set_attribute_propertyOption(json.loads(data[attribute_propertyOption]))
        self.set_attribute_dispatchPlace(data[attribute_dispatchPlace])
        # 写入富文本信息，由于商品详情文件太大，无法使用一个字段进行保存，故将该字段已文件的形式保存，在显示时，通过ajax请求
        # 获得文件内容，并将文件内容进行显示
        #        if not Base.set_file(productGroup, attribute_detailDescription, data[attribute_detailDescription]):
        #            state = STATE_NO_FINISH
        if data[attribute_detailDescription]:
            for pic in data[attribute_detailDescription]:
                productDetail = ProductDetailDescription()
                detailDescription = productDetail.create_Object()
                imageFile = Base.save_image(pic)
                if productDetail.set_attribute_imageFile(imageFile):
                    productDetail.set_attribute_height_and_width()
                    self.set_attribute_detailDescription(detailDescription)
                else:
                    state = STATE_NO_FINISH


        storeCategory = StoreCategory(Class_Name_StoreCategoryThird)
        store = storeCategory.get_Object(data[attribute_storeCategory])

        if not self.set_attribute_storeCategory(store):
            Base.sys_log_info( 'save storeCategory failed' )
            state = STATE_NO_FINISH

        if self.className == Class_Name_ProductGroup and not storeCategory.set_attribute_productGroup(self.instance):
            state = STATE_NO_FINISH

        if data[attribute_saleCategory]:
            for foo in data[attribute_saleCategory]:
                # 将销售关系写入到商品类中
                saleCategory = SaleCategory(Class_Name_SaleCategorySecond)
                sale = saleCategory.get_Object(foo)
                self.set_attribute_saleCategory(sale)
                # 将商品组写入到对应的销售关系中
                if not self.set_attribute_saleCategory(sale):
                    Base.sys_log_info( 'save saleCategory failed' )
                    state = STATE_NO_FINISH
                if self.className == Class_Name_ProductGroup and not saleCategory.set_attribute_productGroup(self.instance):
                    state = STATE_NO_FINISH
        else:
            state = STATE_NO_FINISH

        # 写入主图片
        if data[attribute_mainImage]:
            productImage = ProductImage()
            image = productImage.create_Image(data[attribute_mainImage])
            if productImage.set_attribute_imageFile(productImage.get_imageFile()):
                self.set_attribute_imageList(image)
                self.set_attribute_mainImage(productImage.get_imageFile())
            else:
                Base.sys_log_info( 'save mainImage failed' )
                state = STATE_NO_FINISH

        # 获得写入的图片列表
        # 创建关系，每个图片单独保存，一起写入会出错
        if data[attribute_imageList]:
            for pic in data[attribute_imageList]:
                productImage = ProductImage()
                image = productImage.create_Image(pic)
                if productImage.set_attribute_imageFile(productImage.get_imageFile()):
                    self.set_attribute_imageList(image)
                else:
                    Base.sys_log_info( 'save imageList failed' )
                    state = STATE_NO_FINISH

        # 写入商品服务信息
        if data[attribute_productService]:
            for foo in data[attribute_productService]:
                productService = ProductService().get_Object(foo)
                if productService:
                    self.set_attribute_productService(productService)
                else:
                    state = STATE_NO_FINISH
        else:
            state = STATE_NO_FINISH

        # 创建商品
        if data[attribute_product]:
            for foo in json.loads(data[attribute_product]):
                if self.productName == Class_Name_Product:
                    product = Product()
                else:
                    product = ShopProduct()
                product.create_Product(foo, self.instance, data[attribute_productMainImage])
                if not self.set_attribute_product(product.instance):
                    Base.sys_log_info( 'save product failed' )
                    state = STATE_NO_FINISH

        # 设置商品组状态
        if self.__save_instance__():
            if state == STATE_SHELF_ON:
                return self.instance
        Base.sys_log_info( 'productGroup save failed' )
        # 删除保存失败的对象
        self.destroy_ProductGroup()
        return None

    def update_ProductGroup(self, data):
        if data and self.instance:
            productGroup = self.instance
            # 上传商品的静态信息
            if data[attribute_name] and self.get_attribute_name() != data[attribute_name]:
                self.set_attribute_name(data[attribute_name])
            if data[attribute_briefDescription] and self.get_attribute_briefDescription() != data[attribute_briefDescription]:
                self.set_attribute_briefDescription(data[attribute_briefDescription])
            if data[attribute_spec] and self.get_attribute_spec() != data[attribute_spec]:
                self.set_attribute_spec(data[attribute_spec])
            if data[attribute_propertyOption]:
                propertyOption = data[attribute_propertyOption].replace("'", "\"")
                propertyOption = json.loads(propertyOption)
                if self.get_attribute_propertyOption() != propertyOption:
                    self.set_attribute_propertyOption(propertyOption)
            """
            更新detailDescription
            """
            # 删除一些旧的图片
            if data['delete_detailDescription']:
                for foo in data['delete_detailDescription']:
                    detailDescription = ProductDetailDescription().get_Object(foo)
                    if detailDescription:
                        if detailDescription.get(attribute_imageFile):
                            detailDescription.get(attribute_imageFile).destroy()
                        detailDescription.destroy()

            if data[attribute_detailDescription]:
                for pic in data[attribute_detailDescription]:
                    productDetail = ProductDetailDescription()
                    detailDescription = productDetail.create_Object()
                    imageFile = Base.save_image(pic)
                    if productDetail.set_attribute_imageFile(imageFile):
                        productDetail.set_attribute_height_and_width()
                        self.set_attribute_detailDescription(detailDescription)

            if data[attribute_storeCategory]:
                if self.className == Class_Name_ProductGroup:
                    oldStoreCategory = StoreCategory()
                    if oldStoreCategory.get_StoreCategoryThird(self.get_attribute_Object_Id(attribute_storeCategory)):
                        oldStoreCategory.remove_attribute_productGroup(self.get_instance())

                storeCategory = StoreCategory(Class_Name_StoreCategoryThird)
                store = storeCategory.get_Object(data[attribute_storeCategory])
                if not self.set_attribute_storeCategory(store):
                    Base.sys_log_info('save storeCategory failed')
                if self.className == Class_Name_ProductGroup and not storeCategory.set_attribute_productGroup(self.instance):
                    pass
            """
            更新销售分类
            """
            # 增加新的关系
            if data[attribute_saleCategory]:
                # 清除旧的关系，增加新的关系
                if self.className == Class_Name_ProductGroup:
                    oldSaleCategory = self.get_attribute_relation(attribute_saleCategory)
                    if oldSaleCategory:
                        for foo in oldSaleCategory:
                            saleCategorySecond = SaleCategory()
                            if saleCategorySecond.get_SaleCategorySecond(foo.get(attribute_objectId)):
                                saleCategorySecond.remove_attribute_productGroup(self.get_instance())
                                self.remove_attribute_relation(attribute_saleCategory, saleCategorySecond.get_instance())
                        self.__save_instance__()

                for foo in data[attribute_saleCategory]:
                    # 将销售关系写入到商品类中
                    saleCategory = SaleCategory(Class_Name_SaleCategorySecond)
                    sale = saleCategory.get_Object(foo)
                    self.set_attribute_saleCategory(sale)
                    # 将商品组写入到对应的销售关系中
                    if not self.set_attribute_saleCategory(sale):
                        Base.sys_log_info('save saleCategory failed')
                    if self.className == Class_Name_ProductGroup and not saleCategory.set_attribute_productGroup(self.instance):
                        pass
            """
            更新主图片
            """
            # 写入列表中的图片
            # 获得图片类

            # 获得写入的图片列表
            # 写入主图片
            if data[attribute_mainImage]:
                # 预留删除旧的主图片
                mainImage = productGroup.get(attribute_mainImage)
                if mainImage:
                    productImage = ProductImage()
                    productImage.get_ProductImage(mainImage)
                    productImage.destroy_Object()
                mainImage.destroy()

                #  写入主图片
                productImage = ProductImage()
                image = productImage.create_Image(data[attribute_mainImage])
                if productImage.set_attribute_imageFile(productImage.get_imageFile()):
                    self.set_attribute_imageList(image)
                    self.set_attribute_mainImage(productImage.get_imageFile())
                else:
                    Base.sys_log_info( 'save mainImage failed' )
            """
            更新图片列表
            """
            # 删除一些旧的图片
            if data['delete_imageList']:
                for foo in data['delete_imageList']:
                    productImage = ProductImage().get_Object(foo)
                    if productImage and productImage.get(attribute_imageFile):
                        productImage.get(attribute_imageFile).destroy()
                        productImage.destroy()


            if data[attribute_imageList]:
                for pic in data[attribute_imageList]:
                    productImage = ProductImage()
                    image = productImage.create_Image(pic)
                    if productImage.set_attribute_imageFile(productImage.get_imageFile()):
                        self.set_attribute_imageList(image)
                    else:
                        Base.sys_log_info('save imageList failed')


            # 删除旧的商品服务信息
            oldProductService = self.get_attribute_relation(attribute_productService)
            if oldProductService:
                for foo in oldProductService:
                    productService = Base.queryInstanceThroughId(Class_Name_ProductService, foo.get(attribute_objectId))
                    self.remove_attribute_relation(attribute_productService, productService)

            # 写入商品服务信息
            if data[attribute_productService]:
                for foo in data[attribute_productService]:
                    productService = ProductService().get_Object(foo)
                    if productService:
                        self.set_attribute_productService(productService)

            # 删除商品
            if data['delete_product']:
                for foo in data['delete_product']:
                    productInstance = Product()
                    product = productInstance.get_Object(foo)
                    productInstance.delete_Product(productGroup)
                    self.remove_attribute_product(product)

            # 更新商品或者创建新的商品
            if data[attribute_product]:
                for foo in json.loads(data[attribute_product]):
                    if self.productName == Class_Name_Product:
                        product = Product()
                    else:
                        product = ShopProduct()
                    if foo[attribute_objectId]:
                        product.get_Object(foo[attribute_objectId])
                        product.update_Product(foo, data['product_mainImage'])
                        self.update_attribute_price()
                    else:
                        product.create_Product(foo, self.instance, data[attribute_productMainImage])
                        if not self.set_attribute_product(product.instance):
                            Base.sys_log_info('save product failed')
        else:
            Base.sys_log_info('objectId is null')

    def input_ProductGroup(self, request):
        self.instance = self.instance
        specification = []
        for foo in range(1, 15):
            spec = request.POST.get('specification_'+str(foo), '')
            specText = request.POST.get('specification_Text_'+str(foo), '')
            if spec and specText:
                A = {
                    'SpecName': spec,
                    'SpecContent': specText
                }
                specification.append(A)
        product = {
            attribute_spec: specification,
            attribute_propertyOption: request.POST.get(attribute_propertyOption, ''),
            attribute_name: request.POST.get(attribute_name, ''),
            attribute_mainImage: request.FILES.get(attribute_mainImage, ''),
            attribute_imageList: request.FILES.getlist(attribute_imageList, ''),
            attribute_briefDescription: request.POST.get(attribute_briefDescription, ''),
            attribute_detailDescription: request.FILES.getlist(attribute_detailDescription, ''),
            attribute_productService: request.POST.getlist(attribute_productService, []),
            attribute_storeCategory: request.POST.get(attribute_storeCategory, ''),
            attribute_saleCategory: request.POST.getlist(attribute_saleCategory, []),
            attribute_dispatchPlace: request.POST.get( attribute_province, '' ) + ' ' + request.POST.get( attribute_city, '' ) + ' ' + request.POST.get( attribute_district, '' ),
            attribute_product: request.POST.get(attribute_product, ''),
            attribute_productMainImage: request.FILES.getlist(attribute_productMainImage, ''),
            attribute_delete_imageList: request.POST.getlist(attribute_delete_imageList, []),
            attribute_delte_product: request.POST.getlist(attribute_delte_product, []),
            attribute_delete_detailDescription: request.POST.getlist(attribute_delete_detailDescription, []),
        }
        return product


