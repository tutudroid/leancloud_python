from django.http import HttpResponseRedirect
from functools import wraps
import leancloud
from ClassLibrary.UserClass.User import _User


def abort():
    return HttpResponseRedirect('/Account/Login/')


def illegal_permission():
    return HttpResponseRedirect('/NoFound/')


def login_required(func):
    """
    检查用户是否已经登陆
    :param func: 
    :return: 
    """
    @wraps(func)
    def secret_view(*args, **kwargs):
        current_user = leancloud.User.get_current()
        if current_user and current_user.is_authenticated():
            if current_user.get('state') != 0:
                return abort()
            return func(*args, **kwargs)
        else:
            print('user is not exist')
            return abort()
    return secret_view



def auto_login(func):
    """
    自动登陆
    :param func: 
    :return: 
    """
    @wraps(func)
    def secret_view(*args, **kwargs):
        current_user = leancloud.User.get_current()
        if current_user and current_user.is_authenticated():
            return func(*args, **kwargs)
        else:
            print('user is not exist')
            return abort()
    return secret_view


def permissions(roles):
    """
    只允许该角色的用户登陆
    :param roles: 
    :return: 
    """
    def _permission(func):
        @wraps(func)
        def __permission(*args, **kwargs):
            return func(*args, **kwargs)
        return __permission
    return _permission



def permission(arg):
    """
    只允许该角色的用户登陆
    :param arg: 
    :return: 
    """
    def _permission(func):
        @wraps(func)
        def __permission(*args, **kwargs):
            return func(*args, **kwargs)
        return __permission
    return _permission


def permissions1(roles):
    """
    只允许该角色的用户登陆
    :param roles: 
    :return: 
    """
    def _permission(func):
        @wraps(func)
        def __permission(*args, **kwargs):
            user = leancloud.User.get_current()
            if user:
                # 获得用户的角色
                userInstance = _User()
                userInstance.set_instance(user)
                role_query_list = userInstance.get_attribute_role()
                role_verify = False
                # 返回当前用户的角色列表
                if role_query_list and roles:
                    for x in role_query_list:
                        if x in roles:
                            role_verify = True
                            break
                if role_verify is True:
                    return func(*args, **kwargs)
                else:
                    return illegal_permission()
            else:

                return abort()

        return __permission
    return _permission



def permission1(arg):
    """
    只允许该角色的用户登陆
    :param arg: 
    :return: 
    """
    def _permission(func):
        @wraps(func)
        def __permission(*args, **kwargs):
            user = leancloud.User.get_current()
            if user:
                # 获得用户的角色
                userInstance = _User()
                userInstance.set_instance(user)
                role_query_list = userInstance.get_attribute_role()
                role_verify = False
                # 返回当前用户的角色列表
                if role_query_list:
                    for x in role_query_list:
                        if x == arg:
                            role_verify = True
                if role_verify is True:
                    return func(*args, **kwargs)
                else:
                    return illegal_permission()
            else:

                return abort()

        return __permission
    return _permission


def not_permission(arg):
    """
    限制该角色的用户登陆
    :param arg: 
    :return: 
    """
    def _permission(func):
        @wraps(func)
        def __permission(*args, **kwargs):
            user = leancloud.User.get_current()
            if user:
                # 获得用户的角色
                userInstance = _User()
                userInstance.set_instance(user)
                role_query_list = userInstance.get_attribute_role()
                role_verify = False
                # 返回当前用户的角色列表
                if role_query_list:
                    for x in role_query_list:
                        if x == arg:
                            role_verify = True
                if role_verify is True:
                    return illegal_permission()
                else:
                    return func(*args, **kwargs)
            else:
                return abort()
        return __permission

    return _permission

# 可以在每个用户组中将该函数进行扩展，判断是否是该用户组的用户，如果不是，则剔除
