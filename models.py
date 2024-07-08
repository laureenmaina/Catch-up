from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model, SerializerMixin):
    _tablename_ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String, nullable= False)
    email = db.Column(db.String, nullable= False)
    password = db.Column(db.String, nullable= False)
    events=db.relationship('Event',back_populates='users')
    bookings=db.relationship('Booking',back_populates='users')
    reviews=db.relationship('Reviews',back_populates='users')

    serialize_rules=('-bookings.users','reviews.users',)

class Event(db.Model, SerializerMixin):
    tablename='events'
    id= db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    description=db.Column(db.String,nullable=False)
    price=db.Column(db.Float,nullable=False)
    date=db.Column(db.DateTime)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    organiser=db.relationship('User',back_populates='events')
    bookings=db.relationship('Booking',back_populates='events')

    serialize_rules=('-organiser.events','-bookings.events')
   

class Booking(db.Model, SerializerMixin):
    tablename='bookings'
    id= db.Column(db.Integer,primary_key=True)
    event_id=db.Column(db.String,db.ForeignKey('event.id'))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    organiser=db.relationship('Event',back_populates='bookings')
    user=db.relationship('User',back_populates='bookings')

    serialize_rules=('')

class Reviews(db.Model, SerializerMixin):
    tablename='reviews'
    id= db.Column(db.Integer,primary_key=True)
    event_id = db.Column(db.Integer,db.ForeignKey('event.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    user = db.relationship('User',back_populates='reviews')
    event = db.relationship('User',back_populates='reviews')