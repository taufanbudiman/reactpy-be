from flask import jsonify, request

from app.tasks.models import Tasks
from app.extensions import db


def list_tasks():
    tasks = Tasks.query.all()
    response = []
    for task in tasks:
        response.append(task.to_dict())
    return jsonify(response)


def create_task():
    request_form = request.json
    task = Tasks(
        title=request_form['title']
    )
    db.session.add(task)
    db.session.commit()

    return jsonify({'success': True}), 201


def update_task(task_id):
    request_form = request.json
    task = Tasks.query.get(task_id)

    task.title = request_form['title']
    db.session.commit()

    response = Tasks.query.get(task_id).to_dict()
    return jsonify(response)


def detail_task(task_id):
    response = Tasks.query.get(task_id)
    if response:
        response = response.to_dict()
    else:
        return jsonify({'success': False}), 404
    return jsonify(response)


def delete_task(task_id):
    task = Tasks.query.filter_by(id=task_id)
    task.delete()

    db.session.commit()

    return jsonify({'success': True, 'message': 'Task deleted'})
