
from Error_Page import *

from ClassLibrary.ProductClass.ShopProductGroup import ShopProductGroup
from ClassLibrary.ShopClass.Shop_New import Shop
from ClassLibrary.ProductClass.ProductService import ProductService
from ClassLibrary.CategoryClass.SaleCategory import SaleCategory
from ClassLibrary.CategoryClass.StoreCategory import StoreCategory
from ClassLibrary.ProductClass.ShopProduct import ShopProduct





@login_required
@permission(ROLE_SHOP)
def CreateShopProductGroup(request):
    """
    创建商品组, 或者修改商品组
    :param request: 
    :return: 
    """
    if request.method == 'POST':
        # 增加商品到店铺中
        # 创建商品组
        shopObjectId = request.POST.get('shopObjectId', '')
        shop = Shop()
        if shopObjectId and shop.get_Object(shopObjectId):
            if request.POST.get('shelf_on') or request.POST.get('shelf_off'):
                # 从前端获取数据
                productGroup1 = ShopProductGroup()
                data = productGroup1.input_ProductGroup(request)
                # 将数据保存到数据库
                if productGroup1.create_ProductGroup(data, shop):
                    if request.POST.get('shelf_off'):
                        productGroup1.set_attribute_state(STATE_SHELF_OFF)
                    productGroupObjectId = productGroup1.get_attribute_objectId()
                    return HttpResponseRedirect('/Product/ShopProductGroupDetail/?objectId='+productGroupObjectId)
                return return_msg('msg is error')
    if request.method == 'GET':
        # 显示创建商品页面
        data = {
            Class_Name_StoreCategory: StoreCategory().get_StoreCategory_All(),
            Class_Name_SaleCategory: SaleCategory().get_SaleCategory_All(),
            Class_Name_ProductService: ProductService().get_ProductService_All(),
        }
        return return_data(Class_Name_ProductGroup, data)


@login_required
@permissions([ROLE_SHOP])
def EditShopProductGroup(request):
    """
    编辑商品组
    :param request: 
    :return: 
    """
    objectId = request.POST.get(attribute_objectId)
    if request.method == "POST" and objectId:
        # 获得productGroupObjectId
        productGroup = ShopProductGroup()
        if productGroup.get_Object(objectId):
            data = productGroup.input_ProductGroup(request)
            productGroup.update_ProductGroup(data)
            return HttpResponseRedirect(reverse("Product:ShopProductGroupDetail")+'?objectId='+objectId)
        return return_msg('no found productGroup')
    return return_msg('parameter is error')


@login_required
@require_http_methods(['GET'])
@permissions([ROLE_SHOP, ROLE_PRODUCT])
def ShopProductGroupDetail(request):
    """
    商品组详情
    :param request: 
    :return: 
    """
    objectId = request.GET.get(attribute_objectId, '')
    if objectId:
        shopProductGroup = ShopProductGroup()
        if shopProductGroup.get_Object(objectId):
            data = shopProductGroup.output_ProductGroup()
            return return_data(Class_Name_ShopProductGroup, data)
        return return_msg('no found shopProductGroup')
    return return_msg('parameter is error')
