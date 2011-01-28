'''
Created on Aug 12, 2010

@author: cagatay.yuksel
'''

import os
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template
from Entry import Entry

class Show(webapp.RequestHandler):
    def get(self):
        ENTRIES_PER_PAGE = 10
        
        query = self.request.get("q")
        page = self.request.get("p")
        
        if page == '':
            page = 1
        else:
            page = int(page)
            
        previous = page - 1    
        next = page + 1
        
        if query:
            
            results = []
            user = users.get_current_user()
        
            if user:
                loglink = users.create_logout_url(self.request.uri)
                logtext = "logout"
            else:
                loglink = "/login?return=" + self.request.uri
                logtext = "login"
        
            
            search = Entry.all();
            search.filter("title =", query)
            search.order('-dateModified')
            results = search.fetch(ENTRIES_PER_PAGE + 1, (page - 1)*ENTRIES_PER_PAGE)
            
            if len(results) < ENTRIES_PER_PAGE + 1:
                next = 0
            else:
                results.pop()
            
            template_dict = {
                        'logtext'       : logtext,
                        'loglink'       : loglink,
                        'entries'       : results,
                        'user'          : user,
                        'query'         : query,
                        'page'          : page,
                        'previous'      : previous,
                        'next'          : next,
                        }
            
            path = os.path.join(os.path.dirname(__file__), "pages/showTemplate.html")
            self.response.out.write(template.render(path, template_dict))
                
        else:
            self.redirect("/")
        
        