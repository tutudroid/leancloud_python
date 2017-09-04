import leancloud

from Product.library.base import sys_log
from Product.library import base
from Admin import Role




def setRoleToUser(user, role_name):

    if user is None or role_name is None:
        return

    role_query = leancloud.Query(leancloud.Role)
    role_query.equal_to('name', role_name)
    role_query_list = role_query.find()

    if len(role_query_list) > 0:  # 该角色存在
        administrator_role = role_query_list[0]
        role_query.equal_to('users', user)
        role_query_with_current_user = role_query.find()
        if len(role_query_with_current_user) == 0:
            # 该角色存在，但是当前用户尚未被赋予该角色
            relation = administrator_role.get_users()
            relation.add(user)  # 为当前用户赋予该角色
            administrator_role.save()
            print('role success')
        else:
            # 该角色存在，当前用户已被被赋予该角色
            print('role exist')
            pass
    else:
        # 该角色不存在，可以新建该角色，并把当前用户设置成该角色
        administrator_role = leancloud.Role(role_name)
        relation = administrator_role.get_users()
        relation.add(user)
        administrator_role.save()
        print('create role')


def cancelRoleToUser(user, role_name):
    """
    删除用户的角色
    :param user: 
    :param role_name: 
    :return: 
    """
    if user is None or role_name is None:
        return
    print('enter _cancelRoleToUser ', user)
    role_query = leancloud.Query(leancloud.Role)
    role_query.equal_to('name', role_name)
    role_query_list = role_query.find()

    if len(role_query_list) > 0:  # 该角色存在
        print(role_query_list[0])
        administrator_role = role_query_list[0]
        role_query.equal_to('users', user)
        role_query_with_current_user = role_query.find()
        if len(role_query_with_current_user) > 0:
            # 该角色存在，且当前用户拥有该角色
            relation = administrator_role.get_users()
            relation.remove(user)
            # 为当前用户剥夺该角色
            administrator_role.save()
            print('remove roles')
        else:
            # 该角色存在，当前用户并不拥有该角色
            print('user is not existed')
            pass
    else:
        # 该角色不存在，可以新建该角色，并把当前用户设置成该角色
        print('role is not existed')
        pass
    pass
    return


def deleteUser(objectId):
    """
    删除用户，设置用户的状态位为2
    用户状态位二进制表示：
    00000000 表示正常
    00000010，表示禁止登陆
    00000100，表示删除
    00001000，邮箱未激活
    00010000，未激活
    :return: 
    """
    user = base.queryInstanceThroughId('_User', objectId)
    if user:
        user.set('state', 1)
        base.save_data(user)
    else:
        sys_log('user is not exits')
    pass


def getUserIDThroughName(username):
    """
    使用用户名获得用户Id
    :param username: 
    :return: 
    """
    User = leancloud.Object.extend('_User')
    query = User.query
    query.equal_to('username', username)
    query_list = query.find()
    if query_list:
        user = query_list[0]
    else:
        user = None
    return user


def _getAllRole():
    """
    得到所有的角色信息
    :return: 
    """
    Role1 = leancloud.Object.extend('_Role')
    role_query = Role1.query
    role_query.exists('objectId')
    role_query_list = role_query.find()  # 返回当前用户的角色列表
    role = [
        {
            'name': x.get('name')
        } for x in role_query_list
    ]
    return role


def getRoleUser(role):
    """
    获得某角色的所有用户
    :param role:
    :return:
    """
    Role1 = leancloud.Object.extend('_Role')
    role_query = Role1.query
    role_query.equal_to('name', role)
    role_query_list = role_query.find()

    if role_query_list:
        administrator_role = role_query_list[0]  # 获取该角色对象
        user_relation = administrator_role.relation('users')
        # 查找该角色下的所有用户列表。如果这里有权限问题，请到控制台设置 leancloud.User 对象的权限
        query = user_relation.query
        users_with_role = user_relation.query.find()
        sys_log(users_with_role)
        return users_with_role
    else:
        # 该角色不存在，可以新建该角色，并把当前用户设置成该角色
        pass
    return []



def getRoleAllUser(role):
    """
    获得某角色的所有用户
    :param role:
    :return:
    """
    Role1 = leancloud.Object.extend('_Role')
    role_query = Role1.query
    role_query.equal_to('name', role)
    role_query_list = role_query.find()

    if role_query_list:
        administrator_role = role_query_list[0]  # 获取该角色对象
        user_relation = administrator_role.relation('users')
        # 查找该角色下的所有用户列表。如果这里有权限问题，请到控制台设置 leancloud.User 对象的权限
        query = user_relation.query
        query.limit(1000)
        users_with_role = query.find()
        # sys_log(users_with_role)
        return users_with_role
    else:
        # 该角色不存在，可以新建该角色，并把当前用户设置成该角色
        pass
    return []


def getAllUser():
    User = leancloud.Object.extend('_User')
    query = User.query
    query.not_equal_to('state', 1)
    query_list = query.find()
    if query_list:
        return query_list
    else:
        return None


def getUserInstance(uniqueId):
    if uniqueId:
        user = base.queryInstanceAttributeFirst('_User', 'uniqueId', int(uniqueId))
        if user:
            return user
        else:
            sys_log('user not found')
    else:
        sys_log('uniqueId is null')
    return None


def getUserRole(uniqueId):
    """
    获得用户的角色
    :param uniqueId: 
    :return: 
    """
    if uniqueId:
        user = getUserInstance(int(uniqueId))
        if user:
            roleList = get_attribute_role(user)
            if roleList:
                return roleList
            else:
                sys_log('role is null')
        else:
            sys_log('user not found')
    else:
        sys_log('uniqueId is null')
    return None


def cancelAllRole(objectId):
    """
    取消用户的所有角色
    :param objectId: 
    :return: 
    """
    if objectId:
        user = base.getInstanceThroughId(CLASS_NAME, objectId)
        if user:
            user_relation = user.relation('role')
            roleList = base.get_relation_data(user.get('objectId'), '_User', 'role')
            if roleList:
                for role in roleList:
                    role = base.queryInstanceThroughId('_Role', role.id)
                    role_relation = role.relation('users')
                    role_relation.remove(user)
                    if base.save_data(role):
                        user_relation.remove(role)
                base.save_data(user)
            else:
                sys_log('role is null')
        else:
            sys_log('user not found')
    else:
        sys_log('uniqueId is null')


def addAllRole(uniqueId, roleList):
    """
    增加用户的所有角色
    :param uniqueId: 
    :param roleList:
    :return: 
    """
    if uniqueId and roleList:
        user = getUserInstance(int(uniqueId))
        if user:
            user_relation = user.relation('role')
            for roleName in roleList:
                role = base.queryInstanceAttributeFirst('_Role', 'name', roleName)
                if role:
                    role_relation = role.relation('users')
                    role_relation.add(user)
                    if base.save_data(role):
                        user_relation.add(role)
            base.save_data(user)
        else:
            sys_log('user not found')
    else:
        sys_log('uniqueId is null')


def delUser(uniqueId):
    if uniqueId:
        user = getUserInstance(int(uniqueId))
        if user:
            user.set('state', 1)
            if base.save_data(user):
                pass
            else:
                sys_log('delete user fail')
        else:
            sys_log('user not found')
    else:
        sys_log('uniqueId is null')


def forbid_user(uniqueId, ban):
    if uniqueId:
        user = getUserInstance(int(uniqueId))
        if user:
            user.set('state', int(ban))
            if base.save_data(user):
                sys_log('forbid success')
                pass
            else:
                sys_log('forbid user fail')
        else:
            sys_log('user not found')
    else:
        sys_log('uniqueId is null')


def reset_user_password(uniqueId, password):
    if uniqueId and password:
        user = getUserInstance(uniqueId)
        user.set('password', password)
        if base.save_data(user):
            sys_log('password modify success')
            return True
        else:
            sys_log('modify password fail')
    else:
        sys_log('uniqueId is null')
    return False


def create_user(username, password):
    if username and password:
        user = leancloud.User()
        user.set_username(username)
        user.set_password(password)
        user.set('state', 2)
        if base.save_data(user):
            return user
    else:
        sys_log('username or password is null')
    return None


def user_exists(username):
    if username:
        query = base.queryInstanceAttributeFirst('_User', 'username', username)
        print(query)
        if query:
            return True
        else:
            return False
    else:
        sys_log('parameter is null')
    return False




CLASS_NAME = '_User'
Attribute_objectId = 'objectId'
Attribute_uniqueId = 'uniqueId'
Attribute_username = 'username'
Attribute_avatar = 'avatar'
Attribute_shop = 'shop'
Attribute_mobilePhoneNumber = 'mobilePhoneNumber'
Attribute_role = 'role'
Attribute_name = 'name'
Attribute_password = 'password'
Attribute_state = 'state'

STATE_OK = 0
STATE_DELETE = -1
STATE_FORBIDDEN = 1
STATE_NO_AUDIT = 2


def get_User(objectId):
    if objectId:
        return base.queryInstanceThroughId(CLASS_NAME, objectId)
    return None


def forbid_User(user, ban):
    if user and ban is not None:
        user.set('state', int(ban))
        if base.save_data(user):
            sys_log('forbid success')
            pass
        else:
            sys_log('forbid user fail')
    else:
        sys_log('user not found')


def get_attribute_uniqueId(user):
    if user:
        return user.get(Attribute_uniqueId)
    return None


def get_attribute_username(user):
    if user:
        return user.get(Attribute_username)
    return None


def get_attribute_avatar(user):
    if user:
        return user.get(Attribute_avatar)
    return None


def get_attribute_shop(user):
    if user:
        return user.get(Attribute_shop)
    return None


def get_attribute_mobilePhoneNumber(user):
    if user:
        return user.get(Attribute_mobilePhoneNumber)
    return None


def get_attribute_objectId(user):
    if user:
        return user.get(Attribute_objectId)
    return None


def get_attribute_role(user):
    if user:
        roleList = base.get_relation_data(user.get('objectId'), CLASS_NAME, Attribute_role)
        if roleList:
            return [foo.get(Role.attribute_name) for foo in roleList]
        else:
            sys_log('role is null')
    else:
        sys_log('user not found')
    return None


def delete_attribute_role(user):
    """
    取消用户的所有角色
    :param user: 
    :return: 
    """
    if user:
        user_relation = user.relation('role')
        roleList = base.get_relation_data(user.get('objectId'), '_User', 'role')
        if roleList:
            for role in roleList:
                role = base.queryInstanceThroughId('_Role', role.id)
                role_relation = role.relation('users')
                role_relation.remove(user)
                if base.save_data(role):
                    user_relation.remove(role)
            base.save_data(user)
        else:
            sys_log('role is null')
    else:
        sys_log('user not found')


def set_attribute_password(user, password):
    if user and password:
        user.set(Attribute_password, password)
        if base.save_data(user):
            sys_log('password modify success')
            return True
        else:
            sys_log('modify password fail')
    else:
        sys_log('uniqueId is null')
    return False


def set_attribute_role(user, roleList):
    """
    增加用户的所有角色
    :param user: 
    :param roleList:
    :return: 
    """
    if user:
        user_relation = user.relation('role')
        for roleName in roleList:
            role = base.queryInstanceAttributeFirst('_Role', 'name', roleName)
            if role:
                role_relation = role.relation('users')
                role_relation.add(user)
                if base.save_data(role):
                    user_relation.add(role)
        base.save_data(user)
    else:
        sys_log('user not found')


def refresh_attribute_sessionToken(current_user, objectId):
    user = current_user.create_follower_query(objectId)
    print(user)
    print(user.get_session_token())


def output_User(user):
    if user:
        A = {
            Attribute_uniqueId: get_attribute_uniqueId(user),
            Attribute_username: get_attribute_username(user),
            Attribute_avatar: get_attribute_avatar(user),
            Attribute_shop: get_attribute_shop(user),
            Attribute_objectId: get_attribute_objectId(user),
            Attribute_mobilePhoneNumber: get_attribute_mobilePhoneNumber(user),
            Attribute_name: user.get(Attribute_name),
            Attribute_role: get_attribute_role(user),
        }
        return A
    return None


def get_all_app_user(skip, limit):
    USER1 = leancloud.Object.extend('_User')
    query = USER1.query
    query.exists('mobilePhoneNumber')
    query.equal_to('shop', None)
    if skip:
        query.skip((int(skip) - 1) * int(limit))
        query.limit(int(limit))
    else:
        query.limit(10)
    role_query_list = query.find()
    if len(role_query_list):
        return role_query_list
    return []


def count_all_app_user():
    USER1 = leancloud.Object.extend('_User')
    role_query = USER1.query
    role_query.exists('mobilePhoneNumber')
    role_query.equal_to('shop', None)
    count = role_query.count()
    return count


def count_User(role):
    if role:
        role_query = base.queryInstanceAttributeFirst('_Role', Attribute_name, role)
        if role_query:
            user_relation = role_query.relation('users')
            # 查找该角色下的所有用户列表。如果这里有权限问题，请到控制台设置 leancloud.User 对象的权限
            query = user_relation.query
            count = query.count()
            print(count)
            return count
    return 0


def get_Role_User(role, skip, limit):
    """
    获得某角色的所有用户
    :param role:
    :return:
    """
    if role:
        role_query = base.queryInstanceAttributeFirst('_Role', Attribute_name, role)
        user_relation = role_query.relation('users')
        # 查找该角色下的所有用户列表。如果这里有权限问题，请到控制台设置 leancloud.User 对象的权限
        query = user_relation.query
        if skip:
            query.skip((int(skip) - 1) * int(limit))
            query.limit(int(limit))
        else:
            query.limit(10)
        users_with_role = query.find()
        sys_log(users_with_role)
        return users_with_role
    return []
