from google.appengine.ext import ndb
from google.appengine.api import users

class SocialUser(ndb.Model):

    user = ndb.UserProperty(required=True)
    social_network = ndb.StringProperty(required=True)
    account_id = ndb.StringProperty(required=True)
    account_username = ndb.StringProperty()
    token = ndb.StringProperty(required=True)
