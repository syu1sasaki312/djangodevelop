import re


class MyValidators():

    @staticmethod
    def isTelephoneNumber(phone):
        if MyValidators.isOnlyNum(phone.replace('-', '')) is False:
            return False
        if len(phone) < 12 or len(phone) > 13:
            return False
        if (re.match('\d{3}-\d{3}-\d{4}', phone) is None and
            re.match('\d{3}-\d{4}-\d{4}', phone) is None ):
            return False
        return True

    @staticmethod
    def isFaxNumber(fax):
        if MyValidators.isOnlyNum(fax.replace('-', '')) is False:
            return False
        if len(fax) != 12:
            return False
        if re.match('\d{3}-\d{3}-\d{4}', fax) is None :
            return False
        return True

    @staticmethod
    def isOnlyNum(s):
        if re.fullmatch('[0-9]+', s) is None:
            return False
        return True

