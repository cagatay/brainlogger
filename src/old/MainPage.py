'''
Created on 31 Jul 2010

@author: cagatay
'''

import os
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template
from Entry import Entry

class MainPage(webapp.RequestHandler):
    def get(self):
        ENTRIES_PER_PAGE = 10;
        
        user = users.GetCurrentUser()
        page = self.request.get('p')
        
        if page == '':
            page = 1
        else:
            page = int(page)
        previous = page -1
        next = page + 1
        
        logtext = ""
        loglink = ""
        
        if user:
            loglink = users.create_logout_url(self.request.uri)
            logtext = "logout"
        else:
            loglink = "/login?return=" + self.request.uri
            logtext = "login"
        
        searchEntries = Entry.all()
        searchEntries.order('-dateModified')
        results = searchEntries.fetch(ENTRIES_PER_PAGE, (page - 1)*ENTRIES_PER_PAGE)
        
        if len(results) < ENTRIES_PER_PAGE + 1:
            next = 0
        else:
            results.pop()
        
        template_dict = {
                        'logtext'   : logtext,
                        'loglink'   : loglink,
                        'entries'   : results,
                        'user'      : user,
                        'page'      : page,
                        'previous'  : previous,
                        'next'      : next,
                        }
        
        path = os.path.join(os.path.dirname(__file__), "pages/mainTemplate.html")
        self.response.out.write(template.render(path, template_dict))