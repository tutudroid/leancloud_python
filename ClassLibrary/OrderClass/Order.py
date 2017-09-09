from ClassLibrary.BaseClass.Object import *
from ClassLibrary.OrderClass.LogisticsInfo import LogisticsInfo
from ClassLibrary.OrderClass.OrderProduct import OrderProduct
from ClassLibrary.ProductClass.ProductComment import ProductComment


class Order(Object):
    def __init__(self):
        super(Order, self).__init__()
        self.className = self.__class__.__name__
        self.finalPrice = None
        self.orderState = None
        self.receiverAddress = None
        self.receiverPhoneNumber = None
        self.receiverName = None
        self.shop = None
        self.user = None
        self.pingppOrderId = None
        self.freight = None
        self.deliveryTime = None
        self.createdAt = None
        self.logisticsInfo = None
        self.productComment = None
        self.orderProduct = None

    def get_attribute_pingppOrderId(self):
        if self.instance:
            return self.instance.get(attribute_pingppOrderId)
        return None

    def get_attribute_cancelTime(self):
        if self.instance:
            return Base.change_timeZone(self.instance.get(attribute_cancelTime))
        return None

    def get_attribute_paymentTime(self):
        if self.instance:
            return Base.change_timeZone(self.instance.get(attribute_paymentTime))
        return None

    def get_attribute_deliveryTime(self):
        if self.instance:
            return Base.change_timeZone(self.instance.get(attribute_deliveryTime))
        return None

    def get_attribute_refundTime(self):
        if self.instance:
            return Base.change_timeZone(self.instance.get(attribute_refundTime))
        return None

    def get_attribute_receiveTime(self):
        if self.instance:
            return Base.change_timeZone(self.instance.get(attribute_receiveTime))
        return None

    def get_attribute_finalPrice(self):
        if self.instance:
            return self.instance.get(attribute_finalPrice)
        return None

    def get_attribute_freight(self):
        if self.instance:
            return self.instance.get(attribute_freight)
        return None

    def get_attribute_orderState(self):
        if self.instance:
            return self.instance.get(attribute_orderSate)
        return None

    def get_attribute_receiverAddress(self):
        if self.instance:
            return self.instance.get(attribute_receiverAddress)
        return None

    def get_attribute_receiverPhoneNumber(self):
        if self.instance:
            return self.instance.get(attribute_receiverPhoneNumber)
        return None

    def get_attribute_receiverName(self):
        if self.instance:
            return self.instance.get(attribute_receiverName)
        return None

    def get_attribute_shop(self):
        if self.instance:
            return self.instance.get(attribute_shop)
        return None

    def get_attribute_user(self):
        if self.instance:
            return self.instance.get(attribute_user)
        return None

    def get_attribute_logisticInfo(self):
        if self.instance:
            logistic = self.instance.get(attribute_logisticInfo)
            if logistic:
                logisticInfo = LogisticsInfo()
                logisticInfo.get_Object(logistic.id)
                return logisticInfo.output_Logistic()
        return None

    def get_attribute_productComment(self):
        if self.instance:
            comment = Base.get_relation_data(self.instance.get(attribute_objectId), Class_Name_Order, attribute_productComment, 1, 100)
            resultComment = []
            if comment:
                for foo in comment:
                    productComment = ProductComment()
                    productComment.set_instance(foo)
                    resultComment.append(productComment.output_ProductComment())
                return resultComment
        return None

    def get_attribute_orderProduct(self):
        if self.instance:
            tmpList = Base.get_relation_data(self.instance.get(attribute_objectId), Class_Name_Order, attribute_orderProduct)
            if tmpList:
                returnList = []
                for foo in tmpList:
                    orderProduct = OrderProduct()
                    orderProduct.set_instance(foo)
                    returnList.append(orderProduct.output_OrderProduct())
                return returnList
        return None

    def set_attribute_orderState(self, orderState):
        if self.instance and 0 <= int(orderState) <= 7:
            self.instance.set(attribute_orderSate, int(orderState))
            self.__save_instance__()
            return True
        return None

    def set_attribute_orderProduct(self, value):
        if self.instance:
            relation = self.instance.relation(attribute_orderProduct)
            relation.add(value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_logisticInfo(self, value):
        if self.instance:
            self.instance.set(attribute_logisticInfo, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_shop(self, value):
        if self.instance:
            self.instance.set(attribute_shop, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_user(self, value):
        if self.instance:
            self.instance.set(attribute_user, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_productComment(self, value):
        if self.instance:
            self.instance.set(attribute_productComment, value)
            self.__save_instance__()
            return True
        return None

    def output_Order(self):
        if self.instance:
            A = {
                attribute_finalPrice: self.get_attribute_finalPrice(),
                attribute_orderSate: self.get_attribute_orderState(),
                attribute_receiverAddress: self.get_attribute_receiverAddress(),
                attribute_receiverPhoneNumber: self.get_attribute_receiverPhoneNumber(),
                attribute_receiverName: self.get_attribute_receiverName(),
                attribute_shop: self.get_attribute_Object_Id(attribute_shop),
                attribute_user: self.get_attribute_Object_Id(attribute_user),
                attribute_state: self.get_attribute_state(),
                attribute_uniqueId: self.get_attribute_uniqueId(),
                attribute_logisticInfo: self.get_attribute_logisticInfo(),
                attribute_createdAt: self.get_attribute_createdAt(),
                attribute_objectId: self.get_attribute_objectId(),
                attribute_cancelTime: self.get_attribute_cancelTime(),
                attribute_paymentTime: self.get_attribute_paymentTime(),
                attribute_deliveryTime: self.get_attribute_deliveryTime(),
                attribute_refundTime: self.get_attribute_refundTime(),
                attribute_receiveTime: self.get_attribute_receiveTime(),
                attribute_orderProduct: self.get_attribute_orderProduct(),
                attribute_productComment: self.get_attribute_productComment(),
                attribute_pingppOrderId: self.get_attribute_pingppOrderId(),
            }
            return A
        return None

    def output_Order_Simple(self):
        if self.instance:
            A = {
                attribute_finalPrice: self.get_attribute_finalPrice(),
                attribute_orderSate: self.get_attribute_orderState(),
                attribute_uniqueId: self.get_attribute_uniqueId(),
                attribute_createdAt: self.get_attribute_createdAt(),
                attribute_objectId: self.get_attribute_objectId(),
            }
            return A
        return None

    def set_attribute_pingppOrderId(self, value):
        if self.instance:
            self.instance.set(attribute_pingppOrderId, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_receiverName(self, value):
        if self.instance:
            self.instance.set(attribute_receiverName, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_receiverPhoneNumber(self, value):
        if self.instance:
            self.instance.set(attribute_receiverPhoneNumber, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_receiverAddress(self, value):
        if self.instance:
            self.instance.set(attribute_receiverAddress, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_finalPrice(self, value):
        if self.instance:
            self.instance.set(attribute_finalPrice, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_freight(self, value):
        if self.instance:
            self.instance.set(attribute_freight, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_cancelTime(self, value):
        if self.instance:
            self.instance.set(attribute_cancelTime, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_paymentTime(self, value):
        if self.instance:
            self.instance.set(attribute_paymentTime, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_deliveryTime(self, value):
        if self.instance:
            self.instance.set(attribute_deliveryTime, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_refundTime(self, value):
        if self.instance:
            self.instance.set(attribute_refundTime, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_receiveTime(self, value):
        if self.instance:
            self.instance.set(attribute_receiveTime, value)
            self.__save_instance__()
            return True
        return None

    def create_Order(self, data):
        self.create_Object()
        self.set_attribute_pingppOrderId(data[attribute_pingppOrderId])
        self.set_attribute_orderState(data[attribute_orderSate])
        self.set_attribute_receiverPhoneNumber(data[attribute_receiverPhoneNumber])
        self.set_attribute_receiverAddress(data[attribute_receiverAddress])
        self.set_attribute_receiverName(data[attribute_receiverName])
        self.set_attribute_finalPrice(data[attribute_finalPrice])
        self.set_attribute_freight(data[attribute_freight])
        self.set_attribute_cancelTime(data[attribute_cancelTime])
        self.set_attribute_paymentTime(data[attribute_paymentTime])
        self.set_attribute_deliveryTime(data[attribute_deliveryTime])
        self.set_attribute_refundTime(data[attribute_refundTime])
        self.set_attribute_receiveTime(data[attribute_receiveTime])

