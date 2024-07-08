from flask import Blueprint
from flask_restful import Api,Resource,reqparse #wworks with principle of jwt


organise_bp= Blueprint('organise_bp',__name__,url_prefix='/organise')
