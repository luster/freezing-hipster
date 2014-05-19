from models import *
import urllib2
import json
from datetime import datetime

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



#TODO: interface merch store API with merch img gallery
class MerchController:

    def __init__(self):
        pass

#TODO: make the comment form submit to email or something
class CommentFormController:

    def __init__(self):
        pass

