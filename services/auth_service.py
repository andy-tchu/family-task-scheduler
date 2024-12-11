from flask import request
import logging
from flask_jwt_extended import decode_token, exceptions, verify_jwt_in_request
from controllers.user_controller import get_user_by_username

def auth_routes():
    try:
        token = request.cookies.get("Authorized")
        if not token:
            return {"error": "Token not found"}, 403

        decoded_token = decode_token(token)
        identity = decoded_token.get("sub")

        if not identity:
            return {"error": "Invalid token"}, 403
        
        if not get_user_by_username(identity):
            return {"error": "Invalid token"}, 403
        
        return True
    
    except Exception as e:
        return {"JWT error": str(e)}, 403
    
def require_jwt_token():
    """
    Middleware to ensure restricting access to routes
    """
    logging.info(f"End point: {request.endpoint}")
    public_endpoints = ['auth.login_bp', 'auth.signup_user_bp', 'catch_all', 'index']
    
    if request.endpoint in public_endpoints:
        return None
    
    try:
        result = auth_routes()
        if result is not True:
            return result
        
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return {"error": "An error occurred while accessing routes"}, 500
        