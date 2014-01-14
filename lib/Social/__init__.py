class Social:

    """Class for social auth and content fetch."""

    def __init__(self, api):
        self.sn = api['name']
        self.api = api

    def authenticate(self):
        pass

    def get_content(self, tag=''):
        if self.sn == 'Instagram':
            return 


class FetchInstagram:

    # initialize with a particular user -> get their access token from datastore
    def __init__(self, social_user, config):
        pass

    def fetch_data(self, response):
        pass

        # get first API response w/ 1 post - first post is most recent

        # if response['data']['created_time'] not equal to most recent post in datastore
            # get posts in between these two times
            # min_timestamp is timestamp from most recent post
            # while response['pagination']['next_url']
                # go to next url and save data
                # image model
                # check for video


