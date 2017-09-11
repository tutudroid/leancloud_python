import Error_Page
from Error_Page import *
from Recommendation import Recommend
from ClassLibrary import Base

# 前端参数
PARAMS_RECOMMEND_TIME = '_recommendationTime'
PARAMS_RECOMMEND_FILE = '_imageFileName'
PARAMS_RECOMMEND_WIDTH = '_imageWidth'
PARAMS_RECOMMEND_HEIGHT = '_imageHeight'
PARAMS_RECOMMEND_PRODUCT_GROUP = '_inputProductGroupId'


PARAMS_RECOMMEND_TAG = 'id_AddTagContentX'
PARAMS_RECOMMEND_TAG_GROUP_ID = 'id_AddTagContentProductGroupId_'
PARAMS_RECOMMEND_TAG_ID = 'id_AddTagContentProductId_'
PARAMS_RECOMMEND_TAG_LINE = 'id_AddTagContentLine_'
PARAMS_RECOMMEND_TAG__LINE_STYLE = 'id_AddTagContentType_'
PARAMS_RECOMMEND_TAG__LINE_DIRECTION = 'id_AddTagContentDirection_'
PARAMS_RECOMMEND_TAG__POINT_X = 'id_AddTagContentX_'
PARAMS_RECOMMEND_TAG__POINT_Y = 'id_AddTagContentY_'


# 返回参数名称
RETURN_PARAMS_POINT = "point"
RETURN_FIRST_DATA = 'data'
RETURN_SECOND_RECOMMEND_LIST = 'recommendList'


def FUNCTION_OUTPUT_DATA(data):
    Base.sys_log_info( data )


def getRequestData1(request):
    """
    从前端获取tag数据，并对数据有效性进行检查
    :param request: 
    :return: 
    """
    tagList = []
    for foo in request.POST.getlist(PARAMS_RECOMMEND_TAG):
        if foo:
            percentX = request.POST.get(PARAMS_RECOMMEND_TAG__POINT_X + foo)
            percentY = request.POST.get(PARAMS_RECOMMEND_TAG__POINT_Y + foo)
            productId = request.POST.get(PARAMS_RECOMMEND_TAG_ID + foo)
            productGroupId = request.POST.get(PARAMS_RECOMMEND_TAG_GROUP_ID + foo)
            lines = []
            for goo in request.POST.getlist(PARAMS_RECOMMEND_TAG_LINE + foo):
                if goo:
                    style = request.POST.get(PARAMS_RECOMMEND_TAG__LINE_STYLE + foo + goo)
                    direction = request.POST.get(PARAMS_RECOMMEND_TAG__LINE_DIRECTION + foo + goo)
                    if style and direction:
                        line = {
                            'style': int(style),
                            'direction': int(direction),
                            'content': goo,
                        }
                        lines.append(line)
                    else:
                        return Error_Page.Parameter_Error()

            if percentX and percentY and productGroupId and productId and len(lines) > 0:
                A = {
                    'point': {
                        'percentX': float(percentX),
                        'percentY': float(percentY),
                    },
                    'lines': lines,
                    'productId': productId,
                    'productGroupId': productGroupId,
                }
                print(A)
                tagList.append(A)
            else:
                return Error_Page.Parameter_Error()
    if len(tagList) > 0:
        return tagList
    return None


def getHtmlDate(request):
    """
    从前端获取数据
    :param request: 
    :return: 
    """
    data = {
        Recommend.Attribute_time: request.POST.get(PARAMS_RECOMMEND_TIME),
        Recommend.Attribute_mainImage: request.FILES.get(PARAMS_RECOMMEND_FILE),
        Recommend.Attribute_imageWidth: request.POST.get(PARAMS_RECOMMEND_WIDTH),
        Recommend.Attribute_imageHeight: request.POST.get(PARAMS_RECOMMEND_HEIGHT),
        Recommend.Attribute_tagGroup: getRequestData1(request),
    }
    return data


@login_required
@permission(ROLE_BUSINESS)
def AddRecommendation(request):
    """
    创建新的推荐
    :param request: 
    :return: 
    """
    content = PROFILE_INIT()
    if request.method == 'POST':
        if request.POST.get('submit'):
            data = getHtmlDate(request)
            # 参数检查
            if data:
                print(data)
                Recommend.save_Recommend(data)
                # 查找所有推荐
                return HttpResponseRedirect('/Recommendation/AllRecommendation/')
            else:
                return Error_Page.Parameter_Error()

    return render(request, 'AddRecommendation.html', {'content': content, })


@login_required
@permission(ROLE_BUSINESS)
@require_http_methods(['GET'])
def AllRecommendation(request):
    """
    显示所有推荐信息
    :param request: 
    :return: 
    """
    content = PROFILE_INIT()
    # 查找所有推荐
    # 设置分页
    page = request.GET.get('page', 1)
    page_nums = Recommend.count_Recommend_All()
    paginator1 = Base.paginator_private(page, page_nums)
    content.update({'paginator': paginator1})

    content['data']['recommendList'] = Recommend.get_Recommend_All(page)
    Base.sys_log_info( content )
    return render(request, 'AllRecommendation.html', {'content': content, })


@login_required
@require_http_methods(['GET'])
@permission(ROLE_BUSINESS)
def ShowRecommendation(request):
    """
    显示推荐信息
    :param request: 
    :return: 
    """
    content = PROFILE_INIT()
    objectId = request.GET.get('objectId')
    query = Recommend.get_Recommend(objectId)
    if query:
        content['recommend'] = Recommend.output_Recommend(query)
    Base.sys_log_info( content )
    return render(request, 'ShowRecommendation.html', {'content': content})


@login_required
@permission(ROLE_BUSINESS)
def EditRecommendation(request):
    """
    编辑推荐信息
    :param request: 
    :return: 
    """
    content = PROFILE_INIT()
    if request.method == 'POST':
        objectId = request.POST.get('objectId')
        if request.POST.get('_EditAndSave'):
            Base.sys_log_info( request.POST )

            tagList = getRequestData1(request)
            if tagList:
                Recommend.update_attribute_tagGroup(objectId, tagList)
                return HttpResponseRedirect('/Recommendation/ShowRecommendation/?objectId='+objectId)
            else:
                return Error_Page.Parameter_Error('EditRecommendation\'s parameter is null')
        if request.POST.get('_delete'):
            Recommend.delete_Recommend(objectId)
            return HttpResponseRedirect('/Recommendation/AllRecommendation/')
    objectId = request.GET.get('objectId')
    # 显示需要修改的数据
    query = Recommend.get_Recommend(objectId)
    if query:
        content['data']['recommend'] = Recommend.output_Recommend(query)
    Base.sys_log_info( content )
    return render(request, 'EditRecommendation.html', {'content': content, })
