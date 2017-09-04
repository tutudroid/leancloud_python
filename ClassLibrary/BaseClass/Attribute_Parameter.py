
Class_Name_StoreCategory = 'StoreCategory'
Class_Name_SaleCategory = 'SaleCategory'
Class_Name_SaleCategoryFirst = 'SaleCategoryFirst'
Class_Name_SaleCategorySecond = 'SaleCategorySecond'
Class_Name_SaleCategoryImage = 'SaleCategoryImage'
Class_Name_SaleCategoryRecommend = 'SaleCategoryRecommend'
Class_Name_StoreCategoryFirst = 'StoreCategoryFirst'
Class_Name_StoreCategorySecond = 'StoreCategorySecond'
Class_Name_StoreCategoryThird = 'StoreCategoryThird'
Class_Name_OrderProduct = 'OrderProduct'
Class_Name_Shop = 'Shop'
Class_Name_ShopProductGroup = 'ShopProductGroup'
Class_Name_ShopProduct = 'ShopProduct'
Class_Name_ProductGroup = 'ProductGroup'
Class_Name_Product = 'Product'
Class_Name_Order = 'Order'
Class_Name_IPTable = 'IPTable'
Class_Name_BrandTable = 'BrandTable'
Class_Name_SettleInCompany = 'SettleInCompany'
Class_Name_SettleInUser = 'SettleInUser'
Class_Name_ProductCommentImage = 'ProductCommentImage'
Class_Name_ProductComment = 'ProductComment'
Class_Name_ProductService = 'ProductService'
Class_Name_ProductDetailDescription = 'ProductDetailDescription'
Class_Name_ProductImage = 'ProductImage'
Class_Name_LogisticsInfo = 'LogisticsInfo'
Class_Name_AfterSaleServiceImage = 'AfterSaleServiceImage'
Class_Name_AfterSaleServiceRecord = 'AfterSaleServiceRecord'
Class_Name_AfterSaleSupport = 'AfterSaleSupport'
Class_Name_User = 'User'
Class_Name_Role = 'Role'
Class_Name_SettleInApplication = 'SettleInApplication'
Class_Name_WebPageConfigure = 'WebPageConfigure'



# base attribute
attribute_objectId = 'objectId'
attribute_uniqueId = 'uniqueId'
attribute_state = 'state'
attribute_name = 'name'
attribute_imageFile = 'imageFile'
STATE_DELETE = -1
STATE_OK = 0



# afterSaleServiceRecord
attribute_refundReasonDetail = 'refundReasonDetail'
attribute_imageList = 'imageList'
attribute_refundProductCount = 'refundProductCount'
attribute_contactName = 'contactName'
attribute_contactPhone = 'contactPhone'
attribute_shopReceiverAddress = 'shopReceiverAddress'
attribute_shopReceiverName = 'shopReceiverName'
attribute_shopReceiverPhone = 'shopReceiverPhone'
attribute_refundSumPrice = 'refundSumPrice'
attribute_user = 'user'
attribute_shop = 'shop'
attribute_afterSaleSupport = 'afterSaleSupport'
attribute_order = 'order'
attribute_orderProduct = 'orderProduct'
attribute_afterSaleProgress = 'afterSaleProgress'
attribute_reason = 'reason'
attribute_recordState = 'recordState'

### 售后状态
AFTER_SALE_0 = 0   # 待受理
AFTER_SALE_1 = 1   # 未通过
AFTER_SALE_2 = 2   # 待退货
AFTER_SALE_3 = 3   # 退货中
AFTER_SALE_4 = 4   # 已退款
AFTER_SALE_5 = 5   # 已取消
AFTER_SALE_6 = 6   # 直接退款

# afterSaleSupport
attribute_serviceState = 'serviceState'


SERVICE_STATE_0 = 0  # 可申请
SERVICE_STATE_1 = 1  # 处理中
SERVICE_STATE_2 = 2  # 已完成
SERVICE_STATE_3 = 3  # 超时


# StoreCategory

attribute_storeCategoryFirst = 'storeCategoryFirst'
attribute_storeCategorySecond = 'storeCategorySecond'
attribute_storeCategoryThird = 'storeCategoryThird'
attribute_productGroup = 'productGroup'

# saleCategory
attribute_saleCategorySecond = 'saleCategorySecond'
attribute_saleCategoryFirst = 'saleCategoryFirst'
attribute_mainImage = 'mainImage'
attribute_briefDescription = 'briefDescription'
attribute_categoryType = 'categoryType'
attribute_saleCategoryRecommend = 'saleCategoryRecommend'

# productGroup

STATE_SHELF_ON = 0
STATE_NO_FINISH = 2

attribute_propertyOption = 'propertyOption'
attribute_productService = 'productService'
attribute_ip = 'ip'
attribute_product = 'product'
attribute_brand = 'brand'
attribute_saleCategory = 'saleCategory'
attribute_storeCategory = 'storeCategory'
attribute_collectionUser = 'collectionUser'
attribute_comment = 'comment'
attribute_detailDescription = 'detailDescription'
attribute_saleCount = 'saleCount'
attribute_price = 'price'
attribute_spec = 'spec'
attribute_freightModel = 'freightModel'
attribute_dispatchPlace = 'dispatchPlace'
attribute_audit = 'audit'
attribute_productMainImage = 'productMainImage'
attribute_group = 'group'

# 修改商品组时可能的参数
attribute_delete_imageList = 'delete_imageList'
attribute_delte_product = 'delete_product'
attribute_delete_detailDescription = 'delete_detailDescription'

# product
attribute_style = 'style'
attribute_stockCount = 'stockCount'
attribute_styleBackUp = 'styleBackUp'
attribute_limitCount = 'limitCount'

# productComment
attribute_priority = 'priority'
attribute_userAvatar = 'userAvatar'
attribute_userNickName = 'userNickName'
attribute_content = 'content'
attribute_productStyle = 'productStyle'

# shop
attribute_address = 'address'
attribute_afterSaleServiceRecord = 'afterSaleServiceRecord'
attribute_createdAt = 'createdAt'
attribute_settleInUser = 'settleInUser'
attribute_settleInCompany = 'settleInCompany'
attribute_phoneNumber = 'phoneNumber'
attribute_shopProductGroup = 'shopProductGroup'
attribute_shopType = 'shopType'
attribute_PROVINCE = 'province'
attribute_CITY = 'city'
attribute_DISTRICT = 'district'
attribute_type = 'type'


attribute_phoneNumber_Old = 'phoneNumberOld'
attribute_phoneNumber_New = 'phoneNumberNew'

# settleIn
attribute_alipay = 'alipay'
attribute_shopName = 'shopName'
attribute_brandName = 'brandName'
attribute_brandLogo = 'brandLogo'
attribute_brandDescription = 'brandDescription'

SHOP_TYPE_0 = 0  # user
SHOP_TYPE_1 = 1  # company

# settleIn State
SETTLE_IN_STATE_0 = 0  # 待审核
SETTLE_IN_STATE_1 = 1  # 拒绝
SETTLE_IN_STATE_2 = 2  # 通过
SETTLE_IN_STATE_3 = 4  # 未申请

# settleInCompany
attribute_businessLicense = 'businessLicense'
attribute_managerRealName = 'managerRealName'
attribute_managerEmail = 'managerEmail'
attribute_managerPhoneNumber = 'managerPhoneNumber'
attribute_uniformSocialCreditCode = 'uniformSocialCreditCode'
attribute_legalPersonName = 'legalPersonName'
attribute_legalPersonEmail = 'legalPersonEmail'
attribute_legalPersonPhoneNumber = 'legalPersonPhoneNumber'
attribute_legalPersonIdCard = 'legalPersonIdCard'
attribute_legalPersonExpireTimeStart = 'legalPersonExpireTimeStart'
attribute_legalPersonExpireTimeEnd = 'legalPersonExpireTimeEnd'
attribute_legalPersonFrontIdCard = 'legalPersonFrontIdCard'
attribute_legalPersonBackIdCard = 'legalPersonBackIdCard'

# settleInUser
attribute_realName = 'realName'
attribute_email = 'email'
attribute_idCard = 'idCard'
attribute_idCardExpireTimeStart = 'idCardExpireTimeStart'
attribute_idCardExpireTimeEnd = 'idCardExpireTimeEnd'
attribute_handIdCard = 'handIdCard'
attribute_frontIdCard = 'frontIdCard'
attribute_backIdCard = 'backIdCard'

# settleIn application
attribute_infoCompany = 'infoCompany'
attribute_infoPersonal = 'infoPersonal'


# web page configure
attribute_code = 'code'
attribute_url = 'url'

# order
attribute_finalPrice = 'finalPrice'
attribute_orderSate = 'orderState'
attribute_receiverAddress = 'receiverAddress'
attribute_receiverPhoneNumber = 'receiverPhoneNumber'
attribute_receiverName = 'receiverName'
attribute_logisticInfo = 'logisticsInfo'
attribute_productComment = 'productComment'
attribute_pingppOrderId = 'pingppOrderId'
attribute_freight = 'freight'
attribute_cancelTime = 'cancelTime'
attribute_paymentTime = 'paymentTime'
attribute_deliveryTime = 'deliveryTime'
attribute_refundTime = 'refundTime'
attribute_receiveTime = 'receiveTime'


ORDER_STATE_NO_PAY = 0          # 待付款
ORDER_STATE_NO_DISPLACED = 1    # 未发货
ORDER_STATE_DISPLACED = 2       # 已发货
ORDER_STATE_FINISHED = 3        # 已完成
ORDER_STATE_COMMENTS = 4        # 已评价
ORDER_STATE_CANCEL = 5          # 已取消
ORDER_STATE_REFUND = 6          # 已退款

# orderProduct
attribute_groupName = 'groupName'
attribute_productPrice = 'productPrice'
attribute_productCount = 'productCount'


# logisticsCode
attribute_shipperCode = 'shipperCode'
attribute_shipperName = 'shipperName'
attribute_logisticCode = 'logisticsCode'
attribute_traces = 'traces'

# user
attribute_role = 'role'
attribute_username = 'username'
attribute_mobilePhoneNumber = 'mobilePhoneNumber'
attribute_avatar = 'avatar'
attribute_nikeName = 'nikeName'
attribute_forbidden = 'forbidden'
attribute_sex = 'sex'
attribute_birthday = 'birthday'


attribute_password = 'password'
attribute_passwordSure = 'passwordSure'
attribute_verifyCode = 'verifyCode'

STATE_FORBIDDEN = 1

# role
attribute_users = 'users'

ROLE_ADMINISTRATOR = 'Administrator'
ROLE_SHOP = 'Shop'
ROLE_PRODUCT = 'ProductAdmin'
ROLE_CUSTOM = 'CustomService'
ROLE_BUSINESS = 'BusinessOperation'
ROLE_APP = 'App'
ROLE_NONE = 'None'
ROLE_SYS = 'Sys'

ROLE = [
    ROLE_NONE,           # app用户第一次登陆，并没有角色信息， 将该用户至于None角色下
    ROLE_ADMINISTRATOR,  # 管理员账户，只有一个用户
    ROLE_SHOP,           # 店铺用户，当用户审核通过后，将该用户角色设置为shop
    ROLE_PRODUCT,
    ROLE_CUSTOM,
    ROLE_BUSINESS,
    ROLE_APP,            # app 用户注册后，将该用户变为该角色
]

# sale
TYPE_BASE = 0
TYPE_RECOMMEND = 1
TYPE_IP = 2


# paginator
Class_Name_paginator = 'Paginator'
QUERY_SKIP = 10
paginator_PAGE = 'page'
paginator_Next_PAGE = 'next_page'
paginator_Prev_PAGE = 'prev_page'
paginator_NUM_PAGES = 'num_pages'


# return
return_status = 'status'
