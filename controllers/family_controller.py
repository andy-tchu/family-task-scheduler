import logging
from flask import abort, request
from config.db import get_db_conn
import json
from bson import json_util


# get family
def get_family(id):
    try:    
        db_conn = get_db_conn()
        found_user = db_conn["families"].find_one({"_id":id})
        endpoint = request.endpoint
        logging.info(f"{endpoint}: {found_user}")
        return found_user
    except Exception as e:
        logging.error(str(e))
        abort(500)
    
# get all families
def get_all_families():
    try:
        db_conn = get_db_conn()
        families = list(db_conn['families'].find())
        logging.info(f"Looked and found families: {len(families)}")
        return json.loads(json_util.dumps(families))
    except Exception as e:
        logging.error(str(e))
        abort(500)
        
# create family
def create_family(family):
    """
    - receive a family as a dictionary of (name)
    """
    try:
        db_conn = get_db_conn()
        family_id = db_conn["families"].insert_one(family)
        family_id_str = str(family_id.inserted_id)
        logging.info(f"Created a family with a family_id of: {family_id_str}")
        return {"message": "Created family", "id": family_id_str}
    except Exception as e:
        logging.error(str(e))
        abort(500)

def get_family_by_name(name):
    try:    
        db_conn = get_db_conn()
        found_family = db_conn["families"].find_one({"name": name})
        endpoint = request.endpoint
        logging.info(f"{endpoint}: {found_family}")
        return json.loads(json_util.dumps(found_family))
    except Exception as e:
        logging.error(str(e))
        abort(500)

# update family
# delete family
