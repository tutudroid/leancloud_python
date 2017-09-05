
from ClassLibrary.UserClass.User import _User
from Error_Page import *
from Initiation import BASE

from Product.library import base

BaseAddress = "/Users/kang/Desktop"

SecondAddress = BaseAddress + "/repertory"

StoreFile = SecondAddress + "/JSON/库存分类.json"
SaleFile = SecondAddress + "/JSON/销售分类.json"
JSONFile_ProductService = SecondAddress + "/JSON/商品服务.json"
JSONFile_IPTable = SecondAddress + "/JSON/IP.json"
JSONFile_BandTable = SecondAddress + "/JSON/品牌.json"
JSONFile_Product = SecondAddress + "/JSON/商品.json"
JSONFile_ProductDir = SecondAddress + "/商品/"

JSONFile_ProductGroup = BaseAddress + "/repertory/JSON/.json"



def get_property(data, code):
    if data and code:
        for foo in data:
            if foo['编号'] == code:
                return foo['值']
    return 'None'


def get_choice(data, codeProperty, codeChoice):
    if data and codeProperty and codeChoice:
        for foo in data:
            if foo['编号'] == codeProperty:
                for goo in foo['选项']:
                    if goo['编号'] == codeChoice:
                        return goo['值']
    return 'None'

def get_style(choice, productGroupData):
    objectData = {}
    for goo in choice:
        A = {
            get_property(productGroupData, goo['属性编号']): get_choice(productGroupData, goo['属性编号'], goo['选项编号'])
        }
        objectData.update(A)
    return objectData



def CreateAdmin(request):
    """
    用户系统初始化时创建Admin用户
    :param request: 
    :return: 
    """
    error = '请输入密码'
    user = leancloud.User()
    user.logout()
    if request.method == 'GET':
        if request.GET.get('name') == 'chuheridangwu':

            error = '修改完成'
            admin = base.queryInstanceAttribute(Class_Name_User, attribute_name, 'admin')
            if admin is None:
                try:
                    user = leancloud.User()
                    user.set_username('admin')
                    user.set_password('123')
                    user.set('state', 0)
                    user.sign_up()

                    userInstance = _User()
                    userInstance.set_instance(user)
                    userInstance.set_attribute_role(ROLE_ADMINISTRATOR)

                except LeanCloudError as e:
                    error = e.error
            else:
                error = '管理员账户已存在，请联系系统管理员'
    content = {
        'message': error,
    }
    return render(request, 'result.html', {'content': content})



def ClearAllData(request):
    if request.GET.get('password') == 'OhMyGod!Landy':
        name = ['_Files', '_User',
                Class_Name_BrandTable,
                Class_Name_IPTable,
                Class_Name_SaleCategoryRecommend,
                Class_Name_ProductImage,
                Class_Name_ProductCommentImage,
                Class_Name_SaleCategorySecond,
                Class_Name_SaleCategoryFirst,
                Class_Name_Product,
                Class_Name_ProductDetailDescription,
                Class_Name_ProductComment,
                Class_Name_ProductGroup,
                Class_Name_ShopProduct,
                Class_Name_ShopProductGroup,
                Class_Name_SettleInUser,
                Class_Name_SettleInCompany,
                Class_Name_Shop,
                Class_Name_Order,
                Class_Name_StoreCategoryThird,
                Class_Name_StoreCategoryFirst,
                Class_Name_StoreCategorySecond,
                Class_Name_LogisticsInfo,
                Class_Name_SettleInApplication,
                Class_Name_SaleCategoryImage,
                Class_Name_AfterSaleSupport,
                Class_Name_AfterSaleServiceRecord,
                Class_Name_AfterSaleServiceImage,
                Class_Name_OrderProduct,
                'TmpUser',
                'Recommend',
                ]
        for foo in name:
            while True:
                ClassInstance = leancloud.Object.extend(foo)
                query = ClassInstance.query
                query.exists('objectId')
                queryList = query.find()
                if queryList:
                    leancloud.Object.destroy_all(queryList)
                else:
                    break
            print('已清理表' + foo)
        return HttpResponse('success')
    return HttpResponse('请输入密码')

from ClassLibrary.ShopClass.Shop_New import Shop


def Inject_Data(request):
    """
    测试所有的类接口，写入与显示
    :param request: 
    :return: 
    """

    return render(request, 'test_example.html', {'content': ''})
