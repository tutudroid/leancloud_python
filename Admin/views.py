# 本地App库
from Error_Page import *
from ClassLibrary.UserClass.User import _User
from ClassLibrary.ShopClass.Shop_New import Shop
from ClassLibrary.ShopClass.SettleInApplication import SettleInApplication
from ClassLibrary.ShopClass.SettleInUser import SettleInUser
from ClassLibrary.ShopClass.SettleInCompany import SettleInCompany
from ClassLibrary.Others.WebPageConfigure import WebPageConfigure


@login_required
# @permission(ROLE_ADMINISTRATOR)
@require_http_methods(['POST'])
def AddUser(request):
    """
    新增一个用户
    :param request: 
    :return: 
    """
    print(request.POST)
    user = _User()
    data = user.input_User(request)
    if user.create_User(data):
        return return_msg('success')
    print('create account failed')
    return return_msg('username has existed')


@login_required
# @permission(ROLE_ADMINISTRATOR)
@require_http_methods(['GET'])
def AppUser(request):
    """
    显示app用户
    :param request: 
    :return: 
    """
    user = _User()

    """设置分页"""
    page = request.GET.get(paginator_PAGE, 1)  # 获取页码
    page_nums = user.count_App_User()

    user_list = user.get_App_User(page)
    return return_paginator_page(Class_Name_User, user_list, page, page_nums)


@login_required
# @permission(ROLE_ADMINISTRATOR)
@require_http_methods(['GET'])
def ShopUser(request):
    """
    显示店铺用户
    :param request: 
    
            SETTLE_IN_STATE_0 = 0  # 待审核
            SETTLE_IN_STATE_1 = 1  # 拒绝
            SETTLE_IN_STATE_2 = 2  # 通过
            SETTLE_IN_STATE_3 = 3  # 禁用
            
            {
                'page': page
                'state': state
                'type': 1/0
            }
    :return: 
    """
    """设置分页"""
    page = request.GET.get(paginator_PAGE, 1)  # 获取页码
    state = request.GET.get(attribute_state)
    shop = Shop()
    page_nums = shop.count_Shop_Audit_All(state)
    shopList = shop.get_Shop_Audit_All(state, page)

    return return_paginator_page(Class_Name_Shop, shopList, page, page_nums)


@login_required
# @permission(ROLE_ADMINISTRATOR)
@require_http_methods(['GET'])
def audit_shop(request):
    objectId = request.GET.get(attribute_objectId, '')
    state = request.GET.get(attribute_state, -1)
    if objectId and 0 <= int(state) <= 3:
        settleInApplication = SettleInApplication()
        settleInApplication.get_Object(objectId)
        settleInApplication.set_attribute_state(int(state))
        shopType = settleInApplication.get_attribute_type()
        if int(state) == SETTLE_IN_STATE_2:
            # 通过认证
            user = _User()
            user.get_Object(settleInApplication.get_attribute_user())
            phoneNumber = user.get_attribute_mobilePhoneNumber()

            # 创建shop表单
            shop = Shop()
            data = {
                attribute_productGroup: None,
                attribute_shopProductGroup: None,
                attribute_order: None,
                attribute_address: '街道',
                attribute_province: '省',
                attribute_city: '市',
                attribute_district: '区',
                attribute_user: None,
                attribute_settleInUser: None,
                attribute_settleInCompany: None,
                attribute_phoneNumber: phoneNumber,
                attribute_mainImage: None,
                attribute_shopType: shopType,
                attribute_brand: '',
                attribute_type: 0,
                attribute_freightModel: None,
                attribute_afterSaleServiceRecord: None,
                attribute_name: 'menglive'
            }
            shop.create_Shop(data)

            # 将入驻信息写入店铺
            if shopType == SHOP_SETTLE_TYPE_0:
                info = settleInApplication.get_infoPersonal()
                shop.set_attribute_settleInUser(info)
                settleIn = SettleInUser()
            else:
                info = settleInApplication.get_infoCompany()
                shop.set_attribute_settleInCompany(info)
                settleIn = SettleInCompany()
            # 将店铺point写入入驻信息表中
            if info:
                settleIn.get_Object(info.id)
                settleIn.set_attribute_shop(shop.get_instance())

            # 写入用户与店铺
            shop.set_attribute_user(user.get_instance())
            user.set_attribute_shop(shop.get_instance())
        if int(state) == SETTLE_IN_STATE_1:
            settleInApplication.set_attribute_state(SETTLE_IN_STATE_1)
        return return_msg('success')
    return Parameter_Error(request, '参数错误')



@login_required
# @permission(ROLE_ADMINISTRATOR)
@require_http_methods(['GET'])
def sysUser(request):
    """
    显示所有系统用户
    :param request: 
    :return: 
    """
    page = request.GET.get(paginator_PAGE, 1)  # 获取页码
    user = _User()
    user_list = user.get_User_Role_All(ROLE_SYS, page)
    page_nums = user.count_User_Role_All(ROLE_SYS)

    return return_paginator_page(Class_Name_User, user_list, page, page_nums)


@login_required
# @permission(ROLE_ADMINISTRATOR)
@require_http_methods(['POST'])
def SysUserManager(request):
    """
    删除用户
    :param request: 
    :return: 
    """
    objectId = request.POST.get(attribute_objectId, '')
    if objectId:
        forbidden = request.POST.get(attribute_forbidden, '')
        state = request.POST.get(attribute_state, '')
        user = _User()
        user.get_Object(objectId)
        role = user.get_attribute_role()
        if forbidden == 'restore':
            user.set_attribute_forbidden(0)
        if forbidden == 'forbid':
            user.set_attribute_forbidden(1)
        if state:
            user.destroy_Object()
        if role:
            return return_msg(role[0])
    return illegal_access()


@login_required
# @permission(ROLE_ADMINISTRATOR)
@require_http_methods(['POST'])
def ResetUserPassword(request):
    """
    重置用户密码
    :param request: 
    :return: 
    """
    objectId = request.POST.get(attribute_objectId, '')
    password = request.POST.get(attribute_password, '')
    passwordSure = request.POST.get(attribute_passwordSure, '')
    if password == passwordSure and objectId:
        user = _User()
        user.get_Object(objectId)
        if user.set_attribute_password(password):
            return return_msg('success')
    return return_msg('fail')


# @csrf_exempt
@login_required
# @permission(ROLE_ADMINISTRATOR)
@require_http_methods(['POST', 'GET'])
def WebPage(request):
    if request.method == 'POST':
        webPageData = json.loads(request.body.decode('utf-8'))
        print(webPageData)
        if webPageData:
            WebPageConfigure().clear_all_WebPageConfigure()
            webPageData = webPageData[Class_Name_WebPageConfigure]
            print(webPageData)
            for foo in webPageData:
                webPage = WebPageConfigure()
                webPage.create_WebPageConfigure(foo)
    webPage = WebPageConfigure()
    webPageData = webPage.output_WebPageConfigure_All()
    return return_data(Class_Name_WebPageConfigure, webPageData)
