'''
Created on 6 Aug 2010

@author: cagatay
'''

from google.appengine.ext import webapp
from google.appengine.api import users
from Entry import Entry
import string

class Post(webapp.RequestHandler):

    def post(self):
        user = users.get_current_user()
        
        if user:
            entry = Entry()
            entry.title = self.request.get('title')
            entry.content = self.request.get('content')
            entry.tags = string.split(self.request.get('tags'),',')
            entry.put()
            self.redirect('/show?q=' + entry.title)
        else:
            self.redirect('/')
        
            