from flask import Blueprint, request
from models import MemberSchema, MemberUpdateSchema
from marshmallow import ValidationError
from controllers.member_controller import create_member, get_member, update_member, delete_member, get_all_members, get_all_family_members
from controllers.family_controller import get_family
import logging


member_schema = MemberSchema()
member_update_schema = MemberUpdateSchema()

# Create a blueprint for members CRUD
members_bp = Blueprint('members', __name__, url_prefix="/members")
   
@members_bp.route("", methods=['POST'])
def create_member_bp():   
    try:
        data = request.get_json()
        if not data:
            return "Member data not found", 400
        
        validated_member = member_schema.load(data)
        member = create_member(validated_member)
        return member
    
    except ValidationError as ve:
        logging.error(str(ve))
        return "Error validating a member", 400
    except Exception as e:
        logging.error(str(e))
        return "Error creating a member", 500      
        
@members_bp.route("<string:id>", methods=['GET'])
def get_member_bp(id):
    try:
        member = get_member(id)
        if not member:
            return "Member not found", 404
        
        return (member, 200)
        
    except Exception as e:
        logging.error(str(e))
        return "Error finding a member", 500

@members_bp.route("<string:id>", methods=['PUT'])
def update_member_bp(id):
    try:
        member = get_member(id)
        if not member:
            return "Member not found", 404
        
        data = request.get_json()
        if not data:
            return "Member data not found", 400
        
        validated_member = member_update_schema.load(data)
        response = update_member(id, validated_member)
        return response, 200
    
    except ValidationError as ve:
        logging.error(str(ve))
        return "Error validating a member", 400
    except Exception as e:
        logging.error(str(e))
        return "Error updating a member", 500
    
@members_bp.route("<string:id>", methods=['DELETE'])
def delete_member_bp(id):
    try:
        member = get_family(id)
        if not member:
            return "Member not found", 404
        
        response = delete_member(id)
        return response, 200
    
    except Exception as e:
        logging.error(str(e))
        return "Error deleting a member", 500

@members_bp.route("", methods=['GET'])
def get_all_members_bp():
    try:
        members = get_all_members()
        if members:
            return members, 200
        
        return "Members not found", 404
    
    except Exception as e:
        logging.error(str(e))
        return "Error finding members", 500

@members_bp.route("family/<string:id>", methods=['GET'])
def get_all_family_members_bp(id):
    try:
        family = get_family(id)
        if not family:
            return "Family not found", 404
        
        return get_all_family_members(id)
    
    except Exception as e:
        logging.error(str(e))
        return "Error finding a family members", 500