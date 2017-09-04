from Error_Page import *
from ClassLibrary.OrderClass.AfterSaleServiceRecord import AfterSaleServiceRecord
from ClassLibrary.ShopClass.Shop_New import Shop
from ClassLibrary.OrderClass.Order_New import Order

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def refund(pingppOrderId, refundSumPrice):
    pingpp.api_key = 'sk_live_4SyjjDm180mLDuzjbHqzrz1C'
    print(BASE_DIR)
    pingpp.private_key_path = BASE_DIR + '/1024-PKCS1.txt'
    ch = pingpp.Charge.retrieve(pingppOrderId)
    re = ch.refunds.create(description='desc', amount=int(refundSumPrice*100))
    print(re)
    return re


@login_required
@permission(ROLE_CUSTOM)
@require_http_methods(['GET'])
def afterSale(request):
    """
    客服检查售后
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
        afterSaleService = shop.get_attribute_afterSaleServiceRecord(int(state), page)
        page_nums = shop.count_attribute_afterSaleServiceRecord(int(state))
        return return_paginator_page(afterSaleService, page, page_nums)
    return illegal_access()


@login_required
@require_http_methods(['POST'])
def disposeAfterSale(request):
    """
    处理售后服务
    :param request: 
    :return: 
    """
    objectId = request.POST.get(attribute_objectId, '')
    state = request.POST.get(attribute_state, -1)
    if objectId and int(state) >= 0:
        state = int(state)
        afterSaleService = AfterSaleServiceRecord()
        afterSaleService.get_Object(objectId)
        if state == AFTER_SALE_2:
            # 退货后退款
            if afterSaleService.set_attribute_state(AFTER_SALE_2):
                return return_OK( '处理成功，等待用户退货后退款' )
        elif state == AFTER_SALE_4 or state == AFTER_SALE_6:
            # 退款
            orderId = afterSaleService.get_attribute_order()
            refundSumPrice = afterSaleService.get_attribute_refundSumPrice()
            if orderId and refundSumPrice is not None:
                order = Order()
                order.get_Object(orderId.id)
                re = refund(order.get_attribute_pingppOrderId(), refundSumPrice)
                if re:
                    if re['failure_msg']:
                        return return_OK( re['failure_msg'] )
                    else:
                        afterSaleService.set_attribute_state(state)
                        return return_OK( '已申请退款，请检查退款状态' )
        elif state == AFTER_SALE_5:
            # 取消申请
            if afterSaleService.set_attribute_state(AFTER_SALE_5):
                return return_OK( '已成功取消申请' )
        return return_OK( '未能成功处理，请联系系统管理员' )
    return illegal_access()


@csrf_exempt
def disposeRefund(request):
    if request.method == 'POST':
        print(request.POST)
        event = request.POST.get('event')
        if event['type'] == 'charge.succeeded':
            return return_OK( status=200 )
        elif event['type'] == 'order.refund.succeeded':
            return return_OK( status=200 )
        return return_OK( status=500 )
    return return_OK( status=200 )
