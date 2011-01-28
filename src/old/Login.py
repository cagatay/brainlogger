'''
Created on Aug 13, 2010

@author: cagatay.yuksel
'''

from google.appengine.ext import webapp
from google.appengine.api import users
import urllib

class Login(webapp.RequestHandler):
    
    def get(self):
        
        returnAddress = self.request.get("return")
        
        googleUser = users.get_current_user()
        if googleUser:
            self.redirect('/newUser?return=' + urllib.quote_plus(returnAddress))
        else:
            self.redirect(users.create_login_url(self.request.uri))