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
from ClassLibrary.BaseClass.Attribute_Parameter import *
from ClassLibrary import Base
from ClassLibrary.ProductClass.ProductGroupBase import ProductGroupBase
from ClassLibrary.ProductClass.ShopProductGroup import ShopProductGroup
from ClassLibrary.ProductClass.ProductDetailDescription import ProductDetailDescription
from ClassLibrary.ProductClass.Product import copy_Shop_Product
from ClassLibrary.CategoryClass.StoreCategory import StoreCategory
from ClassLibrary.CategoryClass.SaleCategory import SaleCategory
from ClassLibrary.CategoryClass.StoreCategoryThird import StoreCategoryThird
from ClassLibrary.CategoryClass.SaleCategorySecond import SaleCategorySecond
from ClassLibrary.ImageClass.ProductImage import ProductImage
from ClassLibrary.ProductClass.ProductService import ProductService



class ProductGroup(ProductGroupBase):
    def __init__(self):
        super(ProductGroup, self).__init__()
        self.className = self.__class__.__name__
        # 用于区分商家商品和上线商品
        self.productName = Class_Name_Product


def copy_Shop_ProductGroup(shopProductGroup:ShopProductGroup):
        if shopProductGroup:
            state = STATE_SHELF_ON
            productGroup = ProductGroup()
            productGroup.create_Object()
            # 写入商品的静态信息
            productGroup.set_attribute_value(attribute_name, shopProductGroup.get_attribute(attribute_name))
            productGroup.set_attribute_value(attribute_shop, shopProductGroup.get_attribute(attribute_shop))

            productGroup.set_attribute_value(attribute_briefDescription, shopProductGroup.get_attribute(attribute_briefDescription))
            productGroup.set_attribute_value(attribute_propertyOption, shopProductGroup.get_attribute(attribute_propertyOption))
            productGroup.set_attribute_value(attribute_dispatchPlace, shopProductGroup.get_attribute(attribute_dispatchPlace))
            productGroup.set_attribute_value(attribute_price, float(shopProductGroup.get_attribute(attribute_price)))
            # roductGroup.set_attribute_value(attribute_saleCount, int(shopProductGroup.get_attribute(attribute_saleCount)))
            productGroup.set_attribute_value(attribute_spec, shopProductGroup.get_attribute(attribute_spec))
            productGroup.set_attribute_value(attribute_ip, shopProductGroup.get_attribute(attribute_ip))
            productGroup.set_attribute_value(attribute_brand, shopProductGroup.get_attribute(attribute_brand))
            productGroup.set_attribute_value(attribute_freightModel, shopProductGroup.get_attribute(attribute_freightModel))

            """
            保存商品详情
            """

            shopDetailDescription = shopProductGroup.get_attribute_relation(attribute_detailDescription)
            if shopDetailDescription:
                for foo in shopDetailDescription:
                    description = ProductDetailDescription()
                    description.create_Object()
                    description.copy_ProductDetailDescription(foo)
                    if not productGroup.add_attribute_relation(attribute_detailDescription, description.get_instance()):
                        Base.sys_log('save detailDescription failed')
                        state = STATE_NO_FINISH
            """
            保存主图片信息
            """
            image = ProductImage()
            image.create_Object()
            imageFile = Base.create_network_image(shopProductGroup.get_instance(), attribute_mainImage)
            image.set_attribute_value(attribute_imageFile, imageFile)
            productGroup.set_attribute_value(attribute_mainImage, imageFile)

            """
            保存图片列表信息
            """
            imageList = shopProductGroup.get_attribute_relation(attribute_imageList)
            if imageList:
                for pic in imageList:
                    image = ProductImage()
                    image.create_Object()
                    image.set_attribute_value(attribute_imageFile, pic.get(attribute_imageFile))
                    if not productGroup.add_attribute_relation(attribute_imageList, image.get_instance()):
                        Base.sys_log('save imageList failed')
                        state = STATE_NO_FINISH

            # 写入商品服务信息
            serviceList = shopProductGroup.get_attribute_relation(attribute_productService)
            if serviceList:
                for foo in serviceList:
                    productService = ProductService()
                    productService.get_Object(foo.id)
                    productGroup.add_attribute_relation(attribute_productService, productService.get_instance())

            # 保存库存信息
            productGroup.set_attribute_value(attribute_storeCategory, shopProductGroup.get_attribute(attribute_storeCategory))

            storeCategory = StoreCategoryThird()
            storeCategory.get_Object(shopProductGroup.get_attribute_Object_Id(attribute_storeCategory))
            if not storeCategory.add_attribute_relation(attribute_productGroup, productGroup.get_instance()):
                Base.sys_log('save storeCategory failed')
                state = STATE_NO_FINISH

            saleList = shopProductGroup.get_attribute_relation(attribute_saleCategory)
            if saleList:
                for foo in saleList:
                    # 将销售关系写入到商品类中
                    sale = SaleCategorySecond()
                    sale.get_Object(foo.id)
                    if not productGroup.add_attribute_relation(attribute_saleCategory, sale.get_instance()):
                        Base.sys_log('save saleCategory failed')
                        state = STATE_NO_FINISH
                    if not sale.add_attribute_relation(attribute_productGroup, productGroup.get_instance()):
                        Base.sys_log('save saleCategory failed')
                        state = STATE_NO_FINISH

            # 保存商品信息
            shopProductList = shopProductGroup.get_attribute_relation(attribute_product)
            if shopProductList:
                for shopProduct in shopProductList:
                    product = copy_Shop_Product(shopProduct)
                    product.set_attribute_value(attribute_group, productGroup.get_instance())
                    if not productGroup.add_attribute_relation(attribute_product, product.get_instance()):
                        Base.sys_log('save product failed')
                        state = STATE_NO_FINISH

            # 设置商品组状态
            if state == STATE_SHELF_ON:
                shopProductGroup.destroy_ProductGroup()
                return productGroup
            else:
                # 清理数据
                productGroup.destroy_ProductGroup()
        Base.sys_log("shopProductGroup doesn't exist")
        return None
