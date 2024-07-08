from flask import Blueprint
from flask_restful import Api,Resource,reqparse #wworks with principle of jwt


attendee_bp= Blueprint('attendee_bp',__name__,url_prefix='/attendee')
