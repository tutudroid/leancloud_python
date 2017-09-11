
from Error_Page import *
from ClassLibrary.CategoryClass.SaleCategory import SaleCategory
from ClassLibrary.CategoryClass.StoreCategory import StoreCategory
from ClassLibrary.CategoryClass.SaleCategoryRecommend import SaleCategoryRecommend
from ClassLibrary.ProductClass.ProductGroup_New import ProductGroup
from ClassLibrary.ImageClass.Image import ImageBase
from ClassLibrary.CategoryClass.StoreCategoryFirst import StoreCategoryFirst, get_StoreCategory_All
from ClassLibrary.CategoryClass.StoreCategorySecond import StoreCategorySecond
from ClassLibrary.CategoryClass.StoreCategoryThird import StoreCategoryThird
from ClassLibrary.CategoryClass.SaleCategoryFirst import SaleCategoryFirst, get_SaleCategory_All
from ClassLibrary.CategoryClass.SaleCategorySecond import SaleCategorySecond



@login_required
def ShowSaleCategory(request):
    """
    显示销售分类
    :param request: 
    :return: 
    """
    request.method = request.method
    allData = get_SaleCategory_All()
    return return_data(Class_Name_SaleCategory, allData)


@login_required
@permission(ROLE_PRODUCT)
def sortSaleCategoryFirst(request):
    content = PROFILE_INIT()
    content.update({'saleCategoryFirst': True})
    return render(request, 'SaleCategorySort.html', {'content': content})


@login_required
@permission(ROLE_PRODUCT)
def sortSaleCategorySecond(request):
    content = PROFILE_INIT()
    return render(request, 'SaleCategorySort.html', {'content': content})


@login_required
@permission(ROLE_PRODUCT)
def createSaleCategory(request):
    """
    创建销售分类
    :param request: 
    :return: 

        for mainImage in imageFileList:
            stringSeries = str(mainImage)
            print(stringSeries)
            print(data[Attribute_mainImage].split('\\')[-1])
            if stringSeries == data[Attribute_mainImage].split('\\')[-1]:
                print('success')
    
    """
    saleCategory = json.loads(request.body.decode('utf-8'))
    if saleCategory:
        keyList1 = keyList2 = [
            attribute_name,
            attribute_briefDescription,
            attribute_mainImage,
        ]
        for foo in saleCategory:
            keyList1.append(attribute_storeCategorySecond)
            Dict_Check(foo, keyList2)
            for goo in foo[attribute_storeCategorySecond]:
                Dict_Check(goo, keyList2)
        print(saleCategory)
        for foo in saleCategory:
            first = SaleCategoryFirst()
            first.create_SaleCategory(foo)
            secondStore = foo[attribute_storeCategorySecond]
            for goo in secondStore:
                second = SaleCategorySecond()
                second.create_SaleCategory(goo, first.get_instance())
                first.add_attribute_relation(attribute_saleCategorySecond, second.get_instance())
    allData = get_SaleCategory_All()
    return return_data(Class_Name_SaleCategory, allData)


@login_required
@permission(ROLE_PRODUCT)
def DelSaleCategory(request):
    """
    编辑销售分类, 已经重新编写了一遍
    :param request: 
    :return: 
    """
    className = request.GET.get(Class_Name_SaleCategory, '')
    objectId = request.GET.get(attribute_objectId, '')
    if className and objectId:
        if className == Class_Name_SaleCategoryFirst:
            saleCategory = SaleCategoryFirst()
        else:
            saleCategory = SaleCategorySecond()
        saleCategory.get_Object(objectId)
        saleCategory.delete_SaleCategory()
        return return_msg('success')
    return return_msg('parameter is null')


@login_required
def ShowStoreCategory(request):
    """
    显示库存分类
    :param request: 
    :return: 
    """
    request.method = request.method
    allData = get_StoreCategory_All()
    return return_data(Class_Name_StoreCategory, allData)



@login_required
@permissions([ROLE_PRODUCT])
def createStoreCategory(request):
    """
    创建库存分类
    :param request: 
    :return: 
    """
    storeCategory = json.loads(request.body.decode('utf-8'))
    storeCategory = storeCategory[Class_Name_StoreCategoryFirst]
    print(storeCategory)
    if storeCategory:
        # 数据过滤
        keyList1 = keyList2 = keyList3 = [
            attribute_name,
        ]
        for foo in storeCategory:
            keyList1.append(attribute_storeCategorySecond)
            Dict_Check(foo, keyList1)
            for goo in foo[attribute_storeCategorySecond]:
                keyList2.append(attribute_storeCategoryThird)
                Dict_Check(goo, keyList2)
                for koo in goo:
                    Dict_Check(koo, keyList3)
        # 上述代码检查输入的数据是否合理------------
        for foo in storeCategory:
            first = StoreCategoryFirst()
            first.create_StoreCategoryFirst(foo)
            secondStore = foo[attribute_storeCategorySecond]
            for goo in secondStore:
                print(goo)
                second = StoreCategorySecond()
                second.create_StoreCategorySecond(goo, first.get_instance())
                first.add_attribute_relation(attribute_storeCategorySecond, second.get_instance())
                thirdStore = goo[attribute_storeCategoryThird]
                for koo in thirdStore:
                    print(koo)
                    third = StoreCategoryThird()
                    third.create_StoreCategoryThird(koo, second.get_instance())
                    second.add_attribute_relation(attribute_storeCategoryThird, third.get_instance())
    allData = get_StoreCategory_All()
    return return_data(Class_Name_SaleCategory, allData)


@login_required
@permission(ROLE_PRODUCT)
@require_http_methods(['GET'])
def DelStoreCategory(request):
    """
    删除
    :param request: 
    :return: 
    """
    className = request.GET.get(Class_Name_StoreCategory, '')
    objectId = request.GET.get(attribute_objectId, '')
    if className and objectId:
        if className == Class_Name_StoreCategoryFirst:
            storeCategory = StoreCategoryFirst()
        elif className == Class_Name_StoreCategorySecond:
            storeCategory = StoreCategorySecond()
        else:
            storeCategory = StoreCategoryThird()
        storeCategory.get_Object(objectId)
        storeCategory.delete_Category()
        return return_msg('success')
    return return_msg('parameter is null')


@login_required
@permission(ROLE_BUSINESS)
@require_http_methods(['GET'])
def DelSaleCategoryRecommend(request):
    objectId = request.GET.get(attribute_objectId)
    if objectId:
        sale = SaleCategory(Class_Name_SaleCategoryFirst)
        sale.get_Object(objectId)
        if sale.get_instance():
            saleRecommend = SaleCategoryRecommend()
            saleRecommend.get_Object(sale.get_attribute_Object_Id(attribute_saleCategoryRecommend))
            saleRecommend.destroy_attribute_image(attribute_mainImage)
            saleRecommend.destroy_Object()
            return return_msg('delete success')
    return return_msg('parameter is error')


@login_required
@permission(ROLE_BUSINESS)
@require_http_methods(['GET'])
def SaleCategoryRecommend(request):
    productGroupUniqueId = request.GET.get(attribute_uniqueId, '')
    objectId = request.GET.get(attribute_objectId, '')
    mainImage = request.FILES.get(attribute_mainImage, '')
    if productGroupUniqueId and objectId and mainImage:
        productGroup = ProductGroup()
        productGroup.get_Object_UniqueId(int(productGroupUniqueId))

        sale = SaleCategory(Class_Name_SaleCategoryFirst)
        sale.get_Object(objectId)
        if sale.get_instance() and productGroup.get_instance():
            saleRecommend = SaleCategoryRecommend()
            saleRecommend.create_Object()
            saleRecommend.set_attribute_value(attribute_productGroup, productGroup.get_instance())
            imageFile = ImageBase().save_ImageFile(mainImage)
            saleRecommend.set_attribute_value(attribute_mainImage, imageFile)

            # 将信息写入第一级销售分类
            sale.set_attribute_value(attribute_saleCategoryRecommend, saleRecommend.get_instance())
            return return_data(Class_Name_SaleCategoryRecommend, saleRecommend.output_SaleCategoryRecommend())
    return return_msg('parameter is error')
