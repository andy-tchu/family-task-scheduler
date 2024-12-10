from flask import Blueprint, request, abort
from models import TaskSchema
from marshmallow import ValidationError
from controllers.task_controller import get_task, create_task, get_all_tasks, get_all_family_tasks, get_all_tasks_by_member
import logging

task_schema = TaskSchema()

# Create a blueprint for tasks CRUD
tasks_bp = Blueprint('tasks', __name__, url_prefix="/tasks")

@tasks_bp.route("", methods=['GET'])
def get_all_tasks_bp():
    try:
        tasks = get_all_tasks()
        if tasks:
            return tasks, 200
        
        return "Tasks not found", 404
    
    except Exception as e:
        logging.error(str(e))
        return "Error finding tasks", 500
    
@tasks_bp.route("", methods=['POST'])
def create_task_bp():   
    try:
        data = request.get_json()
        if not data:
            return "Task data not found", 400
        validated_task = task_schema.load(data)
        if not validated_task:
            return "Family data not correct", 400
        task = create_task(validated_task)
        
        return task
    
    except Exception as e:
        logging.error(str(e))
        return "Error creating task", 500      
        
@tasks_bp.route("<string:id>", methods=['GET'])
def get_task_bp(id):
    try:
        task = get_task(id)
        if task:
            return (task, 200)
        
        return "Task not found", 404
    
    except Exception as e:
        logging.error(str(e))
        return "Error finding task", 500

@tasks_bp.route("member/<string:id>", methods=['GET'])
def get_all_tasks_by_member_bp(id):
    try:
        task = get_all_tasks_by_member(id)
        if task:
            return (task, 200)
        
        return "Task not found", 404
    
    except Exception as e:
        logging.error(str(e))
        return "Error finding task", 500

@tasks_bp.route("<int:id>", methods=['PUT'])
def update_family_bp(id):
    return "NOT YET"
    
@tasks_bp.route("<int:id>", methods=['DELETE'])
def delete_family_bp(id):
    return "NOT YET"