from ClassLibrary.BaseClass.Object import *
from ClassLibrary.OrderClass.LogisticsInfo import LogisticsInfo
from ClassLibrary.OrderClass.AfterSaleSupport import AfterSaleSupport
from ClassLibrary.ImageClass.AfterSaleServiceImage import AfterSaleServiceImage
from ClassLibrary.OrderClass.OrderProduct import OrderProduct
import time

class AfterSaleServiceRecord(LogisticsInfo):
    def __init__(self):
        super(AfterSaleServiceRecord, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_refundReasonDetail(self):
        if self.instance:
            return self.instance.get(attribute_refundReasonDetail)
        return None

    def get_attribute_imageList(self):
        if self.instance:
            imageList = Base.get_relation_data(self.instance.get(attribute_objectId), self.__class__.__name__, attribute_imageList)
            if imageList:
                returnList = []
                for foo in imageList:
                    image = AfterSaleServiceImage()
                    image.set_instance(foo)
                    returnList.append(image.output_Image())
                return returnList
        return None

    def get_attribute_order(self):
        if self.instance:
            return self.instance.get(attribute_order)
        return None

    def get_attribute_orderProduct(self):
        if self.instance and self.instance.get(attribute_orderProduct):
            orderProduct = OrderProduct()
            orderProduct.get_Object(self.instance.get(attribute_orderProduct).id)
            return orderProduct.output_OrderProduct()
        return None


    def set_attribute_orderProduct(self, value):
        if self.instance and value:
            self.instance.set(attribute_orderProduct, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_order(self, value):
        if self.instance and value:
            self.instance.set(attribute_order, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_user(self, value):
        if self.instance and value:
            self.instance.set(attribute_user, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_shop(self, value):
        if self.instance and value:
            self.instance.set(attribute_shop, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_imageList(self, imageFile):
        if self.instance:
            relation = self.instance.relation(attribute_imageList)
            relation.add(imageFile)
            if self.__save_instance__():
                return True
        return None

    def get_attribute_refundProductCount(self):
        if self.instance:
            return self.instance.get(attribute_refundProductCount)
        return None

    def get_attribute_contactName(self):
        if self.instance:
            return self.instance.get(attribute_contactName)
        return None

    def get_attribute_contactPhone(self):
        if self.instance:
            return self.instance.get(attribute_contactPhone)
        return None

    def get_attribute_shopReceiverAddress(self):
        if self.instance:
            return self.instance.get(attribute_shopReceiverAddress)
        return None

    def get_attribute_shopReceiverName(self):
        if self.instance:
            return self.instance.get(attribute_shopReceiverName)
        return None

    def get_attribute_shopReceiverPhone(self):
        if self.instance:
            return self.instance.get(attribute_shopReceiverPhone)
        return None

    def get_attribute_refundSumPrice(self):
        if self.instance:
            return self.instance.get(attribute_refundSumPrice)
        return None

    def get_attribute_attribute_user(self):
        if self.instance:
            return self.instance.get(attribute_user)
        return None

    def get_attribute_shop(self):
        if self.instance:
            return self.instance.get(attribute_shop)
        return None

    def get_attribute_afterSaleSupport(self):
        if self.instance:
            return self.instance.get(attribute_afterSaleSupport)
        return None

    def get_attribute_afterSaleProgress(self):
        if self.instance:
            return self.instance.get(attribute_afterSaleProgress)
        return None

    def get_attribute_reason(self):
        if self.instance:
            return self.instance.get(attribute_reason)
        return None

    def set_attribute_afterSaleProgress(self, value):
        if self.instance and value:
            self.instance.set(attribute_afterSaleProgress, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_afterSaleSupport(self, value):
        if self.instance and value:
            self.instance.set(attribute_afterSaleSupport, value)
            self.__save_instance__()
            return True
        return None

    def set_attribute_state(self, value):
        if self.instance and value:
            if 0 <= int(value) <= 6:
                newRecordDetail = {
                    'AcceptTime': time.strftime("%Y-%m-%d %H:%M", time.localtime()),
                    'AcceptStation': self.__getRecordDetail__(int(value)),
                    'State': int(value),
                }
                recordDetail = self.get_attribute_afterSaleProgress()
                if recordDetail is None:
                    recordDetail = []
                recordDetail.append(newRecordDetail)
                self.set_attribute_afterSaleProgress(recordDetail)
                if self.set_attribute_afterSaleProgress(recordDetail):
                    if int(value) == 1 or int(value) == 4:
                        support = self.get_attribute_afterSaleSupport()
                        # 如果未发货直接退款，则这里support为空
                        if support:
                            afterSaleSupport = AfterSaleSupport()
                            afterSaleSupport.get_Object(support.get(attribute_objectId))
                            if int(value) == 1:
                                # 拒绝售后
                                afterSaleSupport.set_attribute_state(SERVICE_STATE_0)
                            elif int(value) == 4:
                                # 已退款
                                afterSaleSupport.set_attribute_state(SERVICE_STATE_2)
                    self.instance.set(attribute_state, int(value))
                    if self.__save_instance__():
                        return True
                else:
                    Base.sys_log('save fail')
            else:
                Base.sys_log('value is invalid')
        else:
            Base.sys_log('parameter is null')
        return None

    def get_AfterSaleServiceRecord_count(self, recordState):
        """
        获得某状态下订单个数
        :return: 
        """
        self.instance = self.instance
        count = Base.queryInstanceAttributeCount(self.__class__.__name__, attribute_state, int(recordState))
        if count:
            return count
        return 0

    def get_AfterSaleServiceRecord_recordState(self, recordState, skip=None, limit=None):
        self.instance = self.instance
        if recordState is not None:
            afterSaleList = Base.queryInstanceAttribute(self.__class__.__name__, attribute_state, int(recordState), skip, limit)
            if afterSaleList:
                return afterSaleList
            else:
                return None

    def output_AfterSaleServiceRecord(self):
        if self.instance:
            A = {
                attribute_reason: self.get_attribute_reason(),
                attribute_refundReasonDetail: self.get_attribute_refundReasonDetail(),
                attribute_imageList: self.get_attribute_imageList(),
                attribute_contactName: self.get_attribute_contactName(),
                attribute_contactPhone: self.get_attribute_contactPhone(),
                attribute_refundProductCount: self.get_attribute_refundProductCount(),
                attribute_shopReceiverAddress: self.get_attribute_shopReceiverAddress(),
                attribute_shopReceiverName: self.get_attribute_shopReceiverName(),
                attribute_shopReceiverPhone: self.get_attribute_shopReceiverPhone(),
                attribute_uniqueId: self.get_attribute_uniqueId(),
                attribute_refundSumPrice: self.get_attribute_refundSumPrice(),
                attribute_shipperCode: self.get_attribute_shipperCode(),
                attribute_shipperName: self.get_attribute_shipperName(),
                attribute_logisticCode: self.get_attribute_logisticCode(),
                attribute_createdAt: self.get_attribute_createdAt(),
                attribute_objectId: self.get_attribute_objectId(),
                attribute_order: self.get_attribute_Object_Id(attribute_order),
                attribute_orderProduct: self.get_attribute_Object_Id(attribute_orderProduct),
                attribute_afterSaleProgress: self.get_attribute_afterSaleProgress(),
                attribute_state: self.get_attribute_state(),
            }
            print(A)
            return A
        return None


    def create_AfterSaleServiceRecord(self, data):

        service = self.create_Object()
        service.set(attribute_contactName, data[attribute_contactName])
        service.set(attribute_contactPhone, data[attribute_contactPhone])
        service.set(attribute_refundSumPrice, float(data[attribute_refundSumPrice]))
        service.set(attribute_refundReasonDetail, data[attribute_refundReasonDetail])
        service.set(attribute_shipperName, data[attribute_shipperName])
        service.set(attribute_shipperCode, data[attribute_shipperCode])
        service.set(attribute_shopReceiverPhone, data[attribute_shopReceiverPhone])
        service.set(attribute_shopReceiverName, data[attribute_shopReceiverName])
        service.set(attribute_shopReceiverAddress, data[attribute_shopReceiverAddress])
        service.set(attribute_refundProductCount, int(data[attribute_refundProductCount]))
        service.set(attribute_logisticCode, data[attribute_logisticCode])
        service.set(attribute_afterSaleProgress, data[attribute_afterSaleProgress])
        service.set(attribute_reason, data[attribute_reason])
        Base.save_data(service)
        if data[attribute_imageList]:
            for foo in data[attribute_imageList]:
                image = AfterSaleServiceImage()
                image.create_Image(foo)
                self.set_attribute_imageList(image.get_instance())
        if self.__save_instance__():
            return service.id

    @staticmethod
    def __getRecordDetail__(state):
        A = ''
        if state == AFTER_SALE_2:
            A = '申请已受理，请在14天内寄回商品并提交物流信息，过期将自动取消申请'
        elif state == AFTER_SALE_3:
            A = '等待客服收货'
        elif state == AFTER_SALE_4:
            A = '已退款，退款将按照原支付方式返还，7个工作日内到账'
        elif state == AFTER_SALE_1:
            A = '申请未通过'
        elif state == AFTER_SALE_5:
            A = '已取消'
        elif state == AFTER_SALE_6:
            A = '直接退款，退款将按照原支付方式返还，7个工作日内到账'
        return A
