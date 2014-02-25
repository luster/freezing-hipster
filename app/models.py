from app import db
import datetime

ROLE_USER = 0
ROLE_ADMIN = 1

# Comment Form Model
# TODO: have form send an email
class CommentForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)
    created_on = db.Column(db.DateTime, default=db.func.now())
    email = db.Column(db.String(254))
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    phone = db.Column(db.String(50))

# Show Date Model
class ShowDate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime)
    city = db.Column(db.String(120))
    venue = db.Column(db.String(120))

    def __init__(self, date_time, city, venue):
        self.date_time = date_time
        self.city = city
        self.venue = venue

    def __repr__(self):
        date = self.date_time.strftime('%B %d').replace(' 0',' ')
        return '<ShowDate %s @ %r>' % (date, self.venue)

# TODO: Merch Modeling - keep track of merch sold at show dates
