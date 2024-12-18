from controllers.user_controller import create_user, get_user_by_username
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, JWTManager
from flask import make_response, abort
import logging


def signup_user(user):
    try:
        # Hash the password
        user['password'] = generate_password_hash(user['password'])
        new_user = create_user(user)
        return new_user

    except Exception as e:
        logging.error(str(e))
        abort(500) 
       
def login_user(data):
    try:
        username = data.get("username")
        password = data.get("password")
        
        if not username:
            logging.warning("Username not provided")
            return {"error": "Username is required"}, 400
        
        if not password:
            logging.warning("Password not provided")
            return {"error": "Password is required"}, 400

        # Fetch user from the database
        user = get_user_by_username(username)
        if not user:
            logging.warning(f"User not found: {username}")
            return {"error": "User not found"}, 404
        
        # Check password
        if not check_password_hash(user["password"], password):
            logging.warning(f"Invalid password for user: {username}")
            return {"error": "Invalid credentials"}, 401

        # Create JWT token
        token = create_access_token(identity=username)
        
        # Create a response and set the token in a cookie
        response = make_response({"message": "User logged in"}, 200)
        response.set_cookie("Authorized", token, httponly=True, secure=False)
        return response

    except Exception as e:
        logging.error(str(e))
        abort(500)
    
def logout_user(data):
    try:
        username = data.get("username")
        
        if not username:
            logging.warning("Username not provided")
            return {"error": "Username is required"}, 400
        
        # Fetch user from the database
        user = get_user_by_username(username)
        if not user:
            logging.warning(f"User not found: {username}")
            return {"error": "User not found"}, 404
        
        # Create a response and set the token in a cookie
        response = make_response({"message":"User logged out"}, 200)
        response.delete_cookie("Authorized")
        return response

    except Exception as e:
        logging.error(str(e))
        abort(500)