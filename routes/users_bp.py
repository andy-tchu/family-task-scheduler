from flask import Blueprint, request, abort
from models import UserSchema
from marshmallow import ValidationError
from controllers.user_controller import get_user_by_username, create_user, get_all_users
# from controllers.authentication import login_user, register_user
import logging

user_schema = UserSchema()

# Create a blueprint for users CRUD
users_bp = Blueprint('users', __name__, url_prefix="/users")

@users_bp.route("", methods=['GET'])
def get_users_bp():
    try:
        users = get_all_users()
        if users:
            return users, 200
        return "Users not found", 404
    except Exception as e:
        logging.error(str(e))
        return "Error finding users", 500
    
    
@users_bp.route("", methods=['POST'])
def create_user_bp():   
    try:
        data = request.get_json()
        if not data:
            return "User data not found", 400
        validated_user = user_schema.load(data)
        if not validated_user:
            return "User data not correct", 400
        user = create_user(validated_user)
        
        return user
    except Exception as e:
        logging.error(str(e))
        return "Error creating user", 500      
        
@users_bp.route("<string:name>", methods=['GET'])
def get_user_bp(name):
    try:
        user = get_user_by_username(name)
        if user:
            return (user, 200)
        return "User not found", 404
    except Exception as e:
        logging.error(str(e))
        return "Error finding user", 500

@users_bp.route("<int:id>", methods=['PUT'])
def update_user_bp(id):
    return "NOT YET"
    
@users_bp.route("<int:id>", methods=['DELETE'])
def delete_user_bp(id):
    return "NOT YET"

@users_bp.route("login", methods=['POST'])
def login():   
    try:
        data = request.get_json()
        if not data:
            return "Login data not found", 400
        return login_user(data)
    except Exception as e:
        logging.error(str(e))
        return "Error finding user", 500      