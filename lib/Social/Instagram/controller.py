import json
import urllib2
import urllib
import jinja2
import os
import time
import sys

from google.appengine.ext import ndb
from google.appengine.api import users

from lib.Social import Social
from lib.Social.Token.Token import Token
from lib.Social.Instagram.model import InstagramPost

for attr in ('stdin', 'stdout', 'stderr'):
    setattr(sys, attr, getattr(sys, '__%s__' % attr))

import pdb

class Instagram(Social):

    """Extended class for Instagram API Auth and content fetch and store."""

    def __init__(self, current_user):
        pass

    def authenticate(self, code='', token=''):
        #TODO: if GAE user has token, set token (__init__ ?)
        # else, redirect to instagram auth dialog
        current_user = users.get_current_user()
        pdb.set_trace()

        token_key = ndb.Key('Tokens', 'Instagram_Token')
        token_query = Token.query(ancestor=token_key)
        #TODO: query the current user's token specifically in case of multiple feeds
        token = token_query.filter(Token.user==current_user).fetch(1)

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
                          user=current_user,
                          parent=token_key
                          )
            token.put()
            self.token = token

        elif token:
            token = token[0]
            self.token = token
        else:
            print 'Error'


    def fetch(self, timestamp=False, tag=''):

        current_user = users.get_current_user()

        post_key = ndb.Key('Posts','Instagram_Post')
        posts_query = InstagramPost.query(
            ancestor=post_key).filter(InstagramPost.user==current_user)
        last_post = posts_query.order(-InstagramPost.created_time).fetch(1)

        if not last_post:
            timestamp = '0'
        else:
            last_post = last_post[0]
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
                    user=current_user,
                    username=self.token.username,
                    picture_URL=post['images']['standard_resolution']['url'],
                    video_URL=post['videos']['standard_resolution']['url'] if 'videos' in post else None,
                    created_time=post['created_time'],
                    caption_text=post['caption']['text'] if post['caption'] else '',
                    parent=post_key
                    )
            instaPost.put()


    def store(self, data):
        pass
