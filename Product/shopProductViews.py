
from Error_Page import *

from ClassLibrary.ProductClass.ShopProductGroup import ShopProductGroup
from ClassLibrary.ShopClass.Shop_New import Shop
from ClassLibrary.ProductClass.ProductService import ProductService
from ClassLibrary.CategoryClass.SaleCategoryFirst import get_SaleCategory_All
from ClassLibrary.CategoryClass.StoreCategoryFirst import get_StoreCategory_All


@login_required
@permission(ROLE_SHOP)
def CreateShopProductGroup(request):
    """
    创建商品组, 或者修改商品组
    :param request: 
    :return: 
    """
    shop = Shop()
    if request.method == 'POST':
        # 增加商品到店铺中
        # 创建商品组
        shopObjectId = request.POST.get('shopObjectId', '')
        if shopObjectId and shop.get_Object(shopObjectId):
            # 从前端获取数据
            productGroup1 = ShopProductGroup()
            data = productGroup1.input_ProductGroup(request)
            # 将数据保存到数据库
            if productGroup1.create_ProductGroup(data):
                productGroup1.set_attribute_value(attribute_shop, shop.get_instance())
                shop.add_attribute_relation(attribute_shopProductGroup, productGroup1.get_instance())
                productGroupObjectId = productGroup1.get_attribute_objectId()
                return HttpResponseRedirect('/Product/ShopProductGroupDetail/?objectId='+productGroupObjectId)
    if request.method == 'GET' and request.GET.get('shopObjectId'):
        content = PROFILE_INIT()
        # 显示创建商品页面
        data = {
            'current_role': 'Shop',
            'shopObjectId': request.GET.get('shopObjectId'),
            'storeCategory': get_StoreCategory_All(),
            'saleCategory': get_SaleCategory_All(),
            'productService': ProductService().get_ProductService_All(),
            'brand': shop.get_attribute_brand(),
            'freightModel': shop.get_attribute_freightModel(),
        }
        content['data'] = data
        return render(request, 'NewCreateProduct.html', {'content': content})
    return illegal_access()


@login_required
@permissions([ROLE_SHOP])
def EditShopProductGroup(request):
    """
    编辑商品组
    :param request: 
    :return: 
    """
    content = PROFILE_INIT()
    productGroup = ShopProductGroup()
    objectId = request.POST.get(attribute_objectId)
    if request.method == "POST" and objectId:
        # 获得productGroupObjectId
        if productGroup.get_Object(objectId):
            data = productGroup.input_ProductGroup(request)
            productGroup.update_ProductGroup(data)
            return HttpResponseRedirect(reverse("Product:ShopProductGroupDetail")+'?objectId='+objectId)
    if request.method == 'GET':
        objectId = request.GET.get(attribute_objectId)
        if objectId:
            # 产生数据，输出到前端
            if productGroup.get_Object(objectId):
                shopObjectId = productGroup.get_attribute_Object_Id(attribute_shop)
                shop = Shop()
                if shop.get_Object(shopObjectId):
                    content = {
                        'profile': {
                            'current_role': 'Shop'
                        },
                        'productGroup': productGroup.output_ProductGroup(),
                        'range': range(1, 100),
                    }
                    data = {
                        'current_role': 'Shop',
                        'shopObjectId': request.GET.get( 'shopObjectId' ),
                        'storeCategory': get_StoreCategory_All(),
                        'saleCategory': get_SaleCategory_All(),
                        'productService': ProductService().get_ProductService_All(),
                        'brand': shop.get_attribute_brand(),
                        'freightModel': shop.get_attribute_freightModel(),
                    }
                    content['data'] = data
                    productList = content['productGroup']['product']
                    content['productList'] = productList
                    content['propertyOption'] = productGroup.get_attribute(attribute_propertyOption)
                    return render(request, 'NewEditProduct.html', {'content': content})
    content['message'] = '数据无效，请重新提交'
    return render(request, 'result.html', {'content': content})


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
            content = PROFILE_INIT()
            content['productGroup'] = data
            return render(request, 'NewProductDetail.html', {'content': content})
    return return_msg('parameter is error')
