class Social(object):

    """Base class for social auth and content fetch and store."""

    def __init__(self, api):
        self.api = api

    def authenticate(self):
        # try to get access token, store and return
        # if access token not in datastore
            # redirect and authenticate user
            # get access token
            # store token in data store w/ user info

        raise NotImplementedError

    def fetch(self, timestamp=False, tag=''):
        # if timestamp flag is true
            # grab most recent post timestamp
            # query post range from after timestamp
        # else
            # grab all posts

        # store new posts in datastore

        raise NotImplementedError

    def store(self, data):
        # get datastore key for right datatype (socialuser or post)

        # store post
        raise NotImplementedError



