from models import *
from sqlalchemy.sql import text
import urllib2
import json
from datetime import datetime

class CommentFormController:

    def __init__(self):
        pass

class ShowDateController:

    def __init__(self):
        pass

    def new_show(self, date_time, city, venue):
        a = ShowDate(date_time=date_time,
                city=city,
                venue=venue)

        db.session.add(a)
        db.session.commit()

    def update_show(self, show_date, *args):
        """Update show_date record. args should be (attr1,update_val1), ..."""

        for a in args:
            setattr(show_date, args[0], args[1])

        db.session.commit()

    def query_shows(self, limit=4):

        shows = []

        shows_qry = ShowDate.query.order_by('date_time desc').limit(limit)
        shows_qry = shows_qry[:limit]

        for show in shows_qry:
            time = show.date_time.strftime(' %I:%M %p').replace(' 0','').lower().replace(' ','')
            date = show.date_time.strftime('%B %d').replace(' 0',' ')
            shows.append({
                'time': time,
                'date': date,
                'venue': show.venue,
                'city': show.city
                })

        return shows

class BandsInTownController:

    def __init__(self):
        pass

    def query_shows(self):
        url = 'http://api.bandsintown.com/artists/Time%20King/events.json?api_version=2.0&app_id=tk-site'
        shows = []

        try:
            res = urllib2.urlopen(url).read()
            data = json.loads(res)
            for show in data:
                dt = datetime.strptime(show['datetime'],'%Y-%m-%dT%H:%M:%S')
                time = dt.strftime(' %I:%M %p').replace(' 0','').lower().replace(' ','')
                date = dt.strftime('%B %d').replace(' 0',' ')

                venue = show['venue']['name']
                city = show['venue']['city'] + ', ' + show['venue']['region']

                shows.append({
                            'time': time,
                            'date': date,
                            'venue': venue,
                            'city': city
                            })

            return shows

        except:
            return []



class MerchController:

    def __init__(self):
        pass
