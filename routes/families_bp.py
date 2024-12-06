from flask import Blueprint, request, abort
from models import FamilySchema
from marshmallow import ValidationError
from controllers.family_controller import get_family_by_name, create_family, get_all_families
import logging

family_schema = FamilySchema()

# Create a blueprint for families CRUD
families_bp = Blueprint('families', __name__, url_prefix="/families")

@families_bp.route("", methods=['GET'])
def get_families_bp():
    try:
        families = get_all_families()
        if families:
            return families, 200
        return "Families not found", 404
    except Exception as e:
        logging.error(str(e))
        return "Error finding families", 500
    
@families_bp.route("", methods=['POST'])
def create_family_bp():   
    try:
        data = request.get_json()
        if not data:
            return "Family data not found", 400
        validated_family = family_schema.load(data)
        if not validated_family:
            return "Family data not correct", 400
        family = create_family(validated_family)
        
        return family
    except Exception as e:
        logging.error(str(e))
        return "Error creating family", 500      
        
@families_bp.route("<string:name>", methods=['GET'])
def get_family_bp(name):
    try:
        family = get_family_by_name(name)
        if family:
            return (family, 200)
        return "Family not found", 404
    except Exception as e:
        logging.error(str(e))
        return "Error finding family", 500

@families_bp.route("<int:id>", methods=['PUT'])
def update_family_bp(id):
    return "NOT YET"
    
@families_bp.route("<int:id>", methods=['DELETE'])
def delete_family_bp(id):
    return "NOT YET"