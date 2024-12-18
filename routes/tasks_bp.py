from flask import Blueprint, request, abort
from models import TaskSchema, TaskUpdateSchema
from marshmallow import ValidationError
from controllers.task_controller import create_task, get_task, update_task, delete_task, get_all_tasks, get_all_family_tasks, get_all_tasks_by_member
import logging


task_schema = TaskSchema()
task_update_schema = TaskUpdateSchema()

# Create a blueprint for tasks CRUD
tasks_bp = Blueprint('tasks', __name__, url_prefix="/tasks")

@tasks_bp.route("", methods=['POST'])
def create_task_bp():   
    try:
        data = request.get_json()
        if not data:
            return "Task data not found", 400
        
        validated_task = task_schema.load(data)
        task = create_task(validated_task)
        return task
    
    except ValidationError as ve:
        logging.error(str(ve))
        return "Error validating a task", 400
    except Exception as e:
        logging.error(str(e))
        return "Error creating a task", 500      
  
@tasks_bp.route("<string:id>", methods=['GET'])
def get_task_bp(id):
    try:
        task = get_task(id)
        if task:
            return (task, 200)
        
        return "Task not found", 404
    
    except Exception as e:
        logging.error(str(e))
        return "Error finding a task", 500


@tasks_bp.route("<string:id>", methods=['PUT'])
def update_task_bp(id):
    try:
        task = get_task(id)
        if not task:
            return "Task not found", 404
        
        data = request.get_json()
        if not data:
            return "Task data not found", 400
        
        validated_task = task_update_schema.load(data)
        response = update_task(id, validated_task)
        return response, 200
    
    except ValidationError as ve:
        logging.error(str(ve))
        return "Error validating a task", 400
    except Exception as e:
        logging.error(str(e))
        return "Error updating a task", 500
    
@tasks_bp.route("<string:id>", methods=['DELETE'])
def delete_task_bp(id):
    try:
        family = get_task(id)
        if not family:
            return "Task not found", 404
        
        response = delete_task(id)
        return response, 200
    
    except Exception as e:
        logging.error(str(e))
        return "Error deleting a task", 500

@tasks_bp.route("", methods=['GET'])
def get_all_tasks_bp():
    try:
        tasks = get_all_tasks()
        if not tasks:
            return "Tasks not found", 404

        return tasks, 200
    
    except Exception as e:
        logging.error(str(e))
        return "Error finding tasks", 500
   
@tasks_bp.route("member/<string:id>", methods=['GET'])
def get_all_tasks_by_member_bp(id):
    try:
        tasks = get_all_tasks_by_member(id)
        if not tasks:
            return "Tasks not found", 404
        
        return tasks, 200
    
    except Exception as e:
        logging.error(str(e))
        return "Error finding a task", 500