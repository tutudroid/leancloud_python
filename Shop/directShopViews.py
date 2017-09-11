from Error_Page import *
from ClassLibrary.BaseClass.Attribute_Parameter import *
from ClassLibrary.ShopClass.Shop_New import Shop
from ClassLibrary.ShopClass.BrandTable import BrandTable


@login_required
#@permission(ROLE_ADMINISTRATOR)
@require_http_methods(['POST'])
def InitiateDirectShop(request):
    """
    显示所有的入驻信息
    :param request:
    {
        shopName: xxx,
        phoneNumber: xxx,
        name: xxxx,
        imageFile: xxx,
        briefDescription: xxx,
    }
    :return: 
        shopList
    """
    shop = Shop()
    name = request.GET.get(attribute_name, '')
    phoneNumber = request.GET.get(attribute_phoneNumber, '')
    if name and len(phoneNumber) == 11 and phoneNumber.isdigit():
        brand = BrandTable()
        data = brand.input_Table(request)
        if brand.create_Table(data):
            shop.create_Object()
            shop.set_attribute_brand(brand.get_instance())
            shop.set_attribute_name(name)
            shop.set_attribute_phoneNumber(phoneNumber)
            shop.set_attribute_type(SHOP_TYPE_1)
            return return_msg('success')
    return return_msg('parameter is error')


@login_required
#@permission(ROLE_ADMINISTRATOR)
@require_http_methods(['GET'])
def EditDirectShop(request):
    """
    """
    objectId = request.GET.get(attribute_objectId, '')
    name = request.GET.get(attribute_name, '')
    phoneNumber = request.GET.get(attribute_phoneNumber, '')
    if objectId and name and len(phoneNumber) == 11 and phoneNumber.isdigit():
        shop = Shop()
        if shop.get_Object(objectId):
            shop.set_attribute_name(name)
            shop.set_attribute_phoneNumber(phoneNumber)
            return_msg('success')
    return return_msg('parameter is error')


@login_required
#@permission(ROLE_ADMINISTRATOR)
@require_http_methods(['POST'])
def DirectShop(request):
    """
    """
    shop = Shop()
    if shop.get_Direct_Shop():
        return return_data(Class_Name_Shop, shop.output_Shop())
    return return_msg('no found direct shop')
