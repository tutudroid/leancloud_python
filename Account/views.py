from Error_Page import *
from ClassLibrary.UserClass.User import _User
from ClassLibrary.ShopClass.SettleInApplication import SettleInApplication


@require_http_methods(['POST'])
def resetPassword(request):
    """
    用户忘记密码时，用户请求重置用户密码
    :param request: 
    :return: 
    """
    phoneNumber = request.POST.get(attribute_phoneNumber, '')
    verifyCode = request.POST.get(attribute_verifyCode, '')
    password = request.POST.get(attribute_password, '')
    passwordSure = request.POST.get(attribute_passwordSure, '')
    if len(phoneNumber) == 11 and phoneNumber.isdigit() and password == passwordSure:
        try:
            leancloud.cloudfunc.verify_sms_code(phoneNumber, verifyCode)
        except LeanCloudError as e:
            return return_msg( e.error )
        try:
            leancloud.User.reset_password_by_sms_code(phoneNumber, password)
        except LeanCloudError as e:
            return return_msg( e.error )
        return return_msg( 'success' )
    return return_msg( 'fail' )


@require_http_methods(['POST', 'GET'])
def login(request):
    """
    :param request: 
    :return: 
    用户登陆到系统
    :param request:
    :return:
    """
    if request.method == 'POST':
        username = request.POST.get(attribute_username)
        password = request.POST.get(attribute_password)
        if username and password:
            user = leancloud.User()
            try:
                user.login(username, password)
                if user:
                    if user.get(attribute_state) != 0:
                        if user.get(attribute_state) == STATE_FORBIDDEN:
                            print('user is forbidden')
                            return return_msg( '禁止该用户登陆', status=404 )
                        if user.get(attribute_state) == STATE_DELETE:
                            print('user is delete')
                            return return_msg( '该用户不存在', status=404 )
                    print('user state is not true')
                    return HttpResponseRedirect('/Account/Profile/')
                return return_msg( '用户不存在', status=404 )
            except LeanCloudError as e:
                print(e.error)
                return return_msg( e.error, status=404 )
        print('username or password is null')
    if request.method == 'GET':
        return render(request, 'login.html')
    return illegal_access()


@login_required
def profile(request):
    """
    用户登陆系统后，跳转到用户页面
    :param request: 
    :return: 
    """
    # 得到返回角色的主页
    current_user = leancloud.User.get_current()
    user = _User()
    user.set_instance(current_user)
    userData = user.output_User()
    role = user.get_attribute_role()
    if role and 'ProductAdmin' in role:
        settleInApplication = SettleInApplication()
        if not settleInApplication.find_User(current_user):
            settleInApplication.create_Object()
            settleInApplication.set_attribute_user(user.get_instance())
    return render(request, 'index.html', {'User': userData})


@login_required
def logout(request):
    """
    注销当前登陆的用户
    :param request: 
    :return: 
    """
    user = leancloud.User.get_current()
    if user:
        user.logout()
    return HttpResponseRedirect('/Account/Login/')


@require_http_methods(['GET'])
def getVerifyCode_Register(request):
    """
    通过手机号，获得验证码
    验证时不需要检查和账户手机号进行检查，仅仅检查该手机号是否已被注册使用
    :param request: 
    :return: 
    """
    phoneNumber = request.GET.get(attribute_phoneNumber)
    if len(phoneNumber) == 11 and phoneNumber.isdigit():
        user = _User()
        user.get_User_phoneNumber(phoneNumber)
        if user:
            return return_msg( '该手机号已注册' )
        else:
            try:
                leancloud.cloudfunc.request_sms_code(phone_number=phoneNumber, template="萌生活", params={})
                message = '短信发送成功'
            except LeanCloudError as e:
                message = e.error
            return return_msg( message )
    return illegal_access()


@require_http_methods(['GET'])
def getVerifyCode(request):
    """
    通过手机号，获得验证码
    验证时不需要检查和账户手机号进行检查，仅仅检查该手机号是否已被注册使用
    :param request: 
    :return: 
    """
    phoneNumber = request.GET.get(attribute_phoneNumber)
    if len(phoneNumber) == 11 and phoneNumber.isdigit():
        try:
            leancloud.User.request_password_reset_by_sms_code(phoneNumber)
            message = 'success'
        except LeanCloudError as e:
            message = e.error
        return return_msg( message )
    return illegal_access()


@login_required
@require_http_methods(['GET'])
def getVerifyCode_PhoneNumber(request):
    """
    通过手机号，获得验证码
    验证时需要检查是否和账户手机号一致
    :param request: 
    :return: 
    """
    phoneNumber = request.GET.get('phoneNumber')
    user = leancloud.User.get_current()
    userPhoneNumber = user.get_mobile_phone_number()
    if userPhoneNumber != phoneNumber:
        return return_msg( '输入手机号与注册手机号不一致' )

    if len(phoneNumber) == 11 and phoneNumber.isdigit():
        try:
            leancloud.cloudfunc.request_sms_code(phone_number=phoneNumber, template="萌生活", params={})
            return return_msg( '短信发送成功' )
        except LeanCloudError as e:
            return return_msg( e.error )
    return return_msg( '手机号不符合格式' )
