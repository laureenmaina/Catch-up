from flask import Blueprint
from flask_restful import Api,Resource,reqparse #wworks with principle of jwt


organiser_bp= Blueprint('organiser_bp',__name__,url_prefix='/organiser')
