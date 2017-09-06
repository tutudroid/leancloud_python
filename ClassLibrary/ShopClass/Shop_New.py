from ClassLibrary.BaseClass.Object import *
from ClassLibrary.OrderClass.AfterSaleServiceRecord import AfterSaleServiceRecord
from ClassLibrary.OrderClass.Order import Order
from ClassLibrary.ShopClass.SettleInUser import SettleInUser
from ClassLibrary.ShopClass.SettleInCompany import SettleInCompany
from ClassLibrary.ShopClass.SettleInApplication import SettleInApplication
from ClassLibrary.ProductClass.ProductGroup_New import ProductGroup
from ClassLibrary.ShopClass.BrandTable import BrandTable
from ClassLibrary.Frieght.FreightModel import FreightModel


class Shop(Object):
    def __init__(self):
        super(Shop, self).__init__()
        self.className = self.__class__.__name__
        self.productGroup = None
        self.shopProductGroup = None
        self.order = None
        self.address = None
        self.PROVINCE = None
        self.CITY = None
        self.DISTRICT = None
        self.user = None
        self.settleInUser = None
        self.settleInCompany = None
        self.phoneNumber = None
        self.mainImage = None
        self.shopType = None
        self.brand = None
        self.type = None
        self.freightModel = None
        self.afterSaleServiceRecord = None

    @staticmethod
    def __output_ProductGroup__(self):
        # 用于编辑商品时的输出
        if self:
            A = {
                attribute_uniqueId: self.get(attribute_uniqueId),
                attribute_state: self.get(attribute_state),
                attribute_objectId: self.get(attribute_objectId),
                attribute_name: self.get(attribute_name),
                attribute_briefDescription: self.get(attribute_briefDescription),
                attribute_propertyOption: self.get(attribute_propertyOption),
                attribute_mainImage: self.get(attribute_mainImage),
                attribute_saleCount: self.get(attribute_saleCount),
            }
            return A
        return None

    def get_Shop_All(self, page):
        self.instance = self.instance
        shopList = Base.queryInstanceAttribute(Class_Name_Shop, attribute_state, STATE_OK, page, QUERY_SKIP)
        if shopList:
            List = []
            for foo in shopList:
                shop = Shop()
                shop.set_instance(foo)
                List.append(shop.output_Shop())
            return List
        return None

    def count_Shop_All(self):
        self.instance = self.instance
        count = Base.queryInstanceAttributeCount(Class_Name_Shop, attribute_state, STATE_OK)
        return count

    def get_Shop_Audit_All(self, state, page):
        self.instance = self.instance
        settleInList = Base.queryInstanceAttribute(Class_Name_SettleInApplication, attribute_state, state, page)
        if settleInList:
            List = []
            for foo in settleInList:
                application = SettleInApplication()
                application.set_instance(foo)
                List.append(application.output_SettleInApplication())
            return List
        return None

    def count_Shop_Audit_All(self, state):
        self.instance = self.instance
        settleInList = Base.queryInstanceAttribute(Class_Name_SettleInApplication, attribute_state, state)
        if settleInList:
            List = []
            for foo in settleInList:
                application = SettleInApplication()
                application.set_instance(foo)
                List.append(application.output_SettleInApplication())
            return List
        return None

    def get_attribute_productGroup(self, state, page=1):
        if self.instance:
            tmpList = Base.get_relation_data_and_attribute(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_productGroup, attribute_state, int(state), page)
            if tmpList:
                returnList = []
                for foo in tmpList:
                    productGroup = ProductGroup()
                    productGroup.set_instance(foo)
                    returnList.append(productGroup.output_ProductGroup())
                return returnList
            else:
                self.__print_msg__('shop not found productGroup')
        return None

    def get_attribute_shopProductGroup(self, page=1):
        if self.instance:
            tmpList = Base.get_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_shopProductGroup, page)
            if tmpList:
                returnList = [self.__output_ProductGroup__(foo) for foo in tmpList]
                return returnList
        return None

    def get_attribute_order(self, state, page):
        if self.instance:
            if state == -1:
                tmpList = Base.get_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_order, page, QUERY_SKIP)
            else:
                tmpList = Base.get_relation_data_and_attribute(self.instance.get(attribute_objectId), Class_Name_Shop, attribute_order, attribute_orderSate, int(state), page, QUERY_SKIP)
            if tmpList:
                orderList = []
                for foo in tmpList:
                    order = Order()
                    order.set_instance(foo)
                    orderList.append(order.output_Order())
                return orderList
        return None

    def get_attribute_address(self):
        if self.instance:
            return self.instance.get(attribute_address)
        return None

    def get_attribute_province(self):
        if self.instance:
            return self.instance.get(attribute_PROVINCE)
        return None

    def get_attribute_city(self):
        if self.instance:
            return self.instance.get(attribute_CITY)
        return None

    def get_attribute_district(self):
        if self.instance:
            return self.instance.get(attribute_DISTRICT)
        return None

    def get_attribute_user(self):
        if self.instance:
            return self.instance.get(attribute_user)
        return None


    def get_attribute_settleInUser(self):
        if self.instance and self.instance.get(attribute_settleInUser):
            settleIn = SettleInUser()
            settleIn.get_Object(self.instance.get(attribute_settleInUser).id)
            return settleIn.output_SettleIn()
        return None

    def get_attribute_settleInCompany(self):
        if self.instance and self.instance.get(attribute_settleInCompany):
            settleIn = SettleInCompany()
            settleIn.get_Object(self.instance.get(attribute_settleInCompany).get(attribute_objectId))
            return settleIn.output_SettleIn()
        return None

    def get_attribute_phoneNumber(self):
        if self.instance:
            return self.instance.get(attribute_phoneNumber)
        return None

    def get_attribute_shopType(self):
        if self.instance:
            return self.instance.get(attribute_shopType)
        return None

    def get_attribute_brand(self):
        if self.instance:
            query = Base.get_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_brand)
            if query:
                result = []
                for foo in query:
                    brand = BrandTable()
                    brand.set_instance(foo)
                    result.append(brand.output_Table())
                return result
        return None

    def get_attribute_type(self):
        if self.instance:
            return self.instance.get(attribute_type)
        return None

    def get_attribute_freightModel(self):
        if self.instance:
            query = Base.get_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_freightModel)
            if query:
                result = []
                for foo in query:
                    freight = FreightModel()
                    freight.set_instance(foo)
                    result.append(freight.output_FreightModel())
                return result
        return None

    def get_attribute_mainImage(self):
        if self.instance and self.instance.get(attribute_mainImage):
            return self.instance.get(attribute_mainImage).url
        return None

    def get_attribute_afterSaleServiceRecord(self, state, page):
        if self.instance:
            if state == -1:
                tmpList = Base.get_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_afterSaleServiceRecord, page)
            else:
                tmpList = Base.get_relation_data_and_attribute(self.instance.get(attribute_objectId), Class_Name_Shop, attribute_afterSaleServiceRecord, attribute_state, state, page)
            if tmpList:
                returnList = []
                for foo in tmpList:
                    afterSale = AfterSaleServiceRecord()
                    afterSale.set_instance(foo)
                    returnList.append(afterSale.output_AfterSaleServiceRecord())
                return returnList
            self.__print_msg__('afterSale no found')
        return None

    def set_attribute_productGroup(self, productGroup):
        if self.instance and productGroup:
            relation = self.instance.relation(attribute_productGroup)
            relation.add(productGroup)
            if self.__save_instance__():
                return True
        return None

    def set_attribute_shopProductGroup(self, productGroup):
        if self.instance and productGroup:
            relation = self.instance.relation(attribute_shopProductGroup)
            relation.add(productGroup)
            self.__save_instance__()
            return True
        return None

    def set_attribute_address(self, value):
        if self.instance and value:
            self.instance.set(attribute_address, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_province(self, value):
        if self.instance and value:
            self.instance.set(attribute_PROVINCE, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_city(self, value):
        if self.instance and value:
            self.instance.set(attribute_CITY, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_district(self, value):
        if self.instance and value:
            self.instance.set(attribute_DISTRICT, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_user(self, value):
        if self.instance and value:
            self.instance.set(attribute_user, value)
            self.__save_instance__()
            return True
        return None


    def set_attribute_settleInUser(self, value):
        if self.instance and value:
            self.instance.set(attribute_settleInUser, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_settleInCompany(self, value):
        if self.instance and value:
            self.instance.set(attribute_settleInCompany, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_phoneNumber(self, value):
        if self.instance and value:
            self.instance.set(attribute_phoneNumber, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_shopType(self, value):
        if self.instance and value is not None:
            self.instance.set(attribute_shopType, int(value))
            self.__save_instance__()
            return True
        return None

    def set_attribute_brand(self, value):
        if self.instance and value:
            relation = self.instance.relation(attribute_brand)
            relation.add(value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_order(self, value):
        if self.instance and value:
            relation = self.instance.relation(attribute_order)
            relation.add(value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_afterSaleServiceRecord(self, value):
        if self.instance and value:
            relation = self.instance.relation(attribute_afterSaleServiceRecord)
            relation.add(value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_type(self, value):
        if self.instance and value:
            self.instance.set(attribute_type, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_freightModel(self, value):
        if self.instance and value:
            self.instance.set(attribute_freightModel, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_mainImage(self, value):
        if self.instance and value:
            self.instance.set(attribute_mainImage, value)
            self.__save_instance__()
            return True
        return None

    def count_attribute_productGroup(self, state=0):
        if self.instance:
            count = Base.count_relation_data_and_attribute(self.instance.get(attribute_objectId), Class_Name_Shop, attribute_productGroup, attribute_state, int(state))
            return count
        return None

    def count_attribute_shopProductGroup(self):
        if self.instance:
            count = Base.count_relation_data(self.instance.get(attribute_objectId), Class_Name_Shop, attribute_shopProductGroup)
            return count
        return None

    def count_attribute_afterSaleServiceRecord(self, state):
        if self.instance:
            if state == -1:
                count = Base.count_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_afterSaleServiceRecord)
            else:
                count = Base.count_relation_data_and_attribute(self.instance.get(attribute_objectId), Class_Name_Shop, attribute_afterSaleServiceRecord, attribute_state, int(state))
            return count
        return None

    def count_attribute_order(self, state):
        if self.instance:
            if state == -1:
                count = Base.count_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_order)
            else:
                count = Base.count_relation_data_and_attribute(self.instance.get(attribute_objectId), Class_Name_Shop, attribute_order, attribute_orderSate, int(state))
            return count
        return None

    def output_Shop(self):
        if self.instance:
            A = {
                attribute_uniqueId: self.get_attribute_uniqueId(),
                attribute_user: self.get_attribute_Object_Id(attribute_user),
                attribute_address: self.get_attribute_address(),
                attribute_PROVINCE: self.get_attribute_province(),
                attribute_CITY: self.get_attribute_city(),
                attribute_DISTRICT: self.get_attribute_district(),
                attribute_name: self.get_attribute_name(),
                attribute_state: self.get_attribute_state(),
                attribute_createdAt: self.get_attribute_createdAt(),
                attribute_objectId: self.get_attribute_objectId(),
                attribute_phoneNumber: self.get_attribute_phoneNumber(),
                attribute_brand: self.get_attribute_brand(),
                attribute_type: self.get_attribute_type(),
                attribute_freightModel: self.get_attribute_freightModel(),
                attribute_shopType: self.get_attribute_shopType(),
                attribute_settleInCompany: self.get_attribute_settleInCompany(),
                attribute_settleInUser: self.get_attribute_settleInUser(),
                # attribute_order: self.get_attribute_order(5, 1),
                # attribute_afterSaleServiceRecord: self.get_attribute_afterSaleServiceRecord(0, 1),
                # attribute_productGroup: self.get_attribute_productGroup(0, 1)
            }
            return A
        return None

    def get_shop_state(self, state, page):
        query = Base.queryInstanceAttribute(self.__class__.__name__, attribute_state, int(state), page)
        if query:
            settleInList = []
            for foo in query:
                shop = Shop()
                shop.set_instance(foo)
                settleInList.append(shop.output_Shop())
            return settleInList
        return []

    def count_shop_state(self, state):
        count = Base.queryInstanceAttributeCount(self.__class__.__name__, attribute_state, int(state))
        return count

    def create_Shop(self, data):
        self.create_Object()
        self.set_attribute_name(data[attribute_name])
        self.set_attribute_province(data[attribute_PROVINCE])
        self.set_attribute_city(data[attribute_CITY])
        self.set_attribute_district(data[attribute_DISTRICT])
        self.set_attribute_address(data[attribute_address])
        self.set_attribute_phoneNumber(data[attribute_phoneNumber])
        self.set_attribute_shopType(data[attribute_shopType])
        self.set_attribute_type(data[attribute_type])
        self.__print_msg__('create shop success')

    def input_Shop(self, request):
        self.instance = self.instance
        data = {
            attribute_name: request.POST.get(attribute_name, ''),
            attribute_PROVINCE: request.POST.get(attribute_PROVINCE, ''),
            attribute_CITY: request.POST.get(attribute_CITY, ''),
            attribute_DISTRICT: request.POST.get(attribute_DISTRICT, ''),
            attribute_address: request.POST.get(attribute_address, ''),
            attribute_objectId: request.POST.get(attribute_objectId, ''),
            attribute_phoneNumber: request.POST.get(attribute_phoneNumber, ''),
            attribute_brand: request.POST.get(attribute_brand, ''),
            attribute_username: request.POST.get(attribute_username, ''),
            attribute_password: request.POST.get(attribute_password, ''),
            attribute_passwordSure: request.POST.get(attribute_passwordSure, ''),
        }
        return data
