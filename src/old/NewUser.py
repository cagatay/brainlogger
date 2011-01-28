'''
Created on Aug 13, 2010

@author: cagatay.yuksel
'''
import os
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template
from User2 import User

class NewUser(webapp.RequestHandler):
    def get(self):
        
        googleUser = users.get_current_user()
        
        if googleUser:
            template_dict = {}
        
            path = os.path.join(os.path.dirname(__file__), "pages/newUserTemplate.html")
            self.response.out.write(template.render(path, template_dict))
        else: 
            self.redirect('/')
    
    def post(self):
        
        nickname = self.request.get("nickname")
        #returnAddress = self.request.get("return")
        
        googleUser = users.get_current_user()
        message = ""
        
        lookUser = User.all()
        lookUser.filter("userData =", googleUser)
        
        result = lookUser.get()
        
        if result:
            self.redirect('/')
        else:
            lookUser = User.all()
            lookUser.filter("nickname =", nickname)
            result = lookUser.get()
            
            if result is not None:
                message = "you should try another one"
                
                template_dict = {
                                 'message'  : message,
                                 }
        
                path = os.path.join(os.path.dirname(__file__), "pages/newUserTemplate.html")
                self.response.out.write(template.render(path, template_dict))
                
            else:
                user = User()
                user.userData = googleUser
                user.nickname = nickname
                user.put()
                
                self.redirect('/')
                
                