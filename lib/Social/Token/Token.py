from google.appengine.ext import ndb
from google.appengine.api import users

class Token(ndb.Expando):

    token = ndb.StringProperty()
    sn = ndb.StringProperty()
    user = ndb.UserProperty()
