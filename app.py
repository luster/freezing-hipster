import webapp2
import json

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.write('Hello, World! Fuck you')

class Callback(webapp2.RequestHandler):

    def load_conf(self):
        apis_file = open('./conf/apis.json','r')
        self.apis = json.loads(apis_file.read())

    def get(self):
        self.load_conf()

        self.response.write('CALLBACK!<br><br>')
        code = self.request.get('code')
        self.response.write('Code: '+code+'<br><br>')
        self.response.write(self.apis)

class Admin(webapp2.RequestHandler):

    def get(self):
        self.response.write('ADMIN COMING SOON!')


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/callback', Callback),
    ('/admin', Admin),
], debug=True)
