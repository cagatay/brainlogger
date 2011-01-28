'''
Created on Aug 13, 2010

@author: cagatay.yuksel
'''

from Entry import Entry
from django.utils import simplejson
from google.appengine.api import users
from google.appengine.ext import webapp

class Request(webapp.RequestHandler):
    """ Allows the functions defined in the RPCMethods class to be RPCed."""
    def __init__(self):
        webapp.RequestHandler.__init__(self)
        self.methods = RPCMethods()

    def post(self):
        args = simplejson.loads(self.request.body)
        func, args = args[0], args[1:]

        if func[0] == '_':
            self.error(403) # access denied
            return

        func = getattr(self.methods, func, None)
        if not func:
            self.error(404) # file not found
            return

        result = func(*args)
        self.response.out.write(result)

class RPCMethods:
    """ Defines the methods that can be RPCed.
    NOTE: Do not allow remote callers access to private/protected "_*" methods.
    """

    def dislikeEntry(self, *args):
        #user = users.get_current_user()
        
        entry = Entry().get_by_id(int(args[0]))
        entry.dislikes += 1
        result = entry.dislikes
        entry.put()
        
        return "document.getElementById('" + str(args[0]) + "d').innerHTML = '" + str(result) + "';"
    def editEntry(self, *args):
        entry = Entry().get_by_id(long(args[0]))
        user = users.get_current_user()
        
        if entry.author == user:
            entry.content = args[1]
            entry.put()
            return "ok"

        
        