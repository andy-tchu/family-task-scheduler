import logging
from flask import abort, request
from config.db import get_db_conn
import json
from bson import json_util, ObjectId


# create user
def create_user(user):
    """
    - receive a user as a dictionary of (username, password, telegram, admin)
    """
    try:
        db_conn = get_db_conn()
        user_id = db_conn["users"].insert_one(user)
        user_id_str = str(user_id.inserted_id)
        logging.info(f"Created a user with a user_id of: {user_id_str}")
        return {"message": "Created user", "id": user_id_str}
    
    except Exception as e:
        logging.error(str(e))
        abort(500)

# get user
def get_user(id):
    try:    
        db_conn = get_db_conn()
        found_user = db_conn["users"].find_one({"_id": ObjectId(id)})
        endpoint = request.endpoint
        logging.info(f"get_user, {endpoint}: {found_user}")
        return json.loads(json_util.dumps(found_user))
    
    except Exception as e:
        logging.error(str(e))
        abort(500)

# update user
def update_user(id, user):
    """
    - receive a user as a dictionary of (telegram, admin)
    """
    try:
        db_conn = get_db_conn()
        db_conn["users"].update_one({"_id": ObjectId(id)},{"$set": {"telegram": user["telegram"], "admin": user["admin"]}}, upsert=False)
        logging.info(f"Updated a user with a users_id of: {id}")
        return {"message": "Updated user", "id": id}
    
    except Exception as e:
        logging.error(str(e))
        abort(500)

# delete user
def delete_user(id):
    try:
        db_conn = get_db_conn()
        db_conn["users"].delete_one({"_id": ObjectId(id)})
        logging.info(f"Deleted a user with a user_id of: {id}")
        return {"message": "Deleted user", "id": id}
    
    except Exception as e:
        logging.error(str(e))
        abort(500)

# get all users
def get_all_users():
    try:
        db_conn = get_db_conn()
        users = list(db_conn['users'].find())
        logging.info(f"Looked and found users: {len(users)}")
        return json.loads(json_util.dumps(users))
    
    except Exception as e:
        logging.error(str(e))
        abort(500)
        
#get user by username
def get_user_by_username(username):
    try:    
        db_conn = get_db_conn()
        found_user = db_conn["users"].find_one({"username": username})
        endpoint = request.endpoint
        logging.info(f"get_user_by_username, {endpoint}: {found_user}")
        return json.loads(json_util.dumps(found_user))
    
    except Exception as e:
        logging.error(str(e))
        abort(500)

