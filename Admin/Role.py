ROLE_ADMINISTRATOR = 'Administrator'
ROLE_SHOP = 'Shop'
ROLE_PRODUCT = 'ProductAdmin'
ROLE_CUSTOM = 'CustomService'
ROLE_BUSINESS = 'BusinessOperation'
ROLE_APP = 'NormalUser'
ROLE_NONE = 'None'

ROLE = [
    ROLE_NONE,
    ROLE_ADMINISTRATOR,
    ROLE_SHOP,
    ROLE_PRODUCT,
    ROLE_CUSTOM,
    ROLE_BUSINESS,
    ROLE_APP,
]


attribute_name = 'name'


def get_attribute_name(role):
    if role:
        return role.get(attribute_name)
