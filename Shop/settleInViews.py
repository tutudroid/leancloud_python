from Error_Page import *
from ClassLibrary.BaseClass.Attribute_Parameter import *
from ClassLibrary.ShopClass.SettleInUser import SettleInUser
from ClassLibrary.ShopClass.SettleInCompany import SettleInCompany
from ClassLibrary.ShopClass.Shop_New import Shop
from ClassLibrary.ShopClass.SettleInApplication import SettleInApplication


@login_required
@permission(ROLE_ADMINISTRATOR)
@require_http_methods(['GET'])
def AllSettleIn(request):
    """
    显示所有的入驻信息
    :param request:
        state = 
            SETTLE_IN_STATE_0 = 0  # 待审核
            SETTLE_IN_STATE_1 = 1  # 拒绝
            SETTLE_IN_STATE_2 = 2  # 通过
            SETTLE_IN_STATE_3 = 3  # 禁用
    :return: 
        shopList
    """
    state = request.GET.get(attribute_state)
    page = request.GET.get(paginator_PAGE)
    if state and 0 <= int(state) <= 4:
        shop = Shop()
        shopList = shop.get_settleIn_shop(int(state), page)
        returnData = {
            Class_Name_Shop: shopList,
            Class_Name_paginator: {
                paginator_PAGE: page,
                paginator_NUM_PAGES: shop.count_settleIn_shop(int(state))
            }
        }
        return return_OK( returnData )
    return illegal_access()


@login_required
@permission(ROLE_SHOP)
@require_http_methods(['POST'])
def CreateSettleIn(request):
    """
    编辑或创建入驻信息
    :param request: 
    :return: 
    """
    type = request.POST.get(attribute_type, -1)
    settleInApplicationObjectId = request.POST.get('settleInApplicationObjectId', '')
    if settleInApplicationObjectId and int(type) == 1 or int(type) == 0:
        if int(type) == 1:
            settleIn = SettleInUser()
        else:
            settleIn = SettleInCompany()
        data = settleIn.input_SettleIn(request)
        settleIn.create_SettleIn(data)
        returnData = settleIn.output_SettleIn()

        settleInApplication = SettleInApplication()
        settleInApplication.get_Object(settleInApplicationObjectId)
        settleInApplication.set_attribute_type(int(type))
        settleInApplication.set_attribute_state(SETTLE_IN_STATE_0)
        if int(type) == 1:
            settleInApplication.set_attribute_InfoPersonal(settleIn.get_instance())
        else:
            settleInApplication.set_attribute_InfoCompany(settleIn.get_instance())
        return return_OK( returnData )
    return illegal_access()


@login_required
@permission(ROLE_ADMINISTRATOR)
@require_http_methods(['GET'])
def ReviewSettleIn(request):
    """
    审核入驻信息
    :param request: 
    :return: 
    """
    objectId = request.POST.get(attribute_objectId)
    state = request.POST.get(attribute_state)
    if objectId and 1 <= int(state) <= 2:
        shop = Shop()
        shop.get_Object(objectId)
        shop.set_attribute_state(int(state))

        shopType = shop.get_attribute_shopType()
        if int(shopType) == 1:
            settleIn = SettleInUser()
            data = shop.get_attribute_settleInUser()
        else:
            settleIn = SettleInCompany()
            data = shop.get_attribute_settleInCompany()
        if data:
            settleIn.get_Object(data[attribute_objectId])
            settleIn.set_attribute_state(int(state))
            return return_OK( 'success' )
    return illegal_access()
