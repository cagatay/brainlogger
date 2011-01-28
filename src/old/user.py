#===============================================================================
# Created on Aug 20, 2010
# 
# @author: cagatay.yuksel
#===============================================================================

from google.appengine.api import users
from models import userModel

MAX_NICK_LENGTH = 40

class User:
    
    def createUser(self, nickname):
        googleUser = users.get_current_user()
        if not googleUser:
            raise NotSignedIn
        if not nickname.isalnum():
            raise InvalidNick
        if self.getByUserData(googleUser):
            raise UserExists
        if self.getByNickname(nickname):
            raise NickExists
        else:
            user = userModel()
            user.userData = googleUser
            user.nickname = nickname[:MAX_NICK_LENGTH]
            user.put()
    

    # TODO: this function checks only if user is a google user.    
    def getLogInOutURL(self, dest):
        if users.get_current_user():
            return [users.create_logout_url(dest), 'logout' ]
        else:
            return [users.create_login_url(dest), 'login' ]
        
    def getByUserData(self, user):
        user = userModel.all()
        user.filter('userData =', user)
        return user.get()
    
    def getByNickname(self, nickname):
        user = userModel.all()
        user.filter('nickname =', nickname)
        return user.get()
        
class InvalidNick(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
class NickExists(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class NotSignedIn:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
class UserExists:
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)