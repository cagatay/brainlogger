'''
Created on Aug 13, 2010

@author: cagatay.yuksel
'''

from google.appengine.ext import db

class User(db.Model):
    
    userData = db.UserProperty()
    nickname = db.StringProperty()
    likes = db.ListProperty(db.Key)
    dislikes = db.ListProperty(db.Key)
    favourties = db.ListProperty(db.Key)
