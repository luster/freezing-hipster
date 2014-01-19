import json
import urllib2
import urllib
import jinja2
import os
import time

from google.appengine.ext import ndb
from google.appengine.api import users

from lib.Social import Social
from lib.Social.Token.Token import Token
from lib.Social.Instagram.model import InstagramPost

class Instagram(Social):

    """Extended class for Instagram API Auth and content fetch and store."""

    def authenticate(self, code='', token=''):

        token_key = ndb.Key('Tokens', 'Instagram_Token')
        user = users.get_current_user()
        token_query = Token.query(
            ancestor=token_key)
        #TODO: query the current user's token specifically in case of multiple feeds
        token = token_query.fetch(1)
        token = token[0]

        if code and not token:
            params = {
                    'client_id': self.api['client_id'],
                    'client_secret': self.api['client_secret'],
                    'grant_type': 'authorization_code',
                    'redirect_uri': self.api['redirect_uri']+'?sn=Instagram',
                    'code': code
                    }
            token_request = urllib2.Request(self.api['token_url'], urllib.urlencode(params))
            token_response = urllib2.urlopen(token_request).read()
            token_json = json.loads(token_response)

            # store in datastore and return (need token datastore key or something)
            token = Token(token=token_json['access_token'],
                          sn='Instagram',
                          user_id=token_json['user']['id'],
                          username=token_json['user']['username'],
                          full_name=token_json['user']['full_name'],
                          profile_picture=token_json['user']['profile_picture'],
                          user=user,
                          parent=token_key
                          )
            token.put()
            self.token = token

        elif token:
            self.token = token
        else:
            print 'Error'


    def fetch(self, timestamp=False, tag=''):

        post_key = ndb.Key('Posts','Instagram_Post')
        user = users.get_current_user()
        posts_query = InstagramPost.query(
            ancestor=post_key)
        last_post = posts_query.order(-InstagramPost.created_time).fetch(1)
        last_post = last_post[0]

        if not last_post:
            timestamp = '0'
        else:
            timestamp = str(int(last_post.created_time)+1)

        self.api['endpoint'] = self.api['endpoint'].replace('%%USER_ID%%',self.token.user_id)
        self.api['endpoint'] = self.api['endpoint'].replace('%%ACCESS_TOKEN%%',self.token.token)

        time_param = '&min_timestamp=%%MIN_TIMESTAMP%%'.replace('%%MIN_TIMESTAMP%%',timestamp)
        count_param = '&count=1'

        endpoint = self.api['endpoint'] + time_param
        content_response = urllib2.urlopen(endpoint).read()
        content = json.loads(content_response)

        older_content = content
        while older_content['pagination']:
            older_response = urllib2.urlopen(older_content['pagination']['next_url']).read()
            older_content = json.loads(older_response)
            content['data'].extend(post for post in older_content['data'])

        for post in content['data']:
            instaPost = InstagramPost(
                    username=self.token.username,
                    picture_URL=post['images']['standard_resolution']['url'],
                    video_URL=post['videos']['standard_resolution']['url'] if 'videos' in post else None,
                    created_time=post['created_time'],
                    caption_text=post['caption']['text'],
                    parent=post_key
                    )
            instaPost.put()


    def store(self, data):
        pass
