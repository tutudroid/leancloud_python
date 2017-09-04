from Product.library import base
import leancloud
from ClassLibrary.ProductClass.ProductGroup_New import ProductGroup

CLASS_NAME = 'Recommend'
CLASS_RECOMMEND_IMAGE = 'RecommendImage'
Attribute_recommend = 'recommend'
Attribute_imageFile = 'imageFile'

Attribute_mainImage = 'mainImage'
Attribute_tagGroup = 'tagGroup'
Attribute_state = 'state'
Attribute_imageWidth = 'imageWidth'
Attribute_imageHeight = 'imageHeight'
Attribute_createdAt = 'createdAt'
Attribute_objectId = 'objectId'
Attribute_time = 'time'
Attribute_productGroup = 'productGroup'

STATE_DELETE = -1
STATE_OK = 0
SKIP = 10


def get_Recommend(objectId):
    if objectId:
        recommend = base.queryInstanceThroughId(CLASS_NAME, objectId)
        return recommend
    return None


def get_Recommend_All(page):
    if page:
        queries = base.queryInstanceAttribute(CLASS_NAME, Attribute_state, STATE_OK,  page, SKIP)
        if queries:
            recommendList = [output_Recommend(foo) for foo in queries]
            return recommendList
    return None


def count_Recommend_All():
    count = base.queryInstanceAttributeCount(CLASS_NAME, Attribute_state, STATE_OK)
    return count


def save_Recommend(data):
    """
    保存推荐
    :return: 
    """
    Recommend1 = leancloud.Object.extend(CLASS_NAME)

    recommend = Recommend1()
    base.set_image(recommend, data[Attribute_mainImage], Attribute_mainImage)
    recommend.set(Attribute_tagGroup, data[Attribute_tagGroup])

    relation = recommend.relation(Attribute_productGroup)
    for foo in data[Attribute_tagGroup]:
        productGroup = ProductGroup()
        productGroup.get_Object(foo['productGroupId'])
        if productGroup.get_instance():
            relation.add(productGroup.get_instance())

    recommend.set(Attribute_imageWidth, int(data[Attribute_imageWidth]))
    recommend.set(Attribute_imageHeight, int(data[Attribute_imageHeight]))
    recommend.set(Attribute_state, STATE_OK)
    recommend.set(Attribute_time, data[Attribute_time])
    base.save_data(recommend)

    RecommendImage = leancloud.Object.extend(CLASS_RECOMMEND_IMAGE)
    recommendImage = RecommendImage()
    recommendImage.set(Attribute_imageFile, recommend.get(Attribute_mainImage))
    recommendImage.set(Attribute_recommend, recommend)
    base.save_data(recommendImage)


def get_attribute_mainImage(recommend):
    if recommend:
        return recommend.get(Attribute_mainImage)
    return None


def get_attribute_tagGroup(recommend):
    if recommend:
        return recommend.get(Attribute_tagGroup)
    return None


def get_attribute_state(recommend):
    if recommend:
        return recommend.get(Attribute_state)
    return None


def get_attribute_imageWidth(recommend):
    if recommend:
        return recommend.get(Attribute_imageWidth)
    return None


def get_attribute_imageHeight(recommend):
    if recommend:
        return recommend.get(Attribute_imageHeight)
    return None


def get_attribute_createdAt(recommend):
    if recommend:
        return base.change_timeZone(recommend.get(Attribute_createdAt))
    return None


def get_attribute_objectId(recommend):
    if recommend:
        return recommend.get(Attribute_objectId)
    return None


def get_attribute_time(recommend):
    if recommend:
        return recommend.get(Attribute_time)
    return None


def delete_Recommend(objectId):
    if objectId:
        recommend = base.queryInstanceThroughId(CLASS_NAME, objectId)
        if recommend:
            recommend.set(Attribute_state, STATE_DELETE)
            if base.save_data(recommend):
                base.sys_log('delete success')
    return None


def update_attribute_tagGroup(objectId, recommendTag):
    """
    商品推荐的修改，只能修改标签的位置坐标
    :param objectId: 
    :param recommendTag: 
    :return: 
    """
    if objectId and recommendTag:
        recommend = base.queryInstanceThroughId(CLASS_NAME, objectId)
        tagList = recommend.get(Attribute_tagGroup)
        if tagList != recommendTag:
            recommend.set(Attribute_tagGroup, recommendTag)
            relation = recommend.relation(Attribute_productGroup)
            if tagList:
                for goo in tagList:
                    productGroup = ProductGroup()
                    productGroup.get_Object(goo['productGroupId'])
                    if productGroup:
                        relation.remove(productGroup.get_instance())
                base.save_data(recommend)
            for foo in recommendTag:
                productGroup = ProductGroup()
                productGroup.get_Object(foo['productGroupId'])
                if productGroup.get_instance():
                    relation.add(productGroup.get_instance())
            if base.save_data(recommend):
                return True
    return None



def output_Recommend(recommend):
    if recommend:
        A = {
            Attribute_mainImage: get_attribute_mainImage(recommend),
            Attribute_tagGroup: get_attribute_tagGroup(recommend),
            Attribute_state: get_attribute_state(recommend),
            Attribute_imageWidth: get_attribute_imageWidth(recommend),
            Attribute_imageHeight: get_attribute_imageHeight(recommend),
            Attribute_createdAt: get_attribute_createdAt(recommend),
            Attribute_objectId: get_attribute_objectId(recommend),
            Attribute_time: get_attribute_time(recommend),
        }
        return A
    return None
