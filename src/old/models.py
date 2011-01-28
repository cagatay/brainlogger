#===============================================================================
# Created on Aug 20, 2010
# 
# @author: cagatay.yuksel
#===============================================================================

from google.appengine.ext import db

class userModel(db.Model):
    
    nickname = db.StringProperty()
    userData = db.UserProperty()
    likes = db.ListProperty(db.Key)
    dislikes = db.ListProperty(db.Key)
    favourties = db.ListProperty(db.Key)

class titleModel(db.Model):
    
    title = db.StringProperty()
    tags = db.StringListProperty()

class entryModel(db.Model):
    
    author = db.ReferenceProperty(userModel)
    title = db.ReferenceProperty(titleModel)
    content = db.TextProperty()
    tags = db.StringListProperty()
    likes = db.IntegerProperty(default=0)
    dislikes = db.IntegerProperty(default=0)
    
    dateAdded = db.DateTimeProperty(required=True, auto_now_add=True)
    dateModified = db.DateTimeProperty()

