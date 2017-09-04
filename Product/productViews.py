import re
from Product.library.category import getStoreCategory, getSaleCategory
from Product.library import productGroup, base
from Product.library.base import sys_log
from Product.library import category
from Error_Page import *
import Error_Page
#
RETURN_CONTENT = 'content'


# 只能店铺调用
@login_required
@require_http_methods(['GET'])
def shop_ProductGroup(request):
    """
    显示所有商品
    :param request: 
    :return: 
    """
    content = PROFILE_INIT()
    user = leancloud.User.get_current()
    # 设置分页
    page = request.GET.get(paginator_PAGE)

    page_nums = request.GET.get('page_nums')
    # 从用户获得店铺
    shop = User.get_attribute_shop(user)
    # 从店铺获得店铺的objectId
    shopObjectId = Shop.get_attribute_objectId(shop)
    state = ProductGroup.STATE_OK
    if request.GET.get('state'):
        state = int(request.GET.get('state'))
    if page:
        paginator1 = base.paginator_private(page, page_nums, None)
    else:
        paginator1 = base.paginator_private(None, page_nums, Shop.count_attribute_productGroup(shop, state))
        page = 1
    print(paginator1)
    content.update({'paginator': paginator1})

    content['productGroup'] = Shop.get_attribute_productGroup(shop, page, state)
    shopInstance = Shop.get_Shop(shopObjectId)
    content['shop'] = Shop.output_Shop(shopInstance)
    return render(request, 'AllProduct.html', {'content': content})


@login_required
@not_permission(ROLE_BUSINESS)
@not_permission(ROLE_CUSTOM)
@not_permission(ROLE_ADMINISTRATOR)
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
            return Error_Page.illegal_access()

        if request.POST.get('shelf_on') or request.POST.get('shelf_off'):
            # 从前端获取数据
            data = ProductGroup.get_data(request)
            # 将数据保存到数据库
            productGroup1 = ProductGroup.create_newProductGroup(data, shopObjectId)
            if productGroup1:
                if request.POST.get('shelf_off'):
                    ProductGroup.set_attribute_state(productGroup1, ProductGroup.STATE_SHELF_OFF)
                productGroupObjectId = ProductGroup.get_attribute_objectId(productGroup1)
                return HttpResponseRedirect('/Product/ProductGroupDetail/?productGroupObjectId='+productGroupObjectId)

            content['return'] = {
                'message': '数据无效，请重新提交',
            }
            return render(request, 'result.html', {'content': content})
    if request.method == 'GET':
        # 删除一件商品
        if request.GET.get('productGroupObjectId') and request.GET.get('delete'):
            productGroupObjectId = request.GET.get('productGroupObjectId')
            shopObjectId = ProductGroup.delete_ProductGroup(productGroupObjectId)
            address = reverse("Shop:AllShop") + '?objectId=' + str(shopObjectId)
            return HttpResponseRedirect(address)

        # 显示创建商品页面
        if request.GET.get('_shopObjectId'):
            content['data']['shopObjectId'] = request.GET.get('_shopObjectId')
            content['data']['storeCategory'] = getStoreCategory()
            content['data']['saleCategory'] = getSaleCategory()
            content['data']['productService'] = ProductGroup.get_productService_All()
            return render(request, 'NewCreateProduct.html', {'content': content})
    return Error_Page.illegal_access()


@login_required
@require_http_methods(['GET'])
def productGroupDetail(request):
    """
    商品组详情
    :param request: 
    :return: 
    """
    content = PROFILE_INIT()
    productGroupObjectId = request.GET.get('productGroupObjectId')
    if productGroupObjectId:
        productGroupInstance = ProductGroup.get_ProductGroup(productGroupObjectId)
        if productGroupInstance:
            content['productGroup'] = ProductGroup.output_ProductGroup(productGroupInstance)
            if content['productGroup']:
                shop = ProductGroup.get_attribute_shop(productGroupInstance)
                shopInstance = Shop.get_Shop(Shop.get_attribute_objectId(shop))
                content['shop'] = Shop.output_Shop(shopInstance)
                content['productGroup']['shopUniqueId'] = Shop.get_attribute_uniqueId(shopInstance)
                count = ProductGroup.get_attribute_comment_count(productGroupObjectId, ProductComment.Attribute_state, ProductComment.STATE_OK)
                productCommentList = ProductGroup.get_attribute_comment(productGroupObjectId, ProductGroup.Attribute_state, 0, 1, 10)
                content['productGroup']['productCommentList'] = [
                        ProductComment.output_Recommend(foo) for foo in productCommentList
                    ]
                """
                评论换页
                """
                content['productGroup']['commentCount'] = count
                count = ProductGroup.get_attribute_comment_count(productGroupObjectId, ProductGroup.Attribute_state, 0)
                paginator1 = base.paginator_private(None, None, count)
                content.update({'paginator': paginator1})
                return render(request, 'newProductDetail.html', {'content': content})
            else:
                return Error_Page.Parameter_Error()
        else:
            return Error_Page.Parameter_Error()
    return Error_Page.illegal_access()



@login_required
def ProductGroupBriefDetail(request):
    if request.method == 'GET':
        productGroupId = request.GET.get('productGroupId')
        if productGroupId:
            productGroup1 = ProductGroup.get_ProductGroup_UniqueId(productGroupId)
            productGroupData = ProductGroup.output_ProductGroup_Simple(productGroup1)
            return render(request, 'ProductGroup_Simple.html', {'productGroup': productGroupData})
        else:
            return Error_Page.Parameter_Error()
    else:
        return Error_Page.illegal_access()


@login_required
@permission(ROLE_PRODUCT)
@require_http_methods(['GET'])
def DisposeProductGroup(request):
    productGroupId = request.GET.get('productGroupObjectId')
    if request.GET.get('shelf_on') or request.GET.get('shelf_off'):
        if productGroupId:
            productGroup1 = ProductGroup.get_ProductGroup(productGroupId)
            if productGroup1:
                shopPoint = ProductGroup.get_attribute_shop(productGroup1)
                if request.GET.get('shelf_on'):
                    ProductGroup.set_attribute_state(productGroup1, int(ProductGroup.STATE_SHELF_ON))
                    return HttpResponseRedirect('/Shop/AllShop/?objectId='+shopPoint.id)
                if request.GET.get('shelf_off'):
                    ProductGroup.set_attribute_state(productGroup1, int(ProductGroup.STATE_SHELF_OFF))
                    return HttpResponseRedirect('/Shop/AllShop/?objectId='+shopPoint.id)
            return HttpResponse('商品不存在')
    return Error_Page.illegal_access()


@login_required
@permissions([ROLE_PRODUCT])
@require_http_methods(['GET'])
def AuditProductGroup(request):
    content = PROFILE_INIT()
    if request.method == 'GET' and request.GET.get('productGroupObjectId'):
        productGroupId = request.GET.get('productGroupObjectId')
        if request.GET.get('shelf_on') or request.GET.get('shelf_off'):
            # 通过审核
            shopProductGroup1 = ShopProductGroup.get_ProductGroup(productGroupId)
            productGroup1 = ProductGroup.copy_Tmp_ProductGroup(shopProductGroup1)
            if productGroup1:
                if request.GET.get('shelf_off'):
                    ProductGroup.set_attribute_state(productGroup1, ProductGroup.STATE_SHELF_OFF)
                return HttpResponseRedirect('/Product/ProductGroupDetail/?productGroupObjectId='+ProductGroup.get_attribute_objectId(productGroup1))
            content['message'] = '提交数据不正确'
            return render(request, 'result.html', {'content': content})
        base.sys_log('no parameter')
    return Error_Page.illegal_access()


@login_required
@permissions([ROLE_PRODUCT])
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
        productGroupInstance = ProductGroup.get_ProductGroup(productGroupObjectId)
        if productGroupInstance:
            data = ProductGroup.get_data(request)
            ProductGroup.update_ProductGroup(data, productGroupInstance)
            return HttpResponseRedirect(reverse("Product:ProductGroupDetail")+'?productGroupObjectId='+productGroupObjectId)
        else:
            content['message'] = '数据无效，请重新提交'
            return render(request, 'result.html', {'content': content})
    if request.method == 'GET':
        productGroupObjectId = request.GET.get('productGroupObjectId')
        if productGroupObjectId:
            content['data']['storeCategory'] = getStoreCategory()
            content['data']['saleCategory'] = getSaleCategory()
            content['data']['productService'] = ProductGroup.get_productService_All()

            # 产生数据，输出到前端
            productGroupInstance = ProductGroup.get_ProductGroup(productGroupObjectId)
            if productGroupInstance:
                content['productGroup'] = ProductGroup.output_ProductGroup(productGroupInstance)
                productList = content['productGroup']['product']
                if productList:
                    tmpProduct = [
                        Product.output_Product_new(product) for product in productList
                    ]
                    content['productList'] = tmpProduct
                content['propertyOption'] = productGroupInstance.get(ProductGroup.Attribute_propertyOption)
            return render(request, 'NewEditProduct.html', {'content': content})
    return Error_Page.illegal_access()



@login_required
@require_http_methods(['GET'])
def ShowComments(request):
    content = PROFILE_INIT()
    objectId = ''
    if request.method == 'GET':
        page = request.GET.get('page')
        page_nums = request.GET.get('page_nums')
        objectId = request.GET.get('productObjectId')
        if page and page_nums and objectId:
            paginator1 = base.paginator_private(page, page_nums, None)
            content.update({'paginator': paginator1})
            productCommentList = ProductGroup.get_attribute_comment(objectId, 'state', 0, int(page), 10)
            if productCommentList:
                content['productGroup']['productCommentList'] = [
                    ProductComment.output_Recommend(foo) for foo in productCommentList
                ]
    content['productGroup']['objectId'] = objectId
    return render(request, 'ProductComment.html', {RETURN_CONTENT: content})


@login_required
def SearchProductGroup(request):
    content = PROFILE_INIT()
    if request.method == 'POST':
        print(request.POST)
        search_base_list = request.POST.getlist('_search_base')
        tagStore = ''
        productGroupList2 = []
        searchCondition = [
        ]

        ProductGroupQuery = leancloud.Object.extend('ProductGroup')
        query = []
        productGroupList = []

        if search_base_list:
            for search_base in search_base_list:
                search = request.POST.get(search_base)
                search_start = request.POST.get(search_base+'_start')
                search_end = request.POST.get(search_base+'_end')
                query1 = ProductGroupQuery.query
                query2 = ProductGroupQuery.query
                A = {}
                if search_base == '_search_id':
                    query1.equal_to('uniqueId', int(search))
                    A = {
                        'name': '商品Id',
                        'value': search,
                    }
                    query.append(query1)
                elif search_base == '_search_name':
                    query1.equal_to('name', search)
                    query.append(query1)
                    A = {
                        'name': '名称',
                        'value': search,
                    }
                elif search_base == '_search_time':
                    start = datetime(int(search_start[0:4]), int(search_start[5:7]), int(search_start[8:10]))
                    end = datetime(int(search_start[0:4]), int(search_start[5:7]), int(search_start[8:10])) + timedelta(days=1)
                    query1.greater_than_or_equal_to('createdAt', start)
                    query2.less_than_or_equal_to('createdAt', end)
                    queryTmp = leancloud.Query.and_(query1, query2)
                    query.append(queryTmp)
                    A = {
                        'name': '上架时间',
                        'value': search_start + ' ' + search_end,
                    }
                elif search_base == '_search_saleCount':
                    print(search_start)
                    print(search_end)
                    query1.greater_than_or_equal_to('saleCount', int(search_start))
                    query2.less_than_or_equal_to('saleCount', int(search_end))
                    queryTmp = leancloud.Query.and_(query1, query2)
                    query.append(queryTmp)
                    A = {
                        'name': '销量',
                        'value': search_start + ' ' + search_end,
                    }
                searchCondition.append(A)
            print(search_base_list)
            print(query)
            queryAll = ''
            if len(search_base_list) == 1:
                queryAll = query[0].find()
                print(queryAll)
            elif len(search_base_list) == 2:
                queryAll = leancloud.Query.and_(*query).find()
            elif len(search_base_list) == 3:
                queryAll = leancloud.Query.and_(query[0], query[1], query[2]).find()
            elif len(search_base_list) == 4:
                queryAll = leancloud.Query.and_(query[0], query[1], query[2], query[3]).find()

            # 检查库存标签
            if request.POST.get('_checkbox_store_1'):
                for foo in queryAll:
                    tag = category.getStoreCategoryThroughProductGroup(foo.get('storeCategory').id)
                    if tag and re.match(tagStore, tag):
                        productGroupList.append(foo)
            else:
                productGroupList = queryAll
            # 检查销售标签
            sys_log(productGroupList)
            if request.POST.get('_checkbox_sale_1'):
                pass
                # productGroupList2 = category.filterSaleCategory(productGroupList, tagSale)
            else:
                productGroupList2 = productGroupList

        content['data']['searchCondition'] = searchCondition
        content['productGroup'] = productGroup.outputProductGroup(productGroupList2)
        return render(request, 'AllProduct.html', {RETURN_CONTENT: content})
    content['data']['storeCategory'] = getStoreCategory()
    content['data']['saleCategory'] = getSaleCategory()
    return render(request, 'SearchProductGroup.html', {RETURN_CONTENT: content})
