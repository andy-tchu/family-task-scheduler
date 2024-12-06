import logging
from flask import abort, request
from config.db import get_db_conn
import json
from bson import json_util


# get member
def get_member(id):
    try:    
        db_conn = get_db_conn()
        found_member = db_conn["members"].find_one({"_id":id})
        endpoint = request.endpoint
        logging.info(f"{endpoint}: {found_member}")
        return found_member
    except Exception as e:
        logging.error(str(e))
        abort(500)

# get all members
def get_all_members():
    try:
        db_conn = get_db_conn()
        
        members = list(db_conn['members'].find())
        logging.info(f"Looked and found members: {len(members)}")
        return json.loads(json_util.dumps(members))
    except Exception as e:
        logging.error(str(e))
        abort(500)
    
# get all family members
def get_all_family_members_by_name(name):
    try:
        db_conn = get_db_conn()
        found_family = db_conn["families"].find_one({"name": name})
        if not found_family:
            return "Family not found", 404
        
        members = list(db_conn['members'].find({"familyId": found_family["_id"]}))
        logging.info(f"Looked and found family members: {len(members)}")
        return json.loads(json_util.dumps(members))
    except Exception as e:
        logging.error(str(e))
        abort(500)
        
# create member
def create_member(member):
    """
    - receive a member as a dictionary of (name, role, phone, username, family_name)
    """
    try:
        db_conn = get_db_conn()
        found_user = db_conn["users"].find_one({"username": member["username"]})
        if not found_user:
            return "User not found", 404
        member["userId"] = found_user["_id"]
        
        found_family = db_conn["families"].find_one({"name": member["family_name"]})
        print(found_family)
        if not found_family:
            return "Family not found", 404
        member["familyId"] = found_family["_id"]

        member_id = db_conn["members"].insert_one(member)
        member_id_str = str(member_id.inserted_id)
        logging.info(f"Created a member with a member_id of: {member_id_str}")
        return {"message": "Created member", "id": member_id_str}
    except Exception as e:
        logging.error(str(e))
        abort(500)

def get_member_by_familyname_and_name(family_name, name):
    try:    
        db_conn = get_db_conn()
        found_family = db_conn["families"].find_one({"name": family_name})
        if not found_family:
            return "Family not found", 404
        
        found_member = db_conn['members'].find({"familyId": found_family["_id"], "name": name})
        endpoint = request.endpoint
        logging.info(f"{endpoint}: {found_member}")
        return json.loads(json_util.dumps(found_member))
    except Exception as e:
        logging.error(str(e))
        abort(500)

# update family
# delete family
