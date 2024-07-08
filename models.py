from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    _tablename_ = 'user'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String, nullable= False)
    email = db.Column(db.String, nullable= False)
    password = db.Column(db.String, nullable= False)
    events=db.relationship('Event',back_populates='users')
    bookings=db.relationship('Booking',back_populates='users')
    reviews=db.relationship('Reviews',back_populates='users')

class Event(db.Model):
    tablename='events'
    id= db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    description=db.Column(db.String,nullable=False)
    price=db.Column(db.Float,nullable=False)
    date=db.Column(db.DateTime)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    organiser=db.relationship('User',back_populates='events')
    bookings=db.relationship('Booking',back_populates='events')
   

class Booking(db.Model):
    tablename='bookings'
    id= db.Column(db.Integer,primary_key=True)
    event_id=db.Column(db.String,db.ForeignKey('event.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    organiser=db.relationship('Event',back_populates='bookings')
    user=db.relationship('User',back_populates='bookings')

class Reviews(db.Model):
    tablename='reviews'
    id= db.Column(db.Integer,primary_key=True)
    event_id = db.Column(db.Integer,db.ForeignKey('event.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User',back_populates='reviews')
    event = db.relationship('User',back_populates='reviews')