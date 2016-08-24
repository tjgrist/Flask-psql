from flask import Flask, jsonify, abort, make_response, request, url_for, Blueprint

tasks = [
    {
        'id' : 1,
        'title' : u"buy groceries",
        'description' : u"milk, cheese, bread, pizza",
        'done' : False
    },
    {
        'id' : 2,
        'title' : u"learn python",
        'description' : u"find a great tutorial",
        'done' : True
    }
]

mod = Blueprint('todo', __name__)

@mod.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}), 404)

@mod.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

@mod.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task':task[0]})

@mod.route('/api/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id' : tasks[-1]['id'] + 1,
        'title' : request.json['title'],
        'description' : request.json.get('description', ""),
        'done' : False
    }
    tasks.append(task)
    return jsonify({'task' : task}), 201

@mod.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

@mod.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})