import webapp2
import json
import jinja2
import os

from lib.Social import Social
from lib.shows.controller import TourDateController
from google.appengine.api import users
from google.appengine.ext import ndb
from callback import Callback

PROJECT_DIR = os.path.dirname(__file__)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class CommentForm(ndb.Model):

    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    email = ndb.StringProperty()
    phone = ndb.StringProperty()
    comment = ndb.TextProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)

class Comment(webapp2.RequestHandler):

    def get(self):

        c = CommentForm()
        c.first_name = self.request.get('firstName')
        c.last_name = self.request.get('lastName')
        c.email = self.request.get('email')
        c.phone = self.request.get('phone')
        c.comment = self.request.get('comments')

        c.put()

        self.redirect('/')

class MainPage(webapp2.RequestHandler):

    def get(self):
        tour_controller = TourDateController()

        merch_img_path = PROJECT_DIR+'/Merch'
        paths = './static/img/Assets/Merch/'
        merch_img = [
                {
                    'href':paths+f,
                    'alt': f.replace('_',' ').replace('.jpg','')
                } for f in os.listdir(merch_img_path)]
        merch_img = sorted(merch_img, key=lambda k: k['alt'])

        template_values = {
                "top_nav": [
                    {
                        "url": "#music",
                        "text": "music"
                        },
                    {
                        "url": "#tour",
                        "text": "tour"
                        },
                    {
                        "url": "#shop",
                        "text": "shop"
                        },
                    {
                        "url": "#contact",
                        "text": "contact"
                        }],
                    "show_dates": tour_controller.shows,
                    "merch": merch_img
                }
        template = JINJA_ENVIRONMENT.get_template('./templates/base.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/callback', Callback),
    ('/submit', Comment), 
], debug=True)
