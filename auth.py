from flask import Blueprint
from flask_restful import Api,Resource,reqparse #wworks with principle of jwt


auth_bp= Blueprint('auth_bp',__name__,url_prefix='/auth')
auth_api=Api(auth_bp)