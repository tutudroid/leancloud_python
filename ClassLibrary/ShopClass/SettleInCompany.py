from ClassLibrary.ShopClass.SettleIn import *


class SettleInCompany(SettleIn):
    def __init__(self):
        super(SettleInCompany, self).__init__()
        self.className = self.__class__.__name__

    def get_attribute_businessLicense(self):
        if self.instance:
            return self.instance.get(attribute_businessLicense)
        return None

    def get_attribute_managerRealName(self):
        if self.instance:
            return self.instance.get(attribute_managerRealName)
        return None

    def get_attribute_managerEmail(self):
        if self.instance:
            return self.instance.get(attribute_managerEmail)
        return None

    def get_attribute_managerPhoneNumber(self):
        if self.instance:
            return self.instance.get(attribute_managerPhoneNumber)
        return None

    def get_attribute_uniformSocialCreditCode(self):
        if self.instance:
            return self.instance.get(attribute_uniformSocialCreditCode)
        return None

    def get_attribute_legalPersonName(self):
        if self.instance:
            return self.instance.get(attribute_legalPersonName)
        return None

    def get_attribute_legalPersonEmail(self):
        if self.instance:
            return self.instance.get(attribute_legalPersonEmail)
        return None

    def get_attribute_legalPersonPhoneNumber(self):
        if self.instance:
            return self.instance.get(attribute_legalPersonPhoneNumber)
        return None

    def get_attribute_legalPersonExpireTimeStart(self):
        if self.instance:
            return self.instance.get(attribute_legalPersonExpireTimeStart)
        return None

    def get_attribute_legalPersonIdCard(self):
        if self.instance:
            return self.instance.get(attribute_legalPersonIdCard)
        return None

    def get_attribute_legalPersonExpireTimeEnd(self):
        if self.instance:
            return self.instance.get(attribute_legalPersonExpireTimeEnd)
        return None

    def get_attribute_legalPersonFrontIdCard(self):
        if self.instance and isinstance(self.instance.get(attribute_legalPersonFrontIdCard), ISINSTANCE_FILE):
            return self.instance.get(attribute_legalPersonFrontIdCard).url
        return None

    def get_attribute_legalPersonBackIdCard(self):
        if self.instance and isinstance(self.instance.get(attribute_legalPersonBackIdCard), ISINSTANCE_FILE):
            return self.instance.get(attribute_legalPersonBackIdCard).url
        return None

    def set_attribute_businessLicense(self, value):
        if self.instance:
            if value != self.instance.get(attribute_businessLicense):
                self.instance.set(attribute_businessLicense, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_managerRealName(self, value):
        if self.instance:
            if value != self.instance.get(attribute_managerRealName):
                self.instance.set(attribute_managerRealName, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_managerEmail(self, value):
        if self.instance:
            if value != self.instance.get(attribute_managerEmail):
                self.instance.set(attribute_managerEmail, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_managerPhoneNumber(self, value):
        if self.instance:
            if value != self.instance.get(attribute_managerPhoneNumber):
                self.instance.set(attribute_managerPhoneNumber, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_uniformSocialCreditCode(self, value):
        if self.instance:
            if value != self.instance.get(attribute_uniformSocialCreditCode):
                self.instance.set(attribute_uniformSocialCreditCode, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_legalPersonName(self, value):
        if self.instance:
            if value != self.instance.get(attribute_legalPersonName):
                self.instance.set(attribute_legalPersonName, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_legalPersonEmail(self, value):
        if self.instance:
            if value != self.instance.get(attribute_legalPersonEmail):
                self.instance.set(attribute_legalPersonEmail, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_legalPersonPhoneNumber(self, value):
        if self.instance:
            if value != self.instance.get(attribute_legalPersonPhoneNumber):
                self.instance.set(attribute_legalPersonPhoneNumber, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_legalPersonIdCard(self, value):
        if self.instance:
            if value != self.instance.get(attribute_legalPersonIdCard):
                self.instance.set(attribute_legalPersonIdCard, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_legalPersonExpireTimeStart(self, value):
        if self.instance:
            if value != self.instance.get(attribute_legalPersonExpireTimeStart):
                self.instance.set(attribute_legalPersonExpireTimeStart, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_legalPersonExpireTimeEnd(self, value):
        if self.instance:
            if value != self.instance.get(attribute_legalPersonExpireTimeEnd):
                self.instance.set(attribute_legalPersonExpireTimeEnd, value)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_legalPersonFrontIdCard(self, value):
        if self.instance:
            imageFile = Base.save_image(value)
            if imageFile:
                self.instance.set(attribute_legalPersonFrontIdCard, imageFile)
                if self.__save_instance__():
                    return True
        return None

    def set_attribute_legalPersonBackIdCard(self, value):
        if self.instance:
            imageFile = Base.save_image(value)
            if imageFile:
                self.instance.set(attribute_legalPersonBackIdCard, imageFile)
                if self.__save_instance__():
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

                attribute_businessLicense: self.get_attribute_businessLicense(),
                attribute_managerRealName: self.get_attribute_managerRealName(),
                attribute_managerEmail: self.get_attribute_managerEmail(),
                attribute_managerPhoneNumber: self.get_attribute_managerPhoneNumber(),
                attribute_uniformSocialCreditCode: self.get_attribute_uniformSocialCreditCode(),
                attribute_legalPersonName: self.get_attribute_legalPersonName(),
                attribute_legalPersonEmail: self.get_attribute_legalPersonEmail(),
                attribute_legalPersonPhoneNumber: self.get_attribute_legalPersonPhoneNumber(),
                attribute_legalPersonIdCard: self.get_attribute_legalPersonIdCard(),
                attribute_legalPersonExpireTimeStart: self.get_attribute_legalPersonExpireTimeStart(),
                attribute_legalPersonExpireTimeEnd: self.get_attribute_legalPersonExpireTimeEnd(),
                attribute_legalPersonFrontIdCard: self.get_attribute_legalPersonFrontIdCard(),
                attribute_legalPersonBackIdCard: self.get_attribute_legalPersonBackIdCard(),
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
            attribute_businessLicense: request.POST.get(attribute_businessLicense, ''),
            attribute_managerRealName: request.POST.get(attribute_managerRealName, ''),
            attribute_managerEmail: request.POST.get(attribute_managerEmail, ''),
            attribute_managerPhoneNumber: request.POST.get(attribute_managerPhoneNumber, ''),
            attribute_uniformSocialCreditCode: request.POST.get(attribute_uniformSocialCreditCode, ''),
            attribute_legalPersonName: request.POST.get(attribute_legalPersonName, ''),
            attribute_legalPersonEmail: request.POST.get(attribute_legalPersonEmail, ''),
            attribute_legalPersonPhoneNumber: request.POST.get(attribute_legalPersonPhoneNumber, ''),
            attribute_legalPersonIdCard: request.POST.get(attribute_legalPersonIdCard, ''),
            attribute_legalPersonExpireTimeStart: request.POST.get(attribute_legalPersonExpireTimeStart, ''),
            attribute_legalPersonExpireTimeEnd: request.POST.get(attribute_legalPersonExpireTimeEnd, ''),
            attribute_legalPersonFrontIdCard: request.POST.get(attribute_legalPersonFrontIdCard, ''),
            attribute_legalPersonBackIdCard: request.POST.get(attribute_legalPersonBackIdCard, ''),
        }
        return data

    def create_SettleIn(self, data):
        self.create_SettleInBase(data)

        if data[attribute_businessLicense]:
            self.set_attribute_businessLicense(data[attribute_businessLicense])
        if data[attribute_managerRealName]:
            self.set_attribute_managerRealName(data[attribute_managerRealName])
        if data[attribute_managerEmail]:
            self.set_attribute_managerEmail(data[attribute_managerEmail])
        if data[attribute_managerPhoneNumber]:
            self.set_attribute_managerPhoneNumber(data[attribute_managerPhoneNumber])
        if data[attribute_uniformSocialCreditCode]:
            self.set_attribute_uniformSocialCreditCode(data[attribute_uniformSocialCreditCode])
        if data[attribute_legalPersonName]:
            self.set_attribute_legalPersonName(data[attribute_legalPersonName])
        if data[attribute_legalPersonEmail]:
            self.set_attribute_legalPersonEmail(data[attribute_legalPersonEmail])

        if data[attribute_legalPersonPhoneNumber]:
            self.set_attribute_legalPersonPhoneNumber(data[attribute_legalPersonPhoneNumber])
        if data[attribute_legalPersonIdCard]:
            self.set_attribute_legalPersonIdCard(data[attribute_legalPersonIdCard])
        if data[attribute_legalPersonExpireTimeStart]:
            self.set_attribute_legalPersonExpireTimeStart(data[attribute_legalPersonExpireTimeStart])
        if data[attribute_legalPersonExpireTimeEnd]:
            self.set_attribute_legalPersonExpireTimeEnd(data[attribute_legalPersonExpireTimeEnd])
        if data[attribute_legalPersonFrontIdCard]:
            self.set_attribute_legalPersonFrontIdCard(data[attribute_legalPersonFrontIdCard])
        if data[attribute_legalPersonBackIdCard]:
            self.set_attribute_legalPersonBackIdCard(data[attribute_legalPersonBackIdCard])
        self.set_attribute_state(SETTLE_IN_STATE_0)