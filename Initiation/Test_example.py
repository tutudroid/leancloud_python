"""
测试所有的类接口，写入与显示
:return: 

"""
from Error_Page import *
from ClassLibrary.BaseClass.Attribute_Parameter import *
from ClassLibrary.ProductClass import ProductGroup_New
from ClassLibrary.ShopClass import Shop_New
from ClassLibrary.OrderClass import Order
from ClassLibrary.OrderClass import AfterSaleServiceRecord
from ClassLibrary.ShopClass import SettleInCompany
from ClassLibrary.ShopClass import SettleInUser
from ClassLibrary.ShopClass.SettleInApplication import SettleInApplication

from ClassLibrary.UserClass import User
from ClassLibrary.OrderClass.OrderProduct import OrderProduct
from ClassLibrary.OrderClass.LogisticsInfo import LogisticsInfo
from ClassLibrary.OrderClass.AfterSaleSupport import AfterSaleSupport
from ClassLibrary.ProductClass.ProductComment import ProductComment
from ClassLibrary.ShopClass.IPTable import IPTable
from ClassLibrary.ShopClass.BrandTable import BrandTable

from ClassLibrary.CategoryClass.SaleCategory import SaleCategory
from ClassLibrary.CategoryClass.StoreCategory import StoreCategory
from ClassLibrary.ProductClass.ProductService import ProductService

FIRST = None


def CreateAll(request):
    """
    测试所有的类接口，写入与显示
    :param request: 
    :return: 
    """
    """
    1。 创建app用户，app用户登陆后，生成一条SettleInApplication数据
    2。 创建Shop用户，shop用户注册后，生成一条SettleInApplication数据
    3。 创建app用户创建
    """


    content = {}
    # 创建用户
    user = User._User()
    data = {
        attribute_role: ROLE_SHOP,
        attribute_username: 'username1'+str(datetime.now()),
        attribute_password: 'attribute_password',
        attribute_passwordSure: 'attribute_password',
        attribute_mobilePhoneNumber: '18259429083',
        attribute_avatar: request.FILES.get(attribute_imageFile)
    }

    if FIRST:
        user.create_User(data)
    else:
        user.get_Object('59aa19155c497d00640531e9')


    # 创建 商品IP
    ip = IPTable()
    data = {
        attribute_objectId: 'attribute_objectId',
        attribute_name: 'attribute_name',
        attribute_briefDescription: 'attribute_briefDescription',
        attribute_imageFile: request.FILES.get(attribute_imageFile, ''),
    }
    ip.create_Table(data)
    # 创建商品 品牌
    brand = BrandTable()
    brand.create_Table(data)

    # 创建第一级销售分类
    content = {}
    saleCategoryFirst = SaleCategory(Class_Name_SaleCategoryFirst)
    data = {
        attribute_objectId: '',
        attribute_name: 'Class_Name_SaleCategoryFirst',
        attribute_uniqueId: 'attribute_uniqueId',
        attribute_briefDescription: 'attribute_briefDescription',
        attribute_mainImage: request.FILES.get(attribute_imageFile),
    }
    saleCategoryFirst.create_SaleCategory(data)

    # 创建第二级销售分类
    saleCategorySecond = SaleCategory(Class_Name_SaleCategorySecond)
    data = {
        attribute_objectId: '',
        attribute_name: 'Class_Name_SaleCategorySecond1',
        attribute_uniqueId: 'attribute_uniqueId',
        attribute_briefDescription: 'attribute_briefDescription',
        attribute_mainImage: request.FILES.get(attribute_imageFile),
    }
    saleCategorySecond.create_SaleCategory(data)
    saleCategorySecond.set_attribute_saleCategoryFirst(saleCategoryFirst.get_instance())
    saleCategoryFirst.set_attribute_saleCategorySecond(saleCategorySecond.get_instance())

    # 创建第二级销售分类
    saleCategorySecond = SaleCategory(Class_Name_SaleCategorySecond)
    data = {
        attribute_objectId: '',
        attribute_name: 'Class_Name_SaleCategorySecond2',
        attribute_uniqueId: 'attribute_uniqueId',
        attribute_briefDescription: 'attribute_briefDescription',
        attribute_mainImage: request.FILES.get(attribute_imageFile),
    }
    saleCategorySecond.create_SaleCategory(data)
    saleCategorySecond.set_attribute_saleCategoryFirst(saleCategoryFirst.get_instance())
    saleCategoryFirst.set_attribute_saleCategorySecond(saleCategorySecond.get_instance())

    # store first
    storeFirst = StoreCategory(Class_Name_StoreCategoryFirst)
    data = {
        attribute_objectId: '',
        attribute_name: 'Class_Name_StoreCategoryFirst',
    }
    storeFirst.create_StoreCategory(data)

    # store second
    storeSecond = StoreCategory(Class_Name_StoreCategorySecond)
    data = {
        attribute_objectId: '',
        attribute_name: 'Class_Name_StoreCategorySecond',
    }
    storeSecond.create_StoreCategory(data)
    storeSecond.set_attribute_storeCategoryFirst(storeFirst.get_instance())
    storeFirst.set_attribute_storeCategorySecond(storeSecond.get_instance())

    # store third
    storeThird = StoreCategory(Class_Name_StoreCategoryThird)
    data = {
        attribute_objectId: '',
        attribute_name: 'Class_Name_StoreCategoryThird',
    }
    storeThird.create_StoreCategory(data)
    storeThird.set_attribute_storeCategorySecond(storeSecond.get_instance())
    storeSecond.set_attribute_storeCategoryThird(storeThird.get_instance())

    content['StoreCategory'] = storeFirst.output_StoreCategoryFirst()

    content['SaleCategory'] = saleCategoryFirst.output_SaleCategoryFirst()

    productService = ProductService()
    data = {
        attribute_objectId: 'attribute_objectId',
        attribute_name: 'attribute_name',
        attribute_briefDescription: 'attribute_briefDescription',
    }
    productService.create_ProductService(data)


    # 创建店铺
    shop = Shop_New.Shop()
    data = {
        attribute_productGroup: None,
        attribute_shopProductGroup: None,
        attribute_order: None,
        attribute_address: '街道',
        attribute_PROVINCE: '省',
        attribute_CITY: '市',
        attribute_DISTRICT: '区',
        attribute_user: None,
        attribute_settleInUser: None,
        attribute_settleInCompany: None,
        attribute_phoneNumber: '123456789',
        attribute_mainImage: None,
        attribute_shopType: 1,
        attribute_brand: 123,
        attribute_type: 1,
        attribute_freightModel: None,
        attribute_afterSaleServiceRecord: None,
        attribute_name: '萌test'
    }
    if FIRST:
        shop.create_Shop(data)
    else:
        shop.get_Object('59aa192a570c35006b27ea3c')
    shop.set_attribute_user(user.get_instance())
    shop.set_attribute_brand(brand.get_instance())
    user.set_attribute_shop(shop.get_instance())


    # 创建商品
    productGroup = ProductGroup_New.ProductGroup()
    data = {
        attribute_spec: [
            {
                'SpecName': 'spec',
                'SpecContent': 'specText'
            }
        ],
        attribute_propertyOption:  '[{"PropertyId":"0","PropertyName":"颜色","PropertyOption":[{"OptionId":"0","OptionName":"红色"},{"OptionId":"1","OptionName":"黄色"}]},{"PropertyId":"1","PropertyName":"大小","PropertyOption":[{"OptionId":"0","OptionName":"大号"},{"OptionId":"1","OptionName":"小号"}]}]',
        attribute_name: 'attribute_name',
        attribute_mainImage: request.FILES.get('imageFile'),
        attribute_imageList: request.FILES.getlist('imageFile'),
        attribute_briefDescription: 'attribute_briefDescription',
        attribute_detailDescription: request.FILES.getlist('imageFile'),
        attribute_productService: [productService.get_attribute_objectId()],
        attribute_storeCategory: storeThird.get_attribute_objectId(),
        attribute_saleCategory: [saleCategorySecond.get_attribute_objectId()],
        attribute_dispatchPlace: 'attribute_PROVINCE' + ' ' + 'attribute_CITY' + ' ' + 'attribute_DISTRICT',
        attribute_product: '[{"style":[{"PropertyId":"0","OptionId":"0"},{"PropertyId":"1","OptionId":"0"}],"price":"1","stockCount":"22","mainImage":""},{"style":[{"PropertyId":"0","OptionId":"1"},{"PropertyId":"1","OptionId":"1"}],"price":"11","stockCount":"22","mainImage":""}]',
        attribute_productMainImage: request.FILES.getlist('imageFile'),
        attribute_delete_imageList: 'attribute_delete_imageList',
        attribute_delte_product: 'attribute_delete_product',
        attribute_delete_detailDescription: 'attribute_delete_detailDescription',
    }
    productGroup.create_ProductGroup(data, shop)
    productGroup.set_attribute_brand(brand.get_instance())
    productGroup.set_attribute_ip(ip.get_instance())
    productGroup.set_attribute_shop(shop.get_instance())

    # 创建公司入驻
    data = {
        attribute_objectId: '',
        attribute_alipay: 'attribute_alipay',
        attribute_shopName: 'attribute_shopName',
        attribute_brandName: 'attribute_brandName',
        attribute_brandLogo: 'attribute_brandLogo',
        attribute_brandDescription: 'attribute_brandDescription',
        attribute_businessLicense: 'attribute_businessLicense',
        attribute_managerRealName: 'attribute_managerRealName',
        attribute_managerEmail: 'attribute_managerEmail',
        attribute_managerPhoneNumber: 'attribute_managerPhoneNumber',
        attribute_uniformSocialCreditCode: 'attribute_uniformSocialCreditCode',
        attribute_legalPersonName: 'attribute_legalPersonName',
        attribute_legalPersonEmail: 'attribute_legalPersonEmail',
        attribute_legalPersonPhoneNumber: 'attribute_legalPersonPhoneNumber',
        attribute_legalPersonIdCard: 'attribute_legalPersonIdCard',
        attribute_legalPersonExpireTimeStart: 'attribute_legalPersonExpireTimeStart',
        attribute_legalPersonExpireTimeEnd: 'attribute_legalPersonExpireTimeEnd',
        attribute_legalPersonFrontIdCard: request.FILES.get('imageFile'),
        attribute_legalPersonBackIdCard: request.FILES.get('imageFile'),
    }
    settleInCompany = SettleInCompany.SettleInCompany()
    settleInCompany.create_SettleIn(data)
    settleInCompany.set_attribute_managerEmail('test@compamy.com')
    settleInCompany.set_attribute_shop(shop.get_instance())

    # 创建个人入驻
    data = {
        attribute_objectId: '',
        attribute_alipay: 'attribute_alipay',
        attribute_shopName: 'attribute_shopName',
        attribute_brandName: 'attribute_brandName',
        attribute_brandLogo: 'attribute_brandLogo',
        attribute_brandDescription: 'attribute_brandDescription',
        attribute_realName: 'attribute_realName',
        attribute_email: 'attribute_email',
        attribute_idCardExpireTimeStart: 'attribute_idCardExpireTimeStart',
        attribute_idCardExpireTimeEnd: 'attribute_idCardExpireTimeEnd',
        attribute_handIdCard: request.FILES.get('imageFile'),
        attribute_frontIdCard: request.FILES.get('imageFile'),
        attribute_backIdCard: request.FILES.get('imageFile'),
        attribute_phoneNumber: 'attribute_phoneNumber',
        attribute_idCard: 'attribute_idCard',
    }
    settleInUser = SettleInUser.SettleInUser()
    settleInUser.create_SettleIn(data)
    settleInUser.set_attribute_email('user@user.com')
    settleInUser.set_attribute_shop(shop.get_instance())

    settleIn = SettleInApplication()
    settleIn.create_Object()
    settleIn.set_attribute_state(1)
    settleIn.set_attribute_type(2)
    settleIn.set_attribute_InfoCompany(settleInCompany.get_instance())
    settleIn.set_attribute_InfoPersonal(settleInUser.get_instance())
    settleIn.set_attribute_user(user.get_instance())


    #########
    orderProduct = OrderProduct()
    data = {
        attribute_objectId: 'attribute_objectId',
        attribute_productGroup: 'attribute_productGroup',
        attribute_product: 'attribute_product',
        attribute_groupName: 'attribute_groupName',
        attribute_productStyle: ['attribute_productStyle'],
        attribute_productMainImage: request.FILES.get(attribute_imageFile),
        attribute_productPrice: 1020,
        attribute_productCount: 1000,
        attribute_state: 1,
    }
    orderProduct.create_OrderProduct(data)
    orderProduct.set_attribute_productGroup(productGroup.get_instance())

    logistic = LogisticsInfo()
    data = {
        attribute_state: 11,
        attribute_logisticCode: 'attribute_logisticCode',
        attribute_shipperName: 'attribute_shipperName',
        attribute_shipperCode: 'attribute_shipperCode',
        attribute_traces: ['attribute_traces'],
    }
    logistic.create_LogisticInfo(data)

    # 商品评论
    productComment = ProductComment()
    data = {
        attribute_priority: 11,
        attribute_userAvatar: 'attribute_userAvatar',
        attribute_userNickName: 'attribute_userNickName',
        attribute_imageList: request.FILES.getlist(attribute_imageFile),
        attribute_content: 'attribute_content',
        attribute_productStyle: ['attribute_productStyle'],
    }
    productComment.create_ProductComment(data)
    productComment.set_attribute_orderProduct(orderProduct.get_instance())
    productComment.set_attribute_userAvatar(user.get_avatar())
    productComment.set_attribute_user(user.get_instance())
    productGroup.set_attribute_comment(productComment.get_instance())

    order = Order.Order()
    data = {
        attribute_finalPrice: 100,
        attribute_orderSate: 5,
        attribute_receiverAddress: 'attribute_receiverAddress',
        attribute_receiverPhoneNumber: 'attribute_receiverPhoneNumber',
        attribute_receiverName: 'attribute_receiverName',
        attribute_shop: 'attribute_shop',
        attribute_user: 'attribute_user',
        attribute_state: 1,
        attribute_uniqueId: 'attribute_uniqueId',
        attribute_logisticInfo: 'attribute_logisticInfo',
        attribute_createdAt: 'attribute_createdAt',
        attribute_objectId: 'attribute_objectId',
        attribute_cancelTime: datetime.now(),
        attribute_paymentTime: datetime.now(),
        attribute_deliveryTime: datetime.now(),
        attribute_refundTime: datetime.now(),
        attribute_receiveTime: datetime.now(),
        attribute_orderProduct: 'attribute_orderProduct',
        attribute_productComment: 'attribute_productComment',
        attribute_freight: 100,
        attribute_pingppOrderId: 'attribute_pingppOrderId',
    }
    order.create_Order(data)
    order.set_attribute_orderProduct(orderProduct.get_instance())
    order.set_attribute_logisticInfo(logistic.get_instance())
    order.set_attribute_state(5)
    order.set_attribute_productComment(productComment.get_instance())
    order.set_attribute_shop(shop.get_instance())
    order.set_attribute_user(user.get_instance())


    # 售后支持
    afterSupport = AfterSaleSupport()
    afterSupport.create_Object()
    afterSupport.set_attribute_orderProduct(orderProduct.get_instance())
    afterSupport.set_attribute_order(order.get_instance())
    afterSupport.set_attribute_serviceState(3)

    # 售后服务
    afterSaleServiceRecord = AfterSaleServiceRecord.AfterSaleServiceRecord()
    data = {
        attribute_reason: 'attribute_reason',
        attribute_refundReasonDetail: 'attribute_refundReasonDetail',
        attribute_imageList: request.FILES.getlist(attribute_imageFile),
        attribute_contactName: 'attribute_contactName',
        attribute_contactPhone: 'attribute_contactPhone',
        attribute_refundProductCount: 100,
        attribute_shopReceiverAddress: 'attribute_shopReceiverAddress',
        attribute_shopReceiverName: 'attribute_shopReceiverName',
        attribute_shopReceiverPhone: 'attribute_shopReceiverPhone',
        attribute_uniqueId: 'attribute_uniqueId',
        attribute_refundSumPrice: 100,
        attribute_shipperCode: 'attribute_shipperCode',
        attribute_shipperName: 'attribute_shipperName',
        attribute_logisticCode: 'attribute_logisticCode',
        attribute_createdAt: 'attribute_createdAt',
        attribute_objectId: 'attribute_objectId',
        attribute_order: 'attribute_order',
        attribute_orderProduct: 'attribute_orderProduct',
        attribute_afterSaleProgress: ['attribute_afterSaleProgress'],
    }
    afterSaleServiceRecord.create_AfterSaleServiceRecord(data)
    afterSaleServiceRecord.set_attribute_orderProduct(orderProduct.get_instance())
    afterSaleServiceRecord.set_attribute_order(order.get_instance())
    afterSaleServiceRecord.set_attribute_afterSaleSupport(afterSupport.get_instance())
    afterSaleServiceRecord.set_attribute_shop(shop.get_instance())
    afterSaleServiceRecord.set_attribute_user(user.get_instance())

    shop.set_attribute_productGroup(productGroup.get_instance())
    shop.set_attribute_order(order.get_instance())
    shop.set_attribute_afterSaleServiceRecord(afterSaleServiceRecord.get_instance())

    content['ProductGroup'] = productGroup.output_ProductGroup()
    content['SettleInApplication'] = settleIn.output_SettleInApplication()
    content['Shop'] = shop.output_Shop()
    content['User'] = user.output_User()
    content['Order'] = order.output_Order()
    content['AfterSaleServiceRecord'] = afterSaleServiceRecord.output_AfterSaleServiceRecord()
    return render(request, 'test_class.html', {'content': content})


def AfterSale_Order(request):
    content = {}
    #########
    orderProduct = OrderProduct()
    data = {
        attribute_objectId: 'attribute_objectId',
        attribute_productGroup: 'attribute_productGroup',
        attribute_product: 'attribute_product',
        attribute_groupName: 'attribute_groupName',
        attribute_productStyle: ['attribute_productStyle'],
        attribute_productMainImage: request.FILES.get(attribute_imageFile),
        attribute_productPrice: 1020,
        attribute_productCount: 1000,
        attribute_state: 1,
    }
    orderProduct.create_OrderProduct(data)

    logistic = LogisticsInfo()
    data = {
        attribute_state: 11,
        attribute_logisticCode: 'attribute_logisticCode',
        attribute_shipperName: 'attribute_shipperName',
        attribute_shipperCode: 'attribute_shipperCode',
        attribute_traces: ['attribute_traces'],
    }
    logistic.create_LogisticInfo(data)

    # 商品评论
    productComment = ProductComment()
    data = {
        attribute_priority: 11,
        attribute_userAvatar: 'attribute_userAvatar',
        attribute_userNickName: 'attribute_userNickName',
        attribute_imageList: request.FILES.getlist(attribute_imageFile),
        attribute_content: 'attribute_content',
        attribute_productStyle: ['attribute_productStyle'],
    }
    productComment.create_ProductComment(data)
    productComment.set_attribute_orderProduct(orderProduct.get_instance())

    order = Order.Order()
    data = {
        attribute_finalPrice: 100,
        attribute_orderSate: 5,
        attribute_receiverAddress: 'attribute_receiverAddress',
        attribute_receiverPhoneNumber: 'attribute_receiverPhoneNumber',
        attribute_receiverName: 'attribute_receiverName',
        attribute_shop: 'attribute_shop',
        attribute_user: 'attribute_user',
        attribute_state: 1,
        attribute_uniqueId: 'attribute_uniqueId',
        attribute_logisticInfo: 'attribute_logisticInfo',
        attribute_createdAt: 'attribute_createdAt',
        attribute_objectId: 'attribute_objectId',
        attribute_cancelTime: datetime.now(),
        attribute_paymentTime: datetime.now(),
        attribute_deliveryTime: datetime.now(),
        attribute_refundTime: datetime.now(),
        attribute_receiveTime: datetime.now(),
        attribute_orderProduct: 'attribute_orderProduct',
        attribute_productComment: 'attribute_productComment',
        attribute_freight: 100,
        attribute_pingppOrderId: 'attribute_pingppOrderId',
    }
    order.create_Order(data)
    order.set_attribute_orderProduct(orderProduct.get_instance())
    order.set_attribute_logisticInfo(logistic.get_instance())
    order.set_attribute_state(5)
    order.set_attribute_productComment(productComment.get_instance())
    content['Order'] = order.output_Order()

    # 售后支持
    afterSupport = AfterSaleSupport()
    afterSupport.create_Object()
    afterSupport.set_attribute_orderProduct(orderProduct.get_instance())
    afterSupport.set_attribute_order(order.get_instance())
    afterSupport.set_attribute_serviceState(3)

    # 售后服务
    afterSaleServiceRecord = AfterSaleServiceRecord.AfterSaleServiceRecord()
    data = {
        attribute_reason: 'attribute_reason',
        attribute_refundReasonDetail: 'attribute_refundReasonDetail',
        attribute_imageList: request.FILES.getlist(attribute_imageFile),
        attribute_contactName: 'attribute_contactName',
        attribute_contactPhone: 'attribute_contactPhone',
        attribute_refundProductCount: 100,
        attribute_shopReceiverAddress: 'attribute_shopReceiverAddress',
        attribute_shopReceiverName: 'attribute_shopReceiverName',
        attribute_shopReceiverPhone: 'attribute_shopReceiverPhone',
        attribute_uniqueId: 'attribute_uniqueId',
        attribute_refundSumPrice: 100,
        attribute_shipperCode: 'attribute_shipperCode',
        attribute_shipperName: 'attribute_shipperName',
        attribute_logisticCode: 'attribute_logisticCode',
        attribute_createdAt: 'attribute_createdAt',
        attribute_objectId: 'attribute_objectId',
        attribute_order: 'attribute_order',
        attribute_orderProduct: 'attribute_orderProduct',
        attribute_afterSaleProgress: ['attribute_afterSaleProgress'],
    }
    afterSaleServiceRecord.create_AfterSaleServiceRecord(data)
    afterSaleServiceRecord.set_attribute_orderProduct(orderProduct.get_instance())
    afterSaleServiceRecord.set_attribute_order(order.get_instance())
    afterSaleServiceRecord.set_attribute_state(1)
    afterSaleServiceRecord.set_attribute_afterSaleSupport(afterSupport.get_instance())


    content['AfterSaleServiceRecord'] = afterSaleServiceRecord.output_AfterSaleServiceRecord()
    return render(request, 'test_class.html', {'content': content})


def Category(request):
    # 创建第一级销售分类
    content = {}
    saleCategoryFirst = SaleCategory(Class_Name_SaleCategoryFirst)
    data = {
        attribute_objectId: '',
        attribute_name: 'Class_Name_SaleCategoryFirst',
        attribute_uniqueId: 'attribute_uniqueId',
        attribute_briefDescription: 'attribute_briefDescription',
        attribute_mainImage: request.FILES.get(attribute_imageFile),
    }
    saleCategoryFirst.create_SaleCategory(data)

    # 创建第二级销售分类
    saleCategorySecond = SaleCategory(Class_Name_SaleCategorySecond)
    data = {
        attribute_objectId: '',
        attribute_name: 'Class_Name_SaleCategorySecond1',
        attribute_uniqueId: 'attribute_uniqueId',
        attribute_briefDescription: 'attribute_briefDescription',
        attribute_mainImage: request.FILES.get(attribute_imageFile),
    }
    saleCategorySecond.create_SaleCategory(data)
    saleCategorySecond.set_attribute_saleCategoryFirst(saleCategoryFirst.get_instance())
    saleCategoryFirst.set_attribute_saleCategorySecond(saleCategorySecond.get_instance())

    # 创建第二级销售分类
    saleCategorySecond = SaleCategory(Class_Name_SaleCategorySecond)
    data = {
        attribute_objectId: '',
        attribute_name: 'Class_Name_SaleCategorySecond2',
        attribute_uniqueId: 'attribute_uniqueId',
        attribute_briefDescription: 'attribute_briefDescription',
        attribute_mainImage: request.FILES.get(attribute_imageFile),
    }
    saleCategorySecond.create_SaleCategory(data)
    saleCategorySecond.set_attribute_saleCategoryFirst(saleCategoryFirst.get_instance())
    saleCategoryFirst.set_attribute_saleCategorySecond(saleCategorySecond.get_instance())

    # store first
    storeFirst = StoreCategory(Class_Name_StoreCategoryFirst)
    data = {
        attribute_objectId: '',
        attribute_name: 'Class_Name_StoreCategoryFirst',
    }
    storeFirst.create_StoreCategory(data)

    # store second
    storeSecond = StoreCategory(Class_Name_StoreCategorySecond)
    data = {
        attribute_objectId: '',
        attribute_name: 'Class_Name_StoreCategorySecond',
    }
    storeSecond.create_StoreCategory(data)
    storeSecond.set_attribute_storeCategoryFirst(storeFirst.get_instance())
    storeFirst.set_attribute_storeCategorySecond(storeSecond.get_instance())

    # store third
    storeThird = StoreCategory(Class_Name_StoreCategoryThird)
    data = {
        attribute_objectId: '',
        attribute_name: 'Class_Name_StoreCategoryThird',
    }
    storeThird.create_StoreCategory(data)
    storeThird.set_attribute_storeCategorySecond(storeSecond.get_instance())
    storeSecond.set_attribute_storeCategoryThird(storeThird.get_instance())

    content['StoreCategory'] = storeFirst.output_StoreCategoryFirst()

    content['SaleCategory'] = saleCategoryFirst.output_SaleCategoryFirst()
    return render(request, 'test_class.html', {'content': content})


def AllCategory(request):

    content = {}

    content['SaleCategoryAll'] = SaleCategory().get_SaleCategory_All()
    content['StoreCategoryAll'] = StoreCategory().get_StoreCategory_All()
    print(content)
    return render(request, 'test_class.html', {'content': content})


def AllProduct(request):

    state = request.GET.get(attribute_state, 0)
    page = request.GET.get(paginator_PAGE, 1)
    shop = Shop_New.Shop()
    shop.get_Object('59aa192a570c35006b27ea3c')
    content = {
        'AllProductGroup': shop.get_attribute_productGroup(0, page),
    }
    ppp = {
        paginator_Prev_PAGE: int( page ) - 1,
        paginator_PAGE: page,
        paginator_Next_PAGE: int( page ) + 1,
        paginator_NUM_PAGES: shop.count_attribute_productGroup( int( state ) )
    }
    return render(request, 'test_class.html', {'content': content, Class_Name_paginator: ppp })


def AllOrder(request):

    state = request.GET.get(attribute_state, 5)
    page = request.GET.get(paginator_PAGE, 1)
    shop = Shop_New.Shop()
    shop.get_Object('59aa192a570c35006b27ea3c')
    content = {
        'AllOrder': shop.get_attribute_order(state, page),
    }
    ppp = {
        paginator_Prev_PAGE: int(page) - 1,
        paginator_PAGE: page,
        paginator_Next_PAGE: int(page ) + 1,
        paginator_NUM_PAGES: shop.count_attribute_order( int( state ) )
    }
    return render(request, 'test_class.html', {'content': content, Class_Name_paginator: ppp })


def AllAfterSale(request):
    state = request.GET.get(attribute_state, 0)
    page = request.GET.get(paginator_PAGE, 1)
    shop = Shop_New.Shop()
    shop.get_Object('59aa192a570c35006b27ea3c')
    content = {
        'AllAfterSale': shop.get_attribute_afterSaleServiceRecord(int(state), page),
    }
    ppp = {
        paginator_Prev_PAGE: int( page ) - 1,
        paginator_PAGE: page,
        paginator_Next_PAGE: int( page ) + 1,
        paginator_NUM_PAGES: shop.count_attribute_afterSaleServiceRecord( int( state ) )
    }
    return render(request, 'test_class.html', {'content': content, Class_Name_paginator: ppp })