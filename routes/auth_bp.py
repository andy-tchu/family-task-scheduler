from flask import Blueprint, request, abort
from controllers.user_controller import get_user, create_user, get_all_users
from controllers.auth_controller import login_user, signup_user, logout_user
import logging


# Create a blueprint for authenthication
auth_bp = Blueprint('auth', __name__, url_prefix="/")

@auth_bp.route("signup", methods=['POST'])
def signup_user_bp():   
    try:
        data = request.get_json()
        if not data:
            return "User data not found", 400
        user = signup_user(data)
        
        return user
    
    except Exception as e:
        logging.error(str(e))
        return "Signup user error", 500      

@auth_bp.route("login", methods=['POST'])
def login_bp():   
    try:
        data = request.get_json()
        if not data:
            return "Login data not found", 400
        
        return login_user(data)
    
    except Exception as e:
        logging.error(str(e))
        return "Login user error", 500
    
@auth_bp.route("logout", methods=['POST'])
def logout_bp():
    try:
        data = request.get_json()
        if not data:
            return "Logout data not found", 400
        
        return logout_user(data)
    
    except Exception as e:
        logging.error(f"Logout error: {str(e)}", exc_info=True)
        return "Logout user error", 500