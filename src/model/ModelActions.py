'''
Created on Oct 19, 2010

@author: cagatay.yuksel
'''

from Models import *

def getByTitle(title):
    t = Title.all()
    t.filter("name=", title)
    result = t.get()
    result = TitleSerializable(result, title)
    return result

def putEntry(title, content):
    t = Title.all()
    t.filter("name=", title)
    result = t.get()
    
    if(result == None):
        result = Title(name=title)
        result.put()
    
    entry = Entry()
    entry.title = result
    entry.content = content
    entry.put()
    return

def downVote(entryKey):
    def txn(key):
        entry = db.get(key)
        entry.rating -= 1
        entry.put()
        return entry.rating
    return db.run_in_transaction(txn, entryKey)

def upVote(entryKey):
    def txn(key):
        entry = db.get(key)
        entry.rating += 1
        entry.put()
        return entry.rating
    return db.run_in_transaction(txn, entryKey)