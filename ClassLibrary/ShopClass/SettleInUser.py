from ClassLibrary.ShopClass.SettleIn import *


class SettleInUser(SettleIn):
    def __init__(self):
        super(SettleInUser, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_realName(self):
        if self.instance:
            return self.instance.get(attribute_realName)
        return None

    def get_attribute_email(self):
        if self.instance:
            return self.instance.get(attribute_email)
        return None

    def get_attribute_phoneNumber(self):
        if self.instance:
            return self.instance.get(attribute_phoneNumber)
        return None

    def get_attribute_idCard(self):
        if self.instance:
            return self.instance.get(attribute_idCard)
        return None

    def get_attribute_idCardExpireTimeStart(self):
        if self.instance:
            return self.instance.get(attribute_idCardExpireTimeStart)
        return None


    def get_attribute_idCardExpireTimeEnd(self):
        if self.instance:
            return self.instance.get(attribute_idCardExpireTimeEnd)
        return None


    def get_attribute_handIdCard(self):
        if self.instance and isinstance(self.instance.get(attribute_handIdCard), ISINSTANCE_FILE):
            return self.instance.get(attribute_handIdCard).url
        return None

    def get_attribute_frontIdCard(self):
        if self.instance and isinstance(self.instance.get(attribute_frontIdCard), ISINSTANCE_FILE):
            return self.instance.get(attribute_frontIdCard).url
        return None

    def get_attribute_backIdCard(self):
        if self.instance and isinstance(self.instance.get(attribute_backIdCard), ISINSTANCE_FILE):
            return self.instance.get(attribute_backIdCard).url
        return None

    def set_attribute_realName(self, value):
        if self.instance:
            if value != self.instance.get(attribute_realName):
                self.instance.set(attribute_realName, value)
                if self.save_instance():
                    return True
        return None

    def set_attribute_phoneNumber(self, value):
        if self.instance:
            if value != self.instance.get(attribute_phoneNumber):
                self.instance.set(attribute_phoneNumber, value)
                if self.save_instance():
                    return True
        return None


    def set_attribute_email(self, value):
        if self.instance:
            if value != self.instance.get(attribute_email):
                self.instance.set(attribute_email, value)
                if self.save_instance():
                    return True
        return None

    def set_attribute_idCard(self, value):
        if self.instance:
            if value != self.instance.get(attribute_idCard):
                self.instance.set(attribute_idCard, value)
                if self.save_instance():
                    return True
        return None

    def set_attribute_idCardExpireTimeStart(self, value):
        if self.instance:
            if value != self.instance.get(attribute_idCardExpireTimeStart):
                self.instance.set(attribute_idCardExpireTimeStart, value)
                if self.save_instance():
                    return True
        return None

    def set_attribute_idCardExpireTimeEnd(self, value):
        if self.instance:
            if value != self.instance.get(attribute_idCardExpireTimeEnd):
                self.instance.set(attribute_idCardExpireTimeEnd, value)
                if self.save_instance():
                    return True
        return None

    def set_attribute_handIdCard(self, value):
        if self.instance:
            imageFile = Base.save_image(value)
            if imageFile:
                self.instance.set(attribute_handIdCard, imageFile)
                if self.save_instance():
                    return True
        return None

    def set_attribute_frontIdCard(self, value):
        if self.instance:
            imageFile = Base.save_image(value)
            if imageFile:
                self.instance.set(attribute_frontIdCard, imageFile)
                if self.save_instance():
                    return True
        return None

    def set_attribute_backIdCard(self, value):
        if self.instance:
            imageFile = Base.save_image(value)
            if imageFile:
                self.instance.set(attribute_backIdCard, imageFile)
                if self.save_instance():
                    return True
        return None

    def output_SettleIn(self):
        if self.instance:
            data = {
                attribute_objectId: self.get_attribute_objectId(),
                attribute_state: self.get_attribute_state(),


                attribute_alipay: self.get_attribute_alipay(),
                attribute_shopName: self.get_attribute_shopName(),
                attribute_brandName: self.get_attribute_brandName(),
                attribute_brandLogo: self.get_attribute_brandLogo(),
                attribute_brandDescription: self.get_attribute_brandDescription(),

                attribute_phoneNumber: self.get_attribute_phoneNumber(),
                attribute_realName: self.get_attribute_realName(),
                attribute_email: self.get_attribute_email(),
                attribute_idCardExpireTimeStart: self.get_attribute_idCardExpireTimeStart(),
                attribute_idCardExpireTimeEnd: self.get_attribute_idCardExpireTimeEnd(),
                attribute_handIdCard: self.get_attribute_handIdCard(),
                attribute_frontIdCard: self.get_attribute_frontIdCard(),
                attribute_backIdCard: self.get_attribute_backIdCard(),
                attribute_idCard: self.get_attribute_idCard(),
            }
            return data

    def input_SettleIn(self, request):
        self.instance = self.instance
        data = {
            attribute_shopType: request.POST.get(attribute_shopType, ''),
            attribute_objectId: request.POST.get(attribute_objectId, ''),
            attribute_alipay: request.POST.get(attribute_alipay, ''),
            attribute_shopName: request.POST.get(attribute_shopName, ''),
            attribute_brandName: request.POST.get(attribute_brandName, ''),
            attribute_brandLogo: request.POST.get(attribute_brandLogo, ''),
            attribute_brandDescription: request.POST.get(attribute_brandDescription, ''),
            attribute_realName: request.POST.get(attribute_realName, ''),
            attribute_email: request.POST.get(attribute_email, ''),
            attribute_idCardExpireTimeStart: request.POST.get(attribute_idCardExpireTimeStart, ''),
            attribute_idCardExpireTimeEnd: request.POST.get(attribute_idCardExpireTimeEnd, ''),
            attribute_handIdCard: request.POST.get(attribute_handIdCard, ''),
            attribute_frontIdCard: request.POST.get(attribute_frontIdCard, ''),
            attribute_backIdCard: request.POST.get(attribute_backIdCard, ''),
            attribute_phoneNumber: request.POST.get(attribute_phoneNumber, ''),
            attribute_idCard: request.POST.get(attribute_idCard, ''),
        }
        return data

    def create_SettleIn(self, data):
        self.create_SettleInBase(data)

        if data[attribute_realName]:
            self.set_attribute_realName(data[attribute_realName])
        if data[attribute_email]:
            self.set_attribute_email(data[attribute_email])
        if data[attribute_idCardExpireTimeStart]:
            self.set_attribute_idCardExpireTimeStart(data[attribute_idCardExpireTimeStart])
        if data[attribute_idCardExpireTimeEnd]:
            self.set_attribute_idCardExpireTimeEnd(data[attribute_idCardExpireTimeEnd])
        if data[attribute_handIdCard]:
            self.set_attribute_handIdCard(data[attribute_handIdCard])
        if data[attribute_frontIdCard]:
            self.set_attribute_frontIdCard(data[attribute_frontIdCard])
        if data[attribute_backIdCard]:
            self.set_attribute_backIdCard(data[attribute_backIdCard])
        if data[attribute_phoneNumber]:
            self.set_attribute_phoneNumber(data[attribute_phoneNumber])
        if data[attribute_idCard]:
            self.set_attribute_idCard(data[attribute_idCard])
        self.set_attribute_state(SETTLE_IN_STATE_0)

        return None
