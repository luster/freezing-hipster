from google.appengine.ext import ndb

from datetime import datetime

class TourDate(ndb.Model):
    """Models a show date."""

    date_time = ndb.DateTimeProperty()
    city = ndb.StringProperty()
    venue = ndb.StringProperty()

