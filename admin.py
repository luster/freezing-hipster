import webapp2
import urllib2

from lib.Social import Social
from conf import apis, conf

from google.appengine.api import users, urlfetch
from google.appengine.ext import ndb

class Admin(webapp2.RequestHandler):

    def get(self):

        user = users.get_current_user()

        if users.is_current_user_admin():
            self.response.write('Hello, ' + user.nickname()+'<br><br>')
            self.response.write('<a href="%s">Instagram Auth</a>'%(apis['Instagram']['auth_url']))
        elif user:
            self.redirect('http://127.0.0.1:8080')
        else:
            self.redirect(users.create_login_url(self.request.uri))


