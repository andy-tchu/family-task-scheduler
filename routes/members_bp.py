from flask import Blueprint, request, abort
from models import MemberSchema
from marshmallow import ValidationError
from controllers.member_controller import get_all_members, get_member_by_familyname_and_name, create_member, get_all_family_members_by_name
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
        validated_family = member_schema.load(data)
        if not validated_family:
            return "Member data not correct", 400
        member = create_member(validated_family)
        
        return member
    except Exception as e:
        logging.error(str(e))
        return "Error creating family", 500      
        
@members_bp.route("<string:name>", methods=['GET'])
def get_family_bp(name):
    try:
        family = get_family_by_name(name)
        if family:
            return (family, 200)
        return "Family not found", 404
    except Exception as e:
        logging.error(str(e))
        return "Error finding family", 500

@members_bp.route("<int:id>", methods=['PUT'])
def update_family_bp(id):
    return "NOT YET"
    
@members_bp.route("<int:id>", methods=['DELETE'])
def delete_family_bp(id):
    return "NOT YET"