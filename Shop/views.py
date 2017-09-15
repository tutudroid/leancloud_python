from Error_Page import *
from ClassLibrary.ShopClass.Shop_New import Shop
from ClassLibrary.UserClass.User import _User
from ClassLibrary.ShopClass.BrandTable import BrandTable
from ClassLibrary.Frieght.FreightModel import FreightModel
from ClassLibrary.ShopClass.SettleInApplication import SettleInApplication
from rest_framework.views import APIView


def login(request):
    return render(request, 'sellerLogin.html')


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
        elif data[attribute_city] and data[attribute_district] and data[attribute_province] and data[attribute_address]:
            shop.set_attribute_city( data[attribute_city] )
            shop.set_attribute_province( data[attribute_province] )
            shop.set_attribute_district( data[attribute_district] )
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



@require_http_methods(['GET'])
def AllBrand(request):
    page = request.GET.get(paginator_PAGE, 1)
    objectId = request.GET.get(attribute_objectId, '')
    if page and objectId:
        shop = Shop()
        shop.get_Object(objectId)
        brandList = shop.get_attribute_brand()
        return return_data(Class_Name_BrandTable, brandList)
    return return_msg('parameter is error')


@require_http_methods(['POST'])
def EditBrand(request):
    brand = BrandTable()
    data = brand.input_Table(request)
    brand.update_Table(data)
    shopObjectId = request.POST.get('shopObjectId', None)
    if shopObjectId:
        shop = Shop()
        shop.get_Object(shopObjectId)
        shop.add_attribute_relation(attribute_freightModel, brand.get_instance())
    return return_msg(brand.output_Table())


@require_http_methods(['GET'])
def AllFreight(request):
    page = request.GET.get(paginator_PAGE, 1)
    objectId = request.GET.get(attribute_objectId, '')
    if page and objectId:
        shop = Shop()
        shop.get_Object(objectId)
        freightList = shop.get_attribute_freightModel()
        return return_data(Class_Name_FreightModel, freightList)
    return return_msg('parameter is error')


@require_http_methods(['POST'])
def EditFreight(request):
    freight = FreightModel()
    data = freight.input_Freight(request)
    freight.update_Freight(data)
    shopObjectId = request.POST.get('shopObjectId', None)
    if shopObjectId:
        shop = Shop()
        shop.get_Object(shopObjectId)
        shop.add_attribute_relation(attribute_freightModel, freight.get_instance())
    return return_msg(freight.output_FreightModel())


@require_http_methods(['GET'])
def AllActivities(request):
    return return_msg('parameter is error')


@require_http_methods(['POST'])
def EditActivities(request):
    return return_msg()



class brand(APIView):
    def get(self, request):
        """
        显示所有店铺品牌
        :param request: 
        :return: 
        """
        pass

    def post(self, request):
        """
        创建新的品牌
        :param request: 
        :return: 
        """
        pass


class brandDetail(APIView):
    def get(self, request, objectId):
        """
        获得品牌信息
        :param request: 
        :param objectId: 
        :return: 
        """
        pass

    def put(self, request, objectId):
        """
        更新品牌信息
        :param request: 
        :param objectId: 
        :return: 
        """
        pass

    def delete(self, request, objectId):
        """
        删除某个品牌
        :param request: 
        :param objectId: 
        :return: 
        """
        pass



class shop(APIView):
    def get(self, request):
        """
        显示所有店铺信息
        :param request: 
        :return: 
        """
        page = request.GET.get(paginator_PAGE, 1)
        shop = Shop()
        shopList = shop.get_Shop_All(page)
        count = shop.count_Shop_All()
        return return_paginator_page(Class_Name_Shop, shopList, page, count)

    def post(self, request):
        """
        创建新的店铺
        :param request: 
        :return: 
        """
        pass


class shopDetail(APIView):
    def get(self, request, objectId):
        """
        显示店铺详情
        :param request: 
        :param objectId: 
        :return: 
        """
        pass

    def put(self, request, objectId):
        """
        更新店铺信息
        :param request: 
        :param objectId: 
        :return: 
        """
        pass

    def delete(self, request, objectId):
        """
        删除某个店铺
        :param request: 
        :param objectId: 
        :return: 
        """
        pass


"""
shop/objectId/brand/objectId

"""