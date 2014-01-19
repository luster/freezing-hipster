import webapp2
import json
import urllib2
import urllib
import jinja2
import os

from google.appengine.ext import ndb
from google.appengine.api import users

# from lib.Social import Social
from lib.Social.Instagram.controller import Instagram
from conf import apis, conf

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Callback(webapp2.RequestHandler):

    """Gets auth code through redirect if no access token available.
    Stores/retrieves access token and fetches/stores API data."""

    def get(self):

        code = self.request.get('code')
        sn = self.request.get('sn')

        if sn == 'Instagram':
            client = Instagram(apis[sn])
            client.authenticate(code)
            client.fetch()

            # posts = []

            # template_values = {
            #         'posts': posts
            #         }
            # template = JINJA_ENVIRONMENT.get_template('./templates/instagram.html')
            # self.response.write(template.render(template_values))

            # self.response.write(json.dumps(content))
