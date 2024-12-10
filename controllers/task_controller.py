import logging
from flask import abort, request
from config.db import get_db_conn
import json
from bson import json_util, ObjectId


# get task
def get_task(id):
    try:    
        db_conn = get_db_conn()

        found_task = db_conn["tasks"].find_one({"_id":id})
        endpoint = request.endpoint
        logging.info(f"{endpoint}: {found_task}")

        return json.loads(json_util.dumps(found_task))
    
    except Exception as e:
        logging.error(str(e))
        abort(500)

# get all tasks
def get_all_tasks():
    try:
        db_conn = get_db_conn()
        
        found_tasks = list(db_conn['tasks'].find())
        logging.info(f"Looked and found tasks: {len(found_tasks)}")

        return json.loads(json_util.dumps(found_tasks))
    
    except Exception as e:
        logging.error(str(e))
        abort(500)
    
# get all family tasks
def get_all_family_tasks(id):
    try:
        db_conn = get_db_conn()
        found_family = db_conn["families"].find_one({"_id": ObjectId(id)})
        if not found_family:
            logging.error("Family not found")
            abort(404)
        
        found_tasks = list(db_conn['tasks'].find({"familyId": found_family["_id"]}))
        logging.info(f"Looked and found family tasks: {len(found_tasks)}")

        return json.loads(json_util.dumps(found_tasks))
    
    except Exception as e:
        logging.error(str(e))
        abort(500)

# get all member tasks
def get_all_tasks_by_member(id):
    try:
        db_conn = get_db_conn()
        found_member = db_conn["members"].find_one({"_id": ObjectId(id)})

        if not found_member:
            logging.error("Member not found")
            abort(404)
        
        tasks = list(db_conn['tasks'].find({"assignedTo": found_member}))
        logging.info(f"Looked and found member tasks: {len(tasks)}")

        return json.loads(json_util.dumps(tasks))
    
    except Exception as e:
        logging.error(str(e))
        abort(500)
        
# create task
def create_task(task):
    """
    - receive a task as a dictionary of (title, description, assigned_to[], family_id, date, priority, status, notes)
    """
    try:
        db_conn = get_db_conn()

        assigned_members =[]
        for task_id in task["assignedTo"]:
            found_member = db_conn["members"].find_one({"_id": ObjectId(task_id)})
            if not found_member:
                return "Member not found", 404
            assigned_members.append(found_member)
        task['assignedTo']=assigned_members

        found_family = db_conn["families"].find_one({"_id": ObjectId(task["familyId"])})
        if not found_family:
            return "Family not found", 404
        task["familyId"] = found_family

        task_id = db_conn["tasks"].insert_one(task)
        task_id_str = str(task_id.inserted_id)
        logging.info(f"Created a task with a member_id of: {task_id_str}")

        return {"message": "Created task", "id": task_id_str}
    
    except Exception as e:
        logging.error(str(e))
        abort(500)

# update family
# delete family
