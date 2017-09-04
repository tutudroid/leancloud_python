import sys
import tempfile
import logging
import os
import datetime
from leancloud import LeanCloudError
import leancloud


QUERY_SKIP = 10


def sys_log(data: object):
    print('------start-------------' + sys._getframe().f_back.f_code.co_name + '--------------')
    logging.error(data)
    print('--------------------------------------------------------------------------------')


def save_data(data):
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
        sys_log(data)

    return None


def local_image(classInstance, imageFile, attribute):
    """
    :param attribute: 
    :param classInstance: 
    :param imageFile: 从file中上传的文件名
    :return: 
    """
    if classInstance is None or imageFile is None:
        sys_log('parameter is null')
        return False
    if os.path.exists(imageFile):
        print(imageFile)
        with open(imageFile, 'rb') as f:
            lc_file = leancloud.File(imageFile.split('/')[-1], f)
            lc_file.save()
            classInstance.set(attribute, lc_file)
            save_data(classInstance)
    return True


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
    lc_file.save()
    name.set(value, lc_file)
    if save_data(name):
        return True
    else:
        return False


def save_image(imageFile):
    """
    :param imageFile: 
    :param classInstance: 类的实例 
    :param attribute: 从file中上传的文件名
    :return: 
    """
    if imageFile:
        tup = tempfile.mkstemp()
        file = open(tup[0], 'wb+')
        for chunk in imageFile.chunks():
            file.write(chunk)
        lc_file = leancloud.File(imageFile.name, data=file)
        lc_file.save()
        return lc_file
    return False


def set_file(classInstance, attribute, fileDate):
    tup = tempfile.mkstemp()
    file = open(tup[0], 'wb+')
    file.write(bytes(fileDate, encoding="utf8"))
    lc_file = leancloud.File('detailDescription', data=file)
    classInstance.set(attribute, lc_file)
    if save_data(classInstance):
        return True
    return None


def getInstanceThroughId(className, objectId):
    if className is None or objectId is None:
        return
    Instance = leancloud.Object.extend(className)
    instance = Instance.create_without_data(objectId)
    sys_log(instance)
    return instance


def count_relation_data(objectId, className, relation_value):
    """
    获得关联表的所有数据
    :param relation_value: 
    :param className: 
    :param objectId:
    :return:如果object为空，则返回空，否则，返回关联数据的json格式数据。
    """
    if objectId and className and relation_value:
        classInstance = queryInstanceThroughId(className, objectId)
        if classInstance:
            relation = classInstance.relation(relation_value)
            query = relation.query
            try:
                count = query.count()
                return count
            except LeanCloudError as e:
                sys_log(e.error)
    sys_log('parameter is null')
    return None


def get_relation_data(objectId, className, relation_value, skip=None, limit=QUERY_SKIP):
    """
    获得关联表的所有数据
    :param limit: 
    :param skip: 
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
        if skip:
            query.skip((int(skip) - 1)*int(limit))
            query.limit(int(limit))
        try:
            query_list = query.find()
            return query_list
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def get_relation_data_and_exist(objectId, className, relation_value, attribute, skip=None, limit=QUERY_SKIP):
    """
    获得关联表的所有数据
    :param attribute: 
    :param limit: 
    :param skip: 
    :param relation_value: 
    :param className: 
    :param objectId:
    :return:如果object为空，则返回空，否则，返回关联数据的json格式数据。
    """
    if objectId and className and relation_value and attribute:
        ClassInstance = leancloud.Object.extend(className)
        classInstance = ClassInstance.create_without_data(objectId)
        relation = classInstance.relation(relation_value)
        query = relation.query
        query = query.exists(attribute)
        if skip:
            query.skip((int(skip) - 1)*int(limit))
            query.limit(int(limit))
        try:
            query_list = query.find()
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
    return 0


def get_relation_data_and_attribute(objectId, className, relation_value, attribute, value, skip=None, limit=QUERY_SKIP):
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
        query = query.equal_to(attribute, value)
        if skip and int(skip) - 1 > 0:
             query.skip((int(skip) - 1)*int(limit))
        query.limit(int(limit))
        try:
            query_list = query.find()
            return query_list
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def get_relation_data_and_attribute_and_sort_uniqueId(objectId, className, relation_value, attribute, value, skip=None, limit=QUERY_SKIP):
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
        query = query.equal_to(attribute, value)
        if skip and int(skip) - 1 >= 0:
            query.skip((int(skip) - 1)*int(limit))
            query.limit(int(limit))
        try:
            query.add_ascending('uniqueId')
            query_list = query.find()
            return query_list
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def count_relation_data_greater_attribute(objectId, className, relation_value, attribute, value):
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
        query2 = query.greater_than_or_equal_to(attribute, value)
        try:
            count = query2.count()
            return count
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return 0


def get_relation_data_greater_attribute(objectId, className, relation_value, attribute, value, skip=None, limit=QUERY_SKIP):
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
        query = query.greater_than_or_equal_to(attribute, value)
        if skip and int(skip) - 1 >= 0:
            query.skip((int(skip) - 1)*int(limit))
            query.limit(int(limit))
        try:
            query_list = query.find()
            return query_list
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def query_relation_data_greater_and_less_attribute(objectId, className, queryClassName, attribute, value, value2, method=None, skip=None, limit=QUERY_SKIP):
    """
    获得关联表的所有数据
    :param method: 
    :param limit: 
    :param skip: 
    :param value: 
    :param attribute: 
    :param queryClassName: 
    :param className: 
    :param objectId:
    :param value2: 
    :param attribute2: 
    :return:如果object为空，则返回空，否则，返回关联数据的json格式数据。
    """
    if objectId and className and queryClassName:
        ClassInstance = leancloud.Object.extend(className)
        classInstance = ClassInstance.create_without_data(objectId)

        query = leancloud.Query(queryClassName)
        query.equal_to(className.lower(), classInstance)
        query.greater_than_or_equal_to(attribute, value)
        query.less_than_or_equal_to(attribute, value2)
        if skip and int(skip) - 1 >= 0:
            query.skip((int(skip) - 1)*int(limit))
            query.limit(int(limit))
        try:
            if method:
                count = query.count()
                return count
            else:
                query_list = query.find()
                return query_list

        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None


def get_relation_data_greater_and_less_attribute(objectId, className, queryClassName, attribute, value, value2, skip=None, limit=QUERY_SKIP):
    """
    获得关联表的所有数据
    :param limit: 
    :param skip: 
    :param value: 
    :param attribute: 
    :param relation_value: 
    :param className: 
    :param objectId:
    :param value2: 
    :param attribute2: 
    :return:如果object为空，则返回空，否则，返回关联数据的json格式数据。
    """
    if objectId and className and queryClassName:
        ClassInstance = leancloud.Object.extend(className)
        classInstance = ClassInstance.create_without_data(objectId)

        query = leancloud.Query(queryClassName)
        query.equal_to(className.lower(), classInstance)
        query.greater_than_or_equal_to(attribute, value)
        query.less_than_or_equal_to(attribute, value2)
        if skip and int(skip) - 1 >= 0:
            query.skip((int(skip) - 1)*int(limit))
            query.limit(int(limit))
        try:
            query_list = query.find()
            return query_list
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None



def get_relation_data_and_attribute_two(objectId, className, relation_value, attribute, value1, value2, skip=None, limit=QUERY_SKIP):
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
        query1 = relation.query
        query1.equal_to(attribute, value1)
        query2 = relation.query
        query2.equal_to(attribute, value2)
        query = leancloud.Query.or_(query1, query2)
        if skip and int(skip) - 1 >= 0:
            query.skip((int(skip) - 1)*int(limit))
            query.limit(int(limit))
        try:
            query_list = query.find()
            return query_list
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None



def count_relation_data_and_exist(objectId, className, relation_value, attribute):
    """
    获得关联表的所有数据的个数
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
        query = query.exists(attribute)
        try:
            count = query.count()
            sys_log(count)
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
        # print(className, attribute, value)
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


def count_exist_instance(className, attribute):
    if className and attribute:
        ClassInstance = leancloud.Object.extend(className)
        query = ClassInstance.query
        query.exists(attribute)
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


def queryExistInstance(className, attribute, skip=None, limit=QUERY_SKIP):
    """
    通过name获得类的实例信息
    :expand: 如果expand为空，则返回基本信息，否则，返回point指向对象的所有信息，此时，可以使用get方法获得数据。
    :return: 
    """
    if className and attribute:
        ClassInstance = leancloud.Object.extend(className)
        query = ClassInstance.query
        query.exists(attribute)
        if skip:
            query.skip((int(skip) - 1) * int(limit))
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


def queryInstanceAttributeCount(className, attribute, value):
    """
    通过name获得类的实例信息
    :expand: 如果expand为空，则返回基本信息，否则，返回point指向对象的所有信息，此时，可以使用get方法获得数据。
    :return: 
    """
    if className and attribute and value is not None:
        ClassInstance = leancloud.Object.extend(className)
        query = ClassInstance.query
        query.equal_to(attribute, value)
        try:
            count = query.count()
            if count:
                return count
            else:
                sys_log('none found')
                return 0
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return 0


def queryInstanceAttribute(className, attribute, value, skip=None, limit=QUERY_SKIP):
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
            query.limit(QUERY_SKIP)
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


def queryInstanceAttributeGreaterOrEqual(className, attribute, value, skip=None, limit=QUERY_SKIP):
    """
    通过name获得类的实例信息
    :expand: 如果expand为空，则返回基本信息，否则，返回point指向对象的所有信息，此时，可以使用get方法获得数据。
    :return: 
    """
    if className and attribute and value is not None:
        print(className, attribute, value)
        ClassInstance = leancloud.Object.extend(className)
        query = ClassInstance.query
        query.greater_than_or_equal_to(attribute, value)
        if skip:
            query.skip((int(skip)-1)*int(limit))
            query.limit(int(limit))
        else:
            query.limit(QUERY_SKIP)
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



def queryInstanceAttribute_and_sort_uniqueId(className, attribute, value, skip=None, limit=QUERY_SKIP):
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
            query.limit(QUERY_SKIP)
        try:
            query.add_ascending('uniqueId')
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
    if className and attribute and value is not None:
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


def queryInstanceAttribute1_Attribute2_Count(className, attribute, value, attribute2, value2):
    """
    通过name获得类的实例信息
    :expand: 如果expand为空，则返回基本信息，否则，返回point指向对象的所有信息，此时，可以使用get方法获得数据。
    :return: 
    """
    if className and attribute and attribute2:
        ClassInstance = leancloud.Object.extend(className)
        query = ClassInstance.query
        query.equal_to(attribute, value)
        query2 = ClassInstance.query
        query2.equal_to(attribute2, value2)
        query = leancloud.Query.and_(query, query2)
        try:
            count = query.count()
            if count:
                return count
            else:
                sys_log('none found')
                return 0
        except LeanCloudError as e:
            sys_log(e.error)
    else:
        sys_log('parameter is null')
    return None



def queryInstanceAttribute1_Attribute2(className, attribute, value, attribute2, value2, skip=None, limit=QUERY_SKIP):
    """
    通过name获得类的实例信息
    :expand: 如果expand为空，则返回基本信息，否则，返回point指向对象的所有信息，此时，可以使用get方法获得数据。
    :return: 
    """
    if className and attribute and attribute2:
        ClassInstance = leancloud.Object.extend(className)
        query = ClassInstance.query
        query.equal_to(attribute, value)
        query2 = ClassInstance.query
        query2.equal_to(attribute2, value2)
        query = leancloud.Query.and_(query, query2)
        if skip:
            query.skip((int(skip)-1)*int(limit))
            query.limit(int(limit))
        else:
            query.limit(QUERY_SKIP)
        try:
            query_list = query.find()
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



def queryInstanceAttribute1_Attribute2_First(className, attribute, value, attribute2, value2):
    """
    通过name获得类的实例信息
    :expand: 如果expand为空，则返回基本信息，否则，返回point指向对象的所有信息，此时，可以使用get方法获得数据。
    :return: 
    """
    if className and attribute and value is not None:
        ClassInstance = leancloud.Object.extend(className)
        query = ClassInstance.query
        query.equal_to(attribute, value)
        query2 = ClassInstance.query
        query2.equal_to(attribute2, value2)
        query = leancloud.Query.and_(query, query2)
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


def queryInstance_A1_A2_A3_First(className, attribute, value, attribute1, value1, attribute2, value2):
    """
    通过name获得类的实例信息
    :expand: 如果expand为空，则返回基本信息，否则，返回point指向对象的所有信息，此时，可以使用get方法获得数据。
    :return: 
    """
    if className and attribute and value:
        ClassInstance = leancloud.Object.extend(className)
        query = ClassInstance.query
        query.equal_to(attribute, value)
        query2 = ClassInstance.query
        query2.equal_to(attribute2, value2)
        query1 = ClassInstance.query
        query1.equal_to(attribute1, value1)
        query = leancloud.Query.and_(query, query1, query2)
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
    result = queryInstanceThroughId(className, Id)
    if result:
        return result.get(attribute)
    else:
        return None


def queryAllInstance(className, element, skip=None, limit=QUERY_SKIP):
    if className is None:
        return
    ClassInstance = leancloud.Object.extend(className)
    query = ClassInstance.query
    query.exists(element)
    if skip:
        query.skip((int(skip) - 1) * int(limit))
        query.limit(int(limit))
    else:
        query.limit(10)
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


def paginator_private(page, num_pages):
    """
    设置分页
    :param page: 当前页
    :param num_pages: 总页数
    :param count: 总条数
    :return: 
    """
    has_next = 1
    has_previous = 1
    previous_page_number = 0
    next_page_number = 0

    page = int(page)
    num_pages = int(num_pages)
    if page == num_pages:
        has_next = 0
        next_page_number = page + has_next
    if page == 1:
        has_previous = 0
        previous_page_number = page - has_previous

    paginator1 = {
        'has_next': has_next,
        'next_page_number': next_page_number,
        'number': page,
        'has_previous': has_previous,
        'previous_page_number': previous_page_number,
        'num_pages': num_pages
    }
    return paginator1


def change_timeZone(dt4: datetime.datetime):
    """
    与服务器时间相差8个小时，所以返回的时间再增加8小时
    :param dt4: 
    :return: 
    """
    if dt4:
        dt5 = dt4 + datetime.timedelta(hours=8)
        return dt5.strftime("%Y-%m-%d %H:%M:%S")
    return None


def destroy_relation(objectId, className, relation_attribute, className2):
    relationList = get_relation_data(objectId, className, relation_attribute)
    if relationList:
        for foo in relationList:
            instance = queryInstanceThroughId(className2, foo.get('objectId'))
            if instance:
                if instance.get('mainImage'):
                    instance.get('mainImage').destroy()
                instance.destroy()
            else:
                sys_log('instance no found')


def destroy_relation_imageList(objectId, className, relation_attribute, className2):
    relationList = get_relation_data(objectId, className, relation_attribute)
    if relationList:
        for foo in relationList:
            instance = queryInstanceThroughId(className2, foo.get('objectId'))
            if instance:
                imageFile = instance.get('imageFile')
                if imageFile:
                    imageFile.destroy()
                instance.destroy()
            else:
                sys_log('instance no found')


def create_network_image(instance, attr):
    """
    获得实例参数中的url，并将其赋值给file
    :param instance: 
    :param attr: 
    :return: 
    """
    img_url = instance.get(attr).url
    name = instance.get(attr).name
    avatar = leancloud.File.create_with_url(name, img_url)
    avatar.save()
    return avatar
