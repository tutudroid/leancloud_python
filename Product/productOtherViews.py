from Error_Page import *
from ClassLibrary.ProductClass.ProductService import ProductService


@login_required
@require_http_methods(['GET'])
def AllProductService(request):
    """
    商品组详情
    :param request: 
    :return: 
    """
    productService = ProductService()
    return return_data(Class_Name_ProductService, productService.get_ProductService_All())


@login_required
@require_http_methods(['GET'])
def EditProductService(request):
    objectId = request.GET.get(attribute_objectId, '')
    state = request.GET.get(attribute_state, '')
    name = request.GET.get(attribute_name, '')
    briefDescription = request.GET.get(attribute_briefDescription, '')
    productService = ProductService()
    if objectId:
        if productService.get_Object(objectId):
            if STATE_DELETE == int(state):
                productService.destroy_Object()
            productService.set_attribute_value(attribute_name, name)
            productService.set_attribute_value(attribute_briefDescription, briefDescription)
            return return_data(Class_Name_ProductService, productService.output_ProductService())
        return return_msg('no found productService')
    if name and briefDescription:
        productService.create_Object()
        productService.set_attribute_value(attribute_name, name)
        productService.set_attribute_value(attribute_briefDescription, briefDescription)
        return return_data(Class_Name_ProductService, productService.output_ProductService())
    return return_msg('parameter is error')
