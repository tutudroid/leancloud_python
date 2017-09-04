from Error_Page import *
from ClassLibrary.ShopClass.Shop_New import Shop



@login_required
@permission(ROLE_SHOP)
@require_http_methods(['GET'])
def AllOrder(request):
    """
    显示未发货订单
    :param request: 
    :return: 
    """
    state = request.GET.get(attribute_state, 1)
    objectId = request.GET.get(attribute_objectId, '')
    page = request.GET.get(paginator_PAGE, 1)
    if objectId:
        shop = Shop()
        shop.get_Object(objectId)
        order = shop.get_attribute_order(int(state), page)
        page_nums = shop.count_attribute_order(int(state))
        return return_paginator_page(order, page, page_nums)
    return illegal_access()


@login_required
@require_http_methods(['POST'])
def displaceOrder(request):
    """
    发送请求从快递鸟获得
    :param request: 
    :return: 
    """
    shipperCode = request.POST.get(attribute_shipperCode)
    shipperName = request.POST.get(attribute_shipperName)
    logisticsCode = request.POST.get(attribute_logisticCode)
    objectId = request.POST.get(attribute_objectId)
    if shipperCode and shipperName and logisticsCode and objectId:
        pass
    else:
        return Parameter_Error('输入信息有误')
    return illegal_access()



@login_required
def SearchOrder(request):
    """
    搜索订单
    :param request: 
    :return: 
    """
    content = PROFILE_INIT()
    if request.method == 'POST':
        print(request.POST)
        search_base_list = request.POST.getlist('checkbox_search')

        OrderQuery = leancloud.Object.extend('Order')
        query = []
        searchCondition = []
        if search_base_list:
            for search_base in search_base_list:
                search = request.POST.get(search_base)
                query1 = OrderQuery.query
                query2 = OrderQuery.query
                A = {}
                if search_base == 'orderId':
                    query1.equal_to('uniqueId', int(search))
                    A = {
                        'name': '订单Id',
                        'value': search,
                    }
                    query.append(query1)
                elif search_base == 'order_state':
                    query1.equal_to('orderState', int(search))
                    query.append(query1)
                    A = {
                        'name': '订单状态',
                        'value': '',
                    }
                elif search_base == 'userId':
                    # user = base.queryInstanceAttributeFirst('_User', 'uniqueId', int(search))
                    # print(user)
                    print('user is up')
                    # query1.equal_to('user', user)
                    query.append(query1)
                    A = {
                        'name': '用户Id',
                        'value': search,
                    }
                elif search_base == 'shopId':
                    # s hop = Base.queryInstanceAttributeFirst('Shop', 'uniqueId', int(search))
                    # query1.equal_to('shop', shop)
                    query.append(query1)
                    A = {
                        'name': '商家Id',
                        'value': search,
                    }
                elif search_base == 'orderTime':
                    search_start = request.POST.get(search_base + '_start')
                    search_end = request.POST.get(search_base + '_end')
                    if search_start and search_end:
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
                searchCondition.append(A)
        print(search_base_list)
        print(query)
        queryAll = ''
        if len(query) == 1:
            queryAll = query[0].find()
            print(queryAll)
        elif len(query) >= 2:
            queryAll = leancloud.Query.and_(*query).find()
        print(queryAll)
        # 过滤商品Id
        returnOrderList = []

        content.update({'order': returnOrderList})
        content.update({'searchCondition': searchCondition})
        print(content)
        return render(request, 'ShowAllOrder.html', {'content': content})
    return render(request, 'SearchOrder.html', {'content': content})
