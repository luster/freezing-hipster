import webapp2
import json
from lib.Social import Social
from google.appengine.api import users
from google.appengine.ext import ndb
from admin import Admin
from callback import Callback

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write('HOMEPAGE')

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/callback', Callback),
    ('/admin', Admin),
], debug=True)
