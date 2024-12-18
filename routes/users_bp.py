from flask import Blueprint, request
from models import UserSchema, UserUpdateSchema
from marshmallow import ValidationError
from controllers.user_controller import create_user, get_user, update_user, delete_user, get_all_users
import logging


user_schema = UserSchema()
user_update_schema = UserUpdateSchema()

# Create a blueprint for users CRUD
users_bp = Blueprint('users', __name__, url_prefix="/users")

@users_bp.route("", methods=['POST'])
def create_user_bp():   
    try:
        data = request.get_json()
        if not data:
            return "User data not found", 400
        
        validated_user = user_schema.load(data)
        response = create_user(validated_user)
        return response
    
    except ValidationError as ve:
        logging.error(str(ve))
        return "Error validating a user", 400
    except Exception as e:
        logging.error(str(e))
        return "Error creating a user", 500      
        
@users_bp.route("<string:id>", methods=['GET'])
def get_user_bp(id):
    try:
        user = get_user(id)
        if not user:
            return "User not found", 404
        
        return user, 200
        
    except Exception as e:
        logging.error(str(e))
        return "Error finding a user", 500

@users_bp.route("<string:id>", methods=['PUT'])
def update_user_bp(id):
    try:
        user = get_user(id)
        if not user:
            return "User not found", 404
        
        data = request.get_json()
        if not data:
            return "User data not found", 400
        
        validated_user = user_update_schema.load(data)
        response = update_user(id, validated_user)
        return response, 200
    
    except ValidationError as ve:
        logging.error(str(ve))
        return "Error validating a user", 400
    except Exception as e:
        logging.error(str(e))
        return "Error updating a user", 500
    
@users_bp.route("<string:id>", methods=['DELETE'])
def delete_user_bp(id):
    try:
        user = get_user(id)
        if not user:
            return "User not found", 404
        
        response = delete_user(id)
        return response, 200
    
    except Exception as e:
        logging.error(str(e))
        return "Error deleting a user", 500  

@users_bp.route("", methods=['GET'])
def get_all_users_bp():
    try:
        users = get_all_users()
        if not users:
            return "Users not found", 404
            
        return users, 200
    
    except Exception as e:
        logging.error(str(e))
        return "Error finding users", 500