from flask import Blueprint, request
from models import FamilySchema
from marshmallow import ValidationError
from controllers.family_controller import create_family, get_family, update_family, delete_family, get_all_families
import logging


family_schema = FamilySchema()

# Create a blueprint for families CRUD
families_bp = Blueprint('families', __name__, url_prefix="/families")
   
@families_bp.route("", methods=['POST'])
def create_family_bp():   
    try:
        data = request.get_json()
        if not data:
            return "Family data not found", 400
        
        validated_family = family_schema.load(data)
        response = create_family(validated_family)
        return response, 200
    
    except ValidationError as ve:
        logging.error(str(ve))
        return "Error validating a family", 400
    except Exception as e:
        logging.error(str(e))
        return "Error creating a family", 500      
        
@families_bp.route("<string:id>", methods=['GET'])
def get_family_bp(id):
    try:
        family = get_family(id)
        if not family:
            return "Family not found", 404
        
        return family, 200

    except Exception as e:
        logging.error(str(e))
        return "Error finding a family", 500

@families_bp.route("<string:id>", methods=['PUT'])
def update_family_bp(id):
    try:
        family = get_family(id)
        if not family:
            return "Family not found", 404
        
        data = request.get_json()
        if not data:
            return "Family data not found", 400
        
        validated_family = family_schema.load(data)
        response = update_family(id, validated_family)
        return response, 200
    
    except ValidationError as ve:
        logging.error(str(ve))
        return "Error validating a family", 400
    except Exception as e:
        logging.error(str(e))
        return "Error updating a family", 500
    
@families_bp.route("<string:id>", methods=['DELETE'])
def delete_family_bp(id):
    try:
        family = get_family(id)
        if not family:
            return "Family not found", 404
        
        response = delete_family(id)
        return response, 200
    
    except Exception as e:
        logging.error(str(e))
        return "Error deleting a family", 500
    
@families_bp.route("", methods=['GET'])
def get_all_families_bp():
    try:
        families = get_all_families()
        if not families:
            return "Families not found", 404
        
        return families, 200
    
    except Exception as e:
        logging.error(str(e))
        return "Error finding families", 500