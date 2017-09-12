from Error_Page import *
from ClassLibrary.ProductClass.ProductGroup_New import ProductGroup, copy_Shop_ProductGroup
from ClassLibrary.ShopClass.Shop_New import Shop
from ClassLibrary.ProductClass.ShopProductGroup import ShopProductGroup
from ClassLibrary.CategoryClass.SaleCategoryFirst import get_SaleCategory_All
from ClassLibrary.CategoryClass.StoreCategoryFirst import get_StoreCategory_All
from ClassLibrary.CategoryClass.SaleCategorySecond import SaleCategorySecond
from ClassLibrary.CategoryClass.StoreCategoryThird import StoreCategoryThird
from ClassLibrary.ProductClass.ProductService import ProductService


@login_required
@require_http_methods(['GET'])
def ProductGroupDetail(request):
    """
    商品组详情
    :param request: 
    :return: 
    """
    objectId = request.GET.get(attribute_objectId)
    if objectId:
        productGroup = ProductGroup()
        if productGroup.get_Object(objectId):
            productGroupData = productGroup.output_ProductGroup()
            content = PROFILE_INIT()
            content['productGroup'] = productGroupData
            return render( request, 'NewProductDetail.html', {'content': content} )
    return return_msg('parameter is error')


@login_required
@require_http_methods(['GET'])
def ProductGroupBriefDetail(request):
    objectId = request.GET.get(attribute_objectId)
    if objectId:
        productGroup = ProductGroup()
        if productGroup.get_Object(objectId):
            productGroupData = productGroup.output_ProductGroup_Simple()
            return return_data(Class_Name_ProductGroup, productGroupData)
    return return_msg('parameter is error')


@login_required
@require_http_methods(['GET'])
def ShopAllProductGroup(request):
    """
    显示所有商品
    :param request: 
    :return: 
    """
    state = request.GET.get(attribute_state, 0)
    objectId = request.GET.get(attribute_objectId)
    page = request.GET.get(paginator_PAGE)
    shop = Shop()
    if shop.get_Object(objectId) and state is not None:
        productGroupData = shop.get_attribute_productGroup(int(state), int(page))
        count = shop.count_attribute_productGroup(int(state))
        return return_paginator_page(Class_Name_ProductGroup, productGroupData, page, count)
    return return_msg('parameter is null')


@login_required
@permissions([ROLE_SHOP, ROLE_PRODUCT])
@require_http_methods(['GET'])
def ShopAllShopProductGroup(request):
    """
    显示所有商品
    :param request: 
    :return: 
    """
    # 设置分页
    objectId = request.GET.get(attribute_objectId, '')
    page = request.GET.get(paginator_PAGE, 1)
    shop = Shop()
    if shop.get_Object(objectId):
        productGroup = shop.get_attribute_shopProductGroup(page)
        page_nums = shop.count_attribute_shopProductGroup()
        return return_paginator_page(Class_Name_ShopProductGroup, productGroup, page, page_nums)
    return return_msg('no found shop')


@login_required
@permissions([ROLE_PRODUCT])
@require_http_methods(['GET'])
def AuditProductGroup(request):
    objectId = request.GET.get(attribute_objectId)
    shopProductGroup = ShopProductGroup()
    state = request.GET.get(attribute_state)
    if shopProductGroup.get_Object(objectId) and 0 <= int(state) <= 1:

        # 通过审核
        shopObjectId = shopProductGroup.get_attribute_Object_Id(attribute_shop)
        productGroup1 = copy_Shop_ProductGroup(shopProductGroup)

        # 获得店铺信息
        if productGroup1:
            shop = Shop()
            shop.get_Object(shopObjectId)

            # 将productGroup关联到shop中
            if shop.add_attribute_relation(attribute_productGroup, productGroup1):
                shopProductGroup.destroy_ProductGroup()
                return return_msg('success')
            else:
                productGroup1.destroy_ProductGroup()
            return return_msg('can\'t save to shop')
    return return_msg('parameter is error')


@login_required
@not_permission(ROLE_BUSINESS)
@not_permission(ROLE_CUSTOM)
@not_permission(ROLE_ADMINISTRATOR)
def CreateProductGroup(request):
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
                productGroup1 = ProductGroup()
                data = productGroup1.input_ProductGroup(request)
                # 将数据保存到数据库
                if productGroup1.create_ProductGroup(data):
                    if request.POST.get('shelf_off'):
                        ProductGroup.set_attribute_state(productGroup1, STATE_SHELF_OFF)
                    productGroup1.set_attribute_value(attribute_shop, shop.get_instance())
                    shop.add_attribute_relation(attribute_productGroup, productGroup1.get_instance())
                    productGroupObjectId = ProductGroup.get_attribute_objectId(productGroup1)
                    return HttpResponseRedirect('/Product/ProductGroupDetail/?objectId='+productGroupObjectId)
    if request.method == 'GET' and request.GET.get('shopObjectId'):
        content = PROFILE_INIT()
        # 显示创建商品页面
        data = {
            'current_role': 'ProductAdmin',
            'shopObjectId': request.GET.get('shopObjectId'),
            'storeCategory': get_StoreCategory_All(),
            'saleCategory': get_SaleCategory_All(),
            'productService': ProductService().get_ProductService_All(),
        }
        content['data'] = data
        return render(request, 'NewCreateProduct.html', {'content': content})
    return illegal_access()


@login_required
@permissions([ROLE_PRODUCT])
def EditProductGroup(request):
    """
    编辑商品组
    :param request: 
    :return: 
    """
    content = PROFILE_INIT()
    productGroup = ProductGroup()
    objectId = request.POST.get(attribute_objectId)
    if request.method == "POST" and objectId:
        # 获得productGroupObjectId
        if productGroup.get_Object(objectId):
            data = productGroup.input_ProductGroup(request)
            productGroup.update_ProductGroup(data)
            return HttpResponseRedirect(reverse("Product:ProductGroupDetail")+'?objectId='+objectId)
    if request.method == 'GET':
        objectId = request.GET.get('objectId')
        if objectId:
            # 产生数据，输出到前端
            if productGroup.get_Object(objectId):
                content = {
                    'profile': {
                        'current_role':'ProductAdmin'
                    },
                    'shopObjectId': request.GET.get('shopObjectId'),
                    'storeCategory': get_StoreCategory_All(),
                    'saleCategory': get_SaleCategory_All(),
                    'productService': ProductService().get_ProductService_All(),
                    'productGroup': productGroup.output_ProductGroup(),
                    'range': range( 1, 100 ),
                }
                print(content['productGroup']['saleCategory'])
                print(content['saleCategory'])
                productList = content['productGroup']['product']
                content['productList'] = productList
                content['propertyOption'] = productGroup.get_attribute(attribute_propertyOption)
                return render(request, 'NewEditProduct.html', {'content': content})
    content['message'] = '数据无效，请重新提交'
    return render( request, 'result.html', {'content': content} )


@login_required
@permission(ROLE_PRODUCT)
@require_http_methods(['GET'])
def DisposeProductGroup(request):
    objectId = request.GET.get(attribute_objectId, '')
    state = request.GET.get(attribute_state, '')
    if objectId and state:
        productGroup1 = ProductGroup()
        if productGroup1.get_Object(objectId):
            if 0 <= int(state) <= 1:
                productGroup1.set_attribute_state(int(state))
                return return_msg('success')
            if int(state) == -1:
                # 从店铺关系表中删除商品
                shop = Shop()
                shop.get_Object(productGroup1.get_attribute_Object_Id(attribute_shop))
                shop.remove_attribute_relation(attribute_productGroup, productGroup1.get_instance())
                # 从库存中删除
                store = StoreCategoryThird()
                store.get_Object(productGroup1.get_attribute_Object_Id(attribute_storeCategory))
                store.remove_attribute_relation(attribute_productGroup, productGroup1.get_instance())
                # 从销售分类中删除
                saleList = productGroup1.get_attribute_relation(attribute_saleCategory)
                if saleList:
                    for foo in saleList:
                        sale = SaleCategorySecond()
                        sale.set_instance(foo)
                        sale.remove_attribute_relation(attribute_productGroup, productGroup1.get_instance())
                productGroup1.delete_ProductGroup()
                return return_msg('success')
        return return_msg('no found productGroup')
    return return_msg('parameter is error')


@login_required
@require_http_methods(['GET'])
def ShowComments(request):
    objectId = request.GET.get(attribute_objectId, '')
    page = request.GET.get(paginator_PAGE, 1)
    if page and objectId:
        productGroup = ProductGroup()
        productGroup.get_Object(objectId)
        comment = productGroup.get_attribute_comment(attribute_state, STATE_OK, int(page))
        commentCount = productGroup.get_attribute_comment_count(attribute_state, STATE_OK)
        return return_paginator_page(Class_Name_ProductComment, comment, page, commentCount)
    return return_msg('parameter is error')


@login_required
def SearchProductGroup(request):
    return render(request, 'SearchProductGroup.html')
