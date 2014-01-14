import webapp2
import json
import urllib2
import urllib
import jinja2
import os

from google.appengine.ext import ndb
from google.appengine.api import users

from lib.Social import Social
from conf import apis, conf

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def social_media_key(social_media_name):

    """Constructs a datastore key for a Social entry"""

    return ndb.Key('Social_Media', social_name)

class Callback(webapp2.RequestHandler):

    """Gets auth code through redirect if no access token available.
    Stores/retrieves access token and fetches/stores API data."""

    def get(self):

        code = self.request.get('code')
        sn = self.request.get('sn')

        token_url = apis[sn]['token_url']

        if sn == 'Instagram':
            params = {
                    'client_id': apis[sn]['client_id'],
                    'client_secret': apis[sn]['client_secret'],
                    'grant_type': 'authorization_code',
                    'redirect_uri': conf['redirect']+'?sn=Instagram',
                    'code': code
                    }
            token_request = urllib2.Request(token_url, urllib.urlencode(params))
            token_response = urllib2.urlopen(token_request).read()
            token = json.loads(token_response)

            access_token = token['access_token']
            user_id = token['user']['id']
            username = token['user']['username']

            apis[sn]['endpoint'] = apis[sn]['endpoint'].replace('%%USER_ID%%',user_id)
            apis[sn]['endpoint'] = apis[sn]['endpoint'].replace('%%ACCESS_TOKEN%%',access_token)

            # time_param = '&min_timestamp=%%MIN_TIMESTAMP%%'
            count_param = '&count=20'

            endpoint = apis[sn]['endpoint'] + count_param
            content_response = urllib2.urlopen(endpoint).read()
            content = json.loads(content_response)

            # do stuff with content
            posts = list()
            videos = dict()
            images = dict()
            captions = dict()
            for post in content['data']:
                posts.append({
                    'video': post['videos']['standard_resolution']['url'] if 'videos' in post else None,
                    'image': post['images']['standard_resolution']['url'],
                    'caption': post['caption']['text']
                    })

            template_values = {
                    'posts': posts
                    }
            template = JINJA_ENVIRONMENT.get_template('./templates/instagram.html')
            self.response.write(template.render(template_values))

            # self.response.write(json.dumps(content))
