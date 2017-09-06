from Error_Page import *
from ClassLibrary.ShopClass.Shop_New import Shop
from ClassLibrary.UserClass.User import _User
from ClassLibrary.ShopClass.BrandTable import BrandTable
from ClassLibrary import Base
from ClassLibrary.ShopClass.SettleInApplication import SettleInApplication



def login(request):
    return render(request, 'login.html')


@login_required
@permission(ROLE_SHOP)
def ShopDetail(request):
    """
    显示店铺详情
    :param request: 
    :return: 
    """
    user = _User()
    user.set_instance(leancloud.User.get_current())
    shop = user.get_attribute_shop()
    return HttpResponse(shop, content_type='Application/Json')


@login_required
@permission(ROLE_SHOP)
@require_http_methods(['POST'])
def EditShopDetail(request):
    """
    显示店铺详情
    :param request: 
    :return: 
    """
    brand = request.POST.get(attribute_brand, '')
    if brand:
        brand = BrandTable()
        data = brand.input_Table(request)
        brand.update_Table(data)
    else:
        shop = Shop()
        data = shop.input_Shop(request)
        shop.get_Object(data[attribute_objectId])
        if data[attribute_name]:
            shop.set_attribute_name(attribute_name)
        elif data[attribute_CITY] and data[attribute_DISTRICT] and data[attribute_PROVINCE] and data[attribute_address]:
            shop.set_attribute_city(data[attribute_CITY])
            shop.set_attribute_province(data[attribute_PROVINCE])
            shop.set_attribute_district(data[attribute_DISTRICT])
            shop.set_attribute_address(data[attribute_address])
    return HttpResponse('success')


@login_required
@permission(ROLE_SHOP)
@require_http_methods(['GET'])
def shopAfterSale(request):
    """
    获得店铺中的所有售后记录
    :param request: 
    :return: 
    """
    objectId = request.GET.get(attribute_objectId, '')
    page = request.GET.get(paginator_PAGE, 1)
    state = request.GET.get(attribute_state, -1)
    if objectId:
        shop = Shop()
        if shop.get_Object(objectId):
            # 设置分页
            page_nums = shop.count_attribute_afterSaleServiceRecord(state)
            afterSaleList = shop.get_attribute_afterSaleServiceRecord(state, page)
            return return_paginator_page(Class_Name_AfterSaleServiceRecord, afterSaleList, page, page_nums)
        return return_msg('no found shop')
    return return_msg('parameter is null')


@require_http_methods(["POST"])
def register(request):
    """
    :param request: 
    :return: 
    """
    verifyCode = request.POST.get(attribute_verifyCode)
    phoneNumber = request.POST.get(attribute_phoneNumber)
    if verifyCode:
        try:
            leancloud.cloudfunc.verify_sms_code(phoneNumber, verifyCode)
            # 创建用户
            user = _User()
            data = user.input_User(request)
            user.create_User(data)
            # 创建SettleInApplication
            settleInApplication = SettleInApplication()
            settleInApplication.create_Object()
            settleInApplication.set_attribute_user(user.get_instance())
            return HttpResponse('success')
        except LeanCloudError as e:
            message = e.error
        return HttpResponse(message)
    return illegal_access()


@login_required
@permissions([ROLE_SHOP])
@require_http_methods(['POST'])
def changePhoneNumber(request):
    """
    改变用户的手机号
    :param request: 
    :return: 
    """
    phoneNumber = request.POST.get(attribute_phoneNumber)
    verifyCode = request.POST.get(attribute_verifyCode)
    phoneNumber_new = request.POST.get(attribute_phoneNumber_New)
    if len(phoneNumber) == 11 and phoneNumber.isdigit():
        try:
            leancloud.cloudfunc.verify_sms_code(phoneNumber, verifyCode)
            user = _User()
            user.get_User_phoneNumber(phoneNumber)
            if len(phoneNumber_new) == 11 and phoneNumber_new.isdigit():
                user.set_attribute_mobilePhoneNumber(phoneNumber_new)
                shop = Shop()
                shop.get_Object(user.get_shop())
                shop.set_attribute_phoneNumber(phoneNumber_new)
                return HttpResponse('success')
        except LeanCloudError as e:
            return HttpResponse(e.error)
    return illegal_access()


@login_required
@require_http_methods(['POST'])
def modifyPassword_Username(request):
    """
    商家，修改密码
    :param request: 
    :return: 
    """
    phoneNumber = request.POST.get(attribute_phoneNumber, '')
    verifyCode = request.POST.get(attribute_verifyCode, '')
    password = request.POST.get(attribute_password, '')
    passwordSure = request.POST.get(attribute_passwordSure, '')
    username = request.POST.get(attribute_username, '')
    if len(phoneNumber) == 11 and phoneNumber.isdigit() and password == passwordSure:
        try:
            leancloud.cloudfunc.verify_sms_code(phoneNumber, verifyCode)
        except LeanCloudError as e:
            return HttpResponse(e.error)
        try:
            user = _User()
            user.get_User_phoneNumber(phoneNumber)
            current_user = leancloud.User.get_current()
            if current_user == user.get_instance():
                user.set_attribute_password(password)
                user.logout()
        except LeanCloudError as e:
            return HttpResponse(e.error)
        return HttpResponse('success')
    if username:
        user = _User()
        current_user = leancloud.User.get_current()
        user.set_instance(current_user)
        user.set_attribute_username(username)
        return HttpResponse('success')
    return HttpResponse('fail')


@require_http_methods(['GET'])
def AllForbiddenShop(request):
    page = request.GET.get(paginator_PAGE, 1)
    state = request.GET.get(attribute_state, 1)
    if state and int(state) == 1:
        shop = Shop()
        shopList = shop.get_shop_state(state, page)
        return return_paginator_page(Class_Name_Shop, shopList, page, shop.count_shop_state(state))
    return return_msg('parameter is error')
