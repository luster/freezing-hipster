from google.appengine.ext import ndb

class InstagramPost(ndb.Model):
    """Models an instagram post."""

    user = ndb.UserProperty()
    username = ndb.StringProperty()
    #picture = ndb.BlobProperty(default=None)
    picture_URL = ndb.StringProperty()
    #video = ndb.BlobProperty(default=None)
    video_URL = ndb.StringProperty()
    created_time = ndb.StringProperty()
    caption_text = ndb.StringProperty()
