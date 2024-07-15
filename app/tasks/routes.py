from flask import request
from flask_jwt_extended import jwt_required

from app.tasks import bp
from app.tasks.controllers import list_tasks, create_task, update_task, \
    delete_task, detail_task


@bp.route('/tasks', methods=['GET', 'POST'])
@jwt_required()
def tasks():
    if request.method == 'GET':
        return list_tasks()
    elif request.method == 'POST':
        return create_task()
    else:
        return 'Method is Not Allowed'


@bp.route('/tasks/<task_id>', methods=['GET','PUT', 'DELETE'])
@jwt_required()
def task(task_id):
    if request.method == 'PUT':
        return update_task(task_id)
    elif request.method == 'DELETE':
        return delete_task(task_id)
    elif request.method == 'GET':
        return detail_task(task_id)
    else:
        return 'Method is Not Allowed'
