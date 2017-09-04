import sys
import tempfile
import logging

from leancloud import LeanCloudError
import leancloud


def sys_log(data: object):
    print('------start-------------' + sys._getframe().f_back.f_code.co_name + '--------------')
    logging.error(data)
    print('--------------------------------------------------------------------------------')


def save_data(data: object) -> object:
    """
    保存数据，并增加保存数据时的错误输出。
    :param data:
    :return:
    """
    try:
        data.save()
        return data
    except LeanCloudError as e:
        sys_log(e.error)
    return None


def set_image(name, imageFile, value):
    """
    :param value: 
    :param name: 类的实例 
    :param imageFile: 从file中上传的文件名
    :return: 
    """
    if name is None or imageFile is None or value is None:
        sys_log('parameter is null')
        return False
    tup = tempfile.mkstemp()
    file = open(tup[0], 'wb+')
    for chunk in imageFile.chunks():
        file.write(chunk)
    lc_file = leancloud.File(imageFile.name, data=file)
    name.set(value, lc_file)
    return True


def getInstanceThroughId(className, objectId):
    if className is None or objectId is None:
        return
    Instance = leancloud.Object.extend(className)
    instance = Instance.create_without_data(objectId)
    sys_log(instance)
    return instance


def get_relation_data(objectId, className, relation_value):
    """
    获得关联表的所有数据
    :param relation_value: 
    :param className: 
    :param objectId:
    :return:如果object为空，则返回空，否则，返回关联数据的json格式数据。
    """
    if objectId and className and relation_value:
        ClassInstance = leancloud.Object.extend(className)
        classInstance = ClassInstance.create_without_data(objectId)
        relation = classInstance.relation(relation_value)
        query = relation.query
        try:
            query_list = query.find()
            return query_list
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def get_relation_data_and_attribute(objectId, className, relation_value, attribute, value, skip=None, limit=None):
    """
    获得关联表的所有数据
    :param limit: 
    :param skip: 
    :param value: 
    :param attribute: 
    :param relation_value: 
    :param className: 
    :param objectId:
    :return:如果object为空，则返回空，否则，返回关联数据的json格式数据。
    """
    if objectId and className and relation_value:
        ClassInstance = leancloud.Object.extend(className)
        classInstance = ClassInstance.create_without_data(objectId)
        relation = classInstance.relation(relation_value)
        query = relation.query
        query2 = query.equal_to(attribute, value)
        if skip:
            query.skip(int(skip)*int(limit))
            query.limit(int(limit))
        try:
            query_list = query2.find()
            return query_list
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def count_relation_data_and_attribute(objectId, className, relation_value, attribute, value):
    """
    获得关联表的所有数据的个数
    :param value: 
    :param attribute: 
    :param relation_value: 
    :param className: 
    :param objectId:
    :return:如果object为空，则返回空，否则，返回关联数据的json格式数据。
    """
    if objectId and className and relation_value:
        ClassInstance = leancloud.Object.extend(className)
        classInstance = ClassInstance.create_without_data(objectId)
        relation = classInstance.relation(relation_value)
        query = relation.query
        query2 = query.equal_to(attribute, value)
        try:
            count = query2.count()
            return count
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def get_relation_first(objectId, className, relation_value):
    """
    获得关联表的所有数据
    :param relation_value: 
    :param className: 
    :param objectId:
    :return:如果object为空，则返回空，否则，返回关联数据的json格式数据。
    """
    if objectId and className and relation_value:
        ClassInstance = leancloud.Object.extend(className)
        classInstance = ClassInstance.create_without_data(objectId)
        relation = classInstance.relation(relation_value)
        query = relation.query
        try:
            query_list = query.first()
            return query_list
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def queryInstanceThroughId(className, ID):
    """
    通过对象Id查询对象实例
    :param className: 
    :param ID: 
    :return: 
    """
    if className and ID:
        query = leancloud.Query(className)
        try:
            result_list = query.get(ID)
            sys_log(result_list)
            return result_list
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def queryInstanceThroughName(className, attribute, value):
    """
    通过name获得类的实例信息
    :expand: 如果expand为空，则返回基本信息，否则，返回point指向对象的所有信息，此时，可以使用get方法获得数据。
    :return: 
    """
    if className and attribute and value is not None:
        print(className, attribute, value)
        ClassInstance = leancloud.Object.extend(className)
        query = ClassInstance.query
        query.equal_to(attribute, value)
        try:
            query_list = query.find()
            if len(query_list) > 0:
                return query_list
            else:
                sys_log('none found')
                return None
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def queryInstanceAttributeCount(className, attribute, value):
    """
    通过name获得类的实例信息
    :expand: 如果expand为空，则返回基本信息，否则，返回point指向对象的所有信息，此时，可以使用get方法获得数据。
    :return: 
    """
    if className and attribute and value is not None:
        print(className, attribute, value)
        ClassInstance = leancloud.Object.extend(className)
        query = ClassInstance.query
        query.equal_to(attribute, value)

        try:
            count = query.count()
            if count:
                return count
            else:
                sys_log('none found')
                return None
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def queryInstanceAttribute(className, attribute, value, skip=None, limit=None):
    """
    通过name获得类的实例信息
    :expand: 如果expand为空，则返回基本信息，否则，返回point指向对象的所有信息，此时，可以使用get方法获得数据。
    :return: 
    """
    if className and attribute and value is not None:
        print(className, attribute, value)
        ClassInstance = leancloud.Object.extend(className)
        query = ClassInstance.query
        query.equal_to(attribute, value)
        if skip:
            query.skip((int(skip)-1)*int(limit))
            query.limit(int(limit))
        else:
            query.limit(10)
        try:
            query_list = query.find()
            if len(query_list) > 0:
                return query_list
            else:
                sys_log('none found')
                return None
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def queryInstanceAttributeFirst(className, attribute, value):
    """
    通过name获得类的实例信息
    :expand: 如果expand为空，则返回基本信息，否则，返回point指向对象的所有信息，此时，可以使用get方法获得数据。
    :return: 
    """
    if className and attribute and value:
        ClassInstance = leancloud.Object.extend(className)
        query = ClassInstance.query
        query.equal_to(attribute, value)
        try:
            query_list = query.first()
            if query_list:
                return query_list
            else:
                sys_log('none found')
                return None
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None



def getInstanceAttribute(className, Id, attribute):
    """
    获得对象实例的属性
    :param className: 
    :param Id: 
    :param attribute: 
    :return: 
    """
    result = queryInstanceThroughId(className, Id)
    if result:
        return result.get(attribute)
    else:
        return None


def queryAllInstance(className, element):
    """
    查询所有对象实例
    :param className: 
    :param element: 
    :return: 
    """
    if className is None:
        return
    ClassInstance = leancloud.Object.extend(className)
    query = ClassInstance.query
    query.exists(element)
    try:
        query_list = query.find()
        return query_list
    except LeanCloudError as e:
        sys_log(e.error)
    return None


def getClassThroughName(className, name, value, expandList=None):
    """
    通过name获得类的实例信息
    :expand: 如果expand为空，则返回基本信息，否则，返回point指向对象的所有信息，此时，可以使用get方法获得数据。
    :return: 
    """
    if className is None or name is None or value is None:
        return
    ClassInstance = leancloud.Object.extend(className)
    query = ClassInstance.query
    query.equal_to(name, value)

    if expandList:
        # 这里include有问题，见leancloud文档
        for expand in expandList:
            query.include(expand)
        sys_log(expandList)
    try:
        query_list = query.find()
        return query_list
    except LeanCloudError as e:
        sys_log(e.error)
    return None


def saveImageToClass(className, name, value):
    """
    保存图像到类中
    :param className: 
    :param name: 
    :param value: 
    :return: 
    """
    Image = leancloud.Object.extend(className)
    image = Image()
    image.set(name, value)
    save_data(image)


def searchClassThroughKey(className, name, key):
    """
    查找符合销售策略的所有商品组
    :param className: 
    :param name: 
    :param key: 
    :return: 
    """
    if className and name and key:
        Instance = leancloud.Object.extend(className)
        query = Instance.query
        query.equal_to(name, key)
        query_list = query.find()
        if query_list:
            return query_list
        else:
            return None
    else:
        sys_log('parameter is null')


def searchClassThroughTag(tagClass, tagObjectId, searchClass, searchAttribute):
    """
    查找某个指针
    :param tagClass: 
    :param tagObjectId: 
    :param searchClass: 
    :param searchAttribute: 
    :return: 
    """
    if tagClass and searchAttribute and searchClass and tagObjectId:
        Tag = leancloud.Object.extend(tagClass)
        tag = Tag.create_without_data(tagObjectId)
        query = leancloud.Query(searchClass)
        query.equal_to(searchAttribute, tag)
        query.find()
        return query
    else:
        sys_log('parameter is null')
        return None


def getAllObject(className):
    """
    得到类中所有的元素
    :param className: 
    :return: 
    """
    if className:
        Instance = leancloud.Object.extend(className)
        query = Instance.query
        query.exists('objectId')
        query_list = query.find()
        if query_list:
            return query_list
        else:
            return None
    else:
        sys_log('parameter is null')


def getProductStyle(style, styleArray):
    """
    获得产品风格
    :param style: 
    :param styleArray: 
    :return: 
    """
    productStyle = []
    if style and styleArray:
        for foo in styleArray:
            for k in foo.keys():
                productStyle.append(style[k])
    return productStyle


def paginator_private(page, num_pages, count):
    """
    设置分页
    :param page: 当前页
    :param num_pages: 总页数
    :param count: 总条数
    :return: 
    """
    has_next = 1
    has_previous = 1
    if page:
        page = int(page)
        num_pages = int(num_pages)
        if page == num_pages:
            has_next = 0
        if page == 1:
            has_previous = 0
    else:
        # 获得总条数
        if count > 0:
            num_pages = int(count)
            if num_pages % 10:
                num_pages = int(num_pages / 10) + 1
            else:
                num_pages = int(num_pages / 10)
            print(num_pages)
            page = 1
            has_previous = 0
            if page == num_pages:
                has_next = 0
        elif count == 0:
            num_pages = 0
            has_previous = 0
            has_next = 0
            page = 0
    previous_page_number = None
    next_page_number = None
    if page - has_previous >= 0:
        previous_page_number = page - has_previous
    if num_pages and page + has_next <= num_pages:
        next_page_number = page + has_next
    paginator1 = {
        'has_next': has_next,
        'next_page_number': next_page_number,
        'number': page,
        'has_previous': has_previous,
        'previous_page_number': previous_page_number,
        'num_pages': num_pages
    }
    return paginator1
