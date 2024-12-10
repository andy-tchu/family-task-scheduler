from flask import Blueprint, request, abort
from models import MemberSchema
from marshmallow import ValidationError
from controllers.member_controller import get_all_members, get_all_family_members, create_member, get_member
from controllers.family_controller import get_family
import logging

member_schema = MemberSchema()

# Create a blueprint for members CRUD
members_bp = Blueprint('members', __name__, url_prefix="/members")

@members_bp.route("", methods=['GET'])
def get_members_bp():
    try:
        members = get_all_members()
        if members:
            return members, 200
        return "Members not found", 404
    except Exception as e:
        logging.error(str(e))
        return "Error finding members", 500
    
@members_bp.route("", methods=['POST'])
def create_member_bp():   
    try:
        data = request.get_json()
        if not data:
            return "Member data not found", 400
        
        validated_member = member_schema.load(data)
        if not validated_member:
            return "Member data not correct", 400
        
        member = create_member(validated_member)
        
        return member
    except Exception as e:
        logging.error(str(e))
        return "Error creating member", 500      
        
@members_bp.route("<string:id>", methods=['GET'])
def get_member_bp(id):
    try:
        member = get_member(id)
        if member:
            return (member, 200)
        return "Member not found", 404
    except Exception as e:
        logging.error(str(e))
        return "Error finding member", 500
    
@members_bp.route("family/<string:id>", methods=['GET'])
def get_all_family_members_bp(id):
    try:
        family = get_family(id)
        if not family:
            return "Family not found", 404
        
        return get_all_family_members(id)
    
    except Exception as e:
        logging.error(str(e))
        return "Error finding family members", 500

@members_bp.route("<int:id>", methods=['PUT'])
def update_family_bp(id):
    return "NOT YET"
    
@members_bp.route("<int:id>", methods=['DELETE'])
def delete_family_bp(id):
    return "NOT YET"