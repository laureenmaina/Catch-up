from flask import Flask
from flask_migrate import Migrate
from models import db

from attendee import attendee_bp
from organiser import organiser_bp
from auth import auth_bp


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
migrate = Migrate(app=app, db=db)
app.register_blueprint(attendee_bp)
app.register_blueprint(organiser_bp)
app.register_blueprint(auth_bp)
db.init_app(app)



@app.route('/event')
def home():
    return {"message":"event"}
