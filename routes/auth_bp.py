from flask import Blueprint, request
from controllers.auth_controller import login_user, signup_user, logout_user
from models import UserSchema
from marshmallow import ValidationError
import logging


user_schema = UserSchema()

# Create a blueprint for authenthication
auth_bp = Blueprint('auth', __name__, url_prefix="/")

@auth_bp.route("signup", methods=['POST'])
def signup_user_bp():   
    try:
        data = request.get_json()
        if not data:
            return "User data not found", 400
        
        validated_user = user_schema.load(data)
        user = signup_user(validated_user)
        return user
    
    except ValidationError as ve:
        logging.error(str(ve))
        return "Error validating a user", 400
    except Exception as e:
        logging.error(str(e))
        return "User signup error", 500      

@auth_bp.route("login", methods=['POST'])
def login_bp():   
    try:
        data = request.get_json()
        if not data:
            return "Login data not found", 400
        
        return login_user(data)
    
    except Exception as e:
        logging.error(str(e))
        return "User login error", 500
    
@auth_bp.route("logout", methods=['POST'])
def logout_bp():
    try:
        data = request.get_json()
        if not data:
            return "Logout data not found", 400
        
        return logout_user(data)
    
    except Exception as e:
        logging.error(str(e))
        return "User logout error", 500