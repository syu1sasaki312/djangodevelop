import re


class MyValidators():

    @staticmethod
    def isPostNumber(post):
        if post is None :
            return False
        if MyValidators.isNumber(post.replace('-', '')) is False:
            return False
        if len(post) != 8:
            return False
        if not re.match('\d{3}-\d{4}', post) :
            return False
        return True

    @staticmethod
    def isTelephoneNumber(phone):
        if phone is None :
            return False
        if MyValidators.isNumber(phone.replace('-', '')) is False:
            return False
        if len(phone) < 12 or len(phone) > 13:
            return False
        if (not re.match('\d{3}-\d{3}-\d{4}', phone) and
            not re.match('\d{3}-\d{4}-\d{4}', phone) ):
            return False
        return True

    @staticmethod
    def isFaxNumber(fax):
        if fax is None :
            return False
        if MyValidators.isNumber(fax.replace('-', '')) is False:
            return False
        if len(fax) != 12:
            return False
        if re.match('\d{3}-\d{3}-\d{4}', fax) is None :
            return False
        return True

    @staticmethod
    def isNumber(s):
        if re.fullmatch('[0-9]+', s) is None:
            return False
        return True

