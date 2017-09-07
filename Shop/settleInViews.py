from Error_Page import *
from ClassLibrary.BaseClass.Attribute_Parameter import *
from ClassLibrary.ShopClass.SettleInUser import SettleInUser
from ClassLibrary.ShopClass.SettleInCompany import SettleInCompany
from ClassLibrary.ShopClass.Shop_New import Shop
from ClassLibrary.ShopClass.SettleInApplication import SettleInApplication
from ClassLibrary.UserClass.User import _User


@login_required
#@permission(ROLE_ADMINISTRATOR)
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
    state = request.GET.get(attribute_state, -1)
    page = request.GET.get(paginator_PAGE, 1)
    type1 = request.GET.get(attribute_type, -1)
    if 0 <= int(state) <= 4:
        settle = SettleInApplication()
        settleList = settle.get_SettleInApplication_All(state, type1, page)
        count = settle.count_SettleInApplication_All(state, type1)
        return return_paginator_page(Class_Name_SettleInApplication, settleList, page, count)
    return return_msg('parameter is error')


@login_required
#@permission(ROLE_SHOP)
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
            settleIn = SettleInCompany()
        else:
            settleIn = SettleInUser()
        data = settleIn.input_SettleIn(request)
        settleIn.create_SettleIn(data)
        returnData = settleIn.output_SettleIn()

        settleInApplication = SettleInApplication()
        settleInApplication.get_Object(settleInApplicationObjectId)
        settleInApplication.set_attribute_type(int(type))
        settleInApplication.set_attribute_state(SETTLE_IN_STATE_0)
        if int(type) == 1:
            settleInApplication.set_attribute_InfoCompany(settleIn.get_instance())
        else:
            settleInApplication.set_attribute_InfoPersonal(settleIn.get_instance())
        return return_msg( returnData )
    return illegal_access()


@login_required
#@permission(ROLE_ADMINISTRATOR)
@require_http_methods(['GET'])
def ReviewSettleIn(request):
    """
    审核入驻信息
    :param request: 
    :return: 
    """
    objectId = request.GET.get(attribute_objectId, '')
    state = request.GET.get(attribute_state, 0)
    if objectId and 1 <= int(state) <= 2:
        settleInApplication = SettleInApplication()
        settleInApplication.get_Object(objectId)
        settleInApplication.set_attribute_state(int(state))
        if 2 == int(state):
            # 创建店铺
            shop = Shop()
            shop.create_Object()

            shopType = settleInApplication.get_attribute_type()
            shop.set_attribute_shopType(shopType)
            shop.set_attribute_user(settleInApplication.get_user())
            shop.set_attribute_type(0)
            if 1 == shopType:
                shop.set_attribute_settleInCompany(settleInApplication.get_attribute(attribute_infoCompany))
            else:
                shop.set_attribute_settleInUser(settleInApplication.get_attribute(attribute_infoPersonal))

            user = _User()
            user.get_Object(settleInApplication.get_attribute_user_id())
            user.set_attribute_shop(shop.get_instance())
            shop.set_attribute_phoneNumber(user.get_attribute_mobilePhoneNumber())

        return return_msg('success')
    return return_msg('parameter is error')
