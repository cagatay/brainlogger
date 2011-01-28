'''
Created on Aug 20, 2010
 
@author: cagatay.yuksel
'''

from google.appengine.ext import db

class Title(db.Model):
    name = db.StringProperty()

class Entry(db.Model):
    title = db.ReferenceProperty(Title, collection_name="entries")
    author = db.UserProperty(auto_current_user_add = True)
    content = db.TextProperty()
    rating = db.IntegerProperty(default=0)
    
    dateAdded = db.DateTimeProperty(required=True, auto_now_add=True)

class TitleSerializable:
    title = None
    entry = None
    
    def __init__(self, data, name):
        title = name
        
        if(data != None):
            entry = data.fetch(10)