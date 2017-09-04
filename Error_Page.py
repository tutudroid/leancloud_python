from django.http import HttpResponseRedirect, HttpResponse
import leancloud
from django.shortcuts import render
from django.core.urlresolvers import reverse
from Account.decorators import login_required, permission, not_permission, permissions
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from ClassLibrary.BaseClass.Attribute_Parameter import *
from leancloud import LeanCloudError
import time
from datetime import datetime, timedelta
import pingpp
import os
import json


def abort():
    return HttpResponseRedirect('/Account/Login')


def illegal_permission():
    return HttpResponseRedirect('/NoFound/')


def illegal_access():
    return HttpResponseRedirect('/NoFound/')


def Parameter_Error(request=None, message=None):
    return HttpResponse()


def return_paginator_page(dataList, page, pageNums):
    returnData = {
        Class_Name_Shop: dataList,
        Class_Name_paginator: {
            paginator_PAGE: page,
            paginator_NUM_PAGES: pageNums
        }
    }
    return HttpResponse(returnData, content_type='Application/Json')


def return_OK(msg=None, status=200):
    returnData = {
        'msg': msg,
        return_status: True,
    }
    return HttpResponse(json.dumps(returnData), content_type="application/json")


def return_data(key, value, status=200):
    returnData = {
        key: value,
        return_status: True,
    }
    return HttpResponse(returnData, content_type='Application/Json', status=status)


def PROFILE_INIT():
    """
    初始化返回的数据结构
    :return:
    """
    content = {
        'profile': {
            'token': 'xxxx',
            'username': '',
            'role_list': '',
            'current_role': '',
        },
        'data': {},
        'return': {},
        'order': {},
        'result': {},
        'shop': {},
        'productGroup': {},
        'product': {},
        'time': str( int( time.time() ) ),
        'range': range( 1, 100 ),
    }

    # 获得用户名
    current_user = leancloud.User.get_current()
    return content

# 字典检查


def Dict_Check(data, keyList):
    if keyList:
        for key in keyList:
            if key not in data or not data[key]:
                return return_OK('数据不完整，请检查')
    return True

# 请求错误

# 非法访问

# 未登录

# 数据错误页面

#