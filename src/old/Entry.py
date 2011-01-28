'''
Created on 5 Aug 2010

@author: cagatay
'''

from google.appengine.ext import db

class Entry(db.Model):
    author = db.UserProperty(required=True, auto_current_user_add=True)
    authorNickname = db.StringProperty()
    title = db.StringProperty()
    content = db.TextProperty()
    tags = db.StringListProperty()
    likes = db.IntegerProperty(default=0)
    dislikes = db.IntegerProperty(default=0)
    
    dateAdded = db.DateTimeProperty(required=True, auto_now_add=True)
    dateModified = db.DateTimeProperty(auto_now=True, auto_now_add=True)