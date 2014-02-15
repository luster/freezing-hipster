import json
from datetime import datetime
import datetime as dt2

from google.appengine.ext import ndb

from lib.shows.model import TourDate

class TourDateController(object):

    def __init__(self):

        shows = self.query_shows()
        self.shows = self.format_shows(shows)

    def add_show(self, dt, venue, city):

        new_show = TourDate(
                date_time=dt,
                venue=venue,
                city=city)
        new_show.put()

    def format_show(self, tour_date):

        time = tour_date.date_time.strftime(' %I:%M %p').replace(' 0','').lower().replace(' ','')
        date = tour_date.date_time.strftime('%B %d').replace(' 0',' ')

        string_show = {
                'time': time,
                'date': date,
                'venue': tour_date.venue,
                'city': tour_date.city
                }

        return string_show

    def query_shows(self):

        qry = TourDate.query(TourDate.date_time > datetime.today()-dt2.timedelta(4))

        return qry.order(TourDate.date_time).fetch(3)

    def format_shows(self, tour_dates):
        string_shows = []

        for tour_date in tour_dates:
            string_shows.append(self.format_show(tour_date))

        return string_shows
