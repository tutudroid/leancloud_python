
from Error_Page import *

from ClassLibrary.ProductClass.ShopProductGroup import ShopProductGroup
from ClassLibrary.ShopClass.Shop_New import Shop
from ClassLibrary.ProductClass.ProductService import ProductService
from ClassLibrary.CategoryClass.SaleCategory import SaleCategory
from ClassLibrary.CategoryClass.StoreCategory import StoreCategory
from ClassLibrary.ProductClass.ShopProduct import ShopProduct


@login_required
@permissions([ROLE_SHOP, ROLE_PRODUCT])
@require_http_methods(['GET'])
def Shop_All_ProductGroup(request):
    """
    显示所有商品
    :param request: 
    :return: 
    """
    # 设置分页
    state = request.GET.get(attribute_state, 1)
    objectId = request.GET.get(attribute_objectId, '')
    page = request.GET.get(paginator_PAGE, 1)
    if objectId:
        shop = Shop()
        shop.get_Object(objectId)
        productGroup = shop.get_attribute_productGroup(int(state), page)
        page_nums = shop.count_attribute_productGroup(int(state))
        return return_paginator_page(Class_Name_ProductGroup, productGroup, page, page_nums)
    return illegal_access()


@login_required
@permissions([ROLE_SHOP, ROLE_PRODUCT])
@require_http_methods(['GET'])
def Shop_All_ShopProductGroup(request):
    """
    显示所有商品
    :param request: 
    :return: 
    """
    # 设置分页
    objectId = request.GET.get(attribute_objectId, '')
    page = request.GET.get(paginator_PAGE, 1)
    if objectId:
        shop = Shop()
        shop.get_Object(objectId)
        productGroup = shop.get_attribute_shopProductGroup(page)
        page_nums = shop.count_attribute_shopProductGroup()
        return return_paginator_page(Class_Name_ProductGroup, productGroup, page, page_nums)
    return illegal_access()


@login_required
@permission(ROLE_SHOP)
def createProductGroup(request):
    """
    创建商品组
    :param request: 
    :return: 
    """
    content = PROFILE_INIT()
    if request.method == 'POST':
        # 增加商品到店铺中
        content['shop']['objectId'] = request.POST.get('_shopObjectId')
        # 创建商品组
        shopObjectId = request.POST.get('_shopObjectId')
        if shopObjectId is None:
            return illegal_access()
        shop = Shop()
        shop.get_Object(shopObjectId)
        if request.POST.get('audit'):
            shopProductGroup = ShopProductGroup()
            data = shopProductGroup.input_ProductGroup(request)
            productGroup = ShopProductGroup.create_ProductGroup(data, shop)
            if productGroup:
                return HttpResponseRedirect('/TmpProductGroup/ProductGroupDetail/?productGroupObjectId='+ShopProductGroup.get_attribute_objectId(productGroup))
            else:
                content['return'] = {
                    'message': '创建失败，请检查重新创建商品',
                }
                return render(request, 'result.html', {'content': content})
    if request.method == 'GET':
        # 显示创建商品页面
        if request.GET.get('_shopObjectId'):
            content['data']['shopObjectId'] = request.GET.get('_shopObjectId')
            content['data']['storeCategory'] = StoreCategory().get_StoreCategory_All()
            content['data']['saleCategory'] = SaleCategory().getSaleCategory_All()
            content['data']['productService'] = ProductService().get_ProductService_All()
            return render(request, 'NewCreateProduct.html', {'content': content})
        return illegal_access()



@login_required
@permission(ROLE_SHOP)
def editProductGroup(request):
    """
    编辑商品组
    :param request: 
    :return: 
    """
    content = PROFILE_INIT()
    if request.method == "POST" and request.POST.get('productGroupObjectId'):
        # 获得productGroupObjectId
        productGroupObjectId = request.POST.get('productGroupObjectId')
        shopProductGroup = ShopProductGroup()
        data = shopProductGroup.input_ProductGroup(request)
        shopProductGroup.get_Object(productGroupObjectId)
        shopProductGroup.update_ProductGroup(data)
        return HttpResponseRedirect(reverse("TmpProductGroup:ProductGroupDetail")+'?productGroupObjectId='+productGroupObjectId)
    if request.method == 'GET':
        productGroupObjectId = request.GET.get('productGroupObjectId')
        if productGroupObjectId:
            content['data']['storeCategory'] = StoreCategory().get_StoreCategory_All()
            content['data']['saleCategory'] = SaleCategory().getSaleCategory_All()
            content['data']['productService'] = ProductService().get_ProductService_All()

            # 产生数据，输出到前端
            shopProductGroup = ShopProductGroup()
            shopProductGroup.get_Object(productGroupObjectId)

            content['productGroup'] = shopProductGroup.output_ProductGroup()
            productList = content['productGroup']['product']
            if productList:
                tmpProduct = []
                for foo in productList:
                    product = ShopProduct()
                    product.set_instance(foo)
                    tmpProduct.append(product.output_Product())
                content['productList'] = tmpProduct
            return render(request, 'NewEditProduct.html', {'content': content})
    return illegal_access()


@login_required
@require_http_methods(['GET'])
@permissions([ROLE_SHOP, ROLE_PRODUCT])
def productGroupDetail(request):
    """
    商品组详情
    :param request: 
    :return: 
    """
    content = PROFILE_INIT()
    productGroupObjectId = request.GET.get('productGroupObjectId')
    if productGroupObjectId:
        shopProductGroup = ShopProductGroup()
        shopProductGroup.get_Object(productGroupObjectId)
        if shopProductGroup.get_instance():
            content['productGroup'] = shopProductGroup.output_ProductGroup()
            if content['productGroup'] and shopProductGroup.get_attribute_shop():
                content['productGroup']['commentCount'] = shopProductGroup.get_attribute_comment_count(productGroupObjectId, attribute_state, STATE_OK)
                return render(request, 'newProductDetail.html', {'content': content})
            else:
                return illegal_access()
        else:
            return illegal_access()
    else:
        return illegal_access()