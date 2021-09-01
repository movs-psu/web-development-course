from flask import Flask, request, session, jsonify
from .entities import User, Todo
from .storage import Storage

app = Flask(__name__)

app.secret_key = b'super-secret-key'


@app.route('/api/me')
def me():
    if 'user_id' not in session:
        return 'Not authorized!', 401
    user = Storage.get_user_by_id(session['user_id'])
    return jsonify(user.__dict__)


@app.route('/api/login', methods=['POST'])
def login_action():
    if not request.json['email']:
        return "Требуется ввести Email", 422
    if not request.json['password']:
        return "Требуется ввести пароль", 422

    user = Storage.get_user_by_email_and_password(request.json['email'], request.json['password'])

    if not user:
        return "Неверный пароль", 401

    session['user_id'] = user.id

    return jsonify(user.__dict__)


@app.route('/api/registration', methods=['post'])
def registration_action():
    error = None
    if not request.json['email']:
        error = "Требуется ввести Email"
    if not request.json['password']:
        error = "Требуется ввести пароль"

    if error:
        return error, 422

    Storage.add_user(User(None, request.json['email'], request.json['password']))

    return '', 200


@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id')
    return '', 200


@app.route('/api/todos')
def todos():
    if 'user_id' not in session:
        return 'Not authorized!', 401
    user = Storage.get_user_by_id(session['user_id'])
    todos = Storage.get_user_todos(user.id)
    return jsonify({'todos': list(map(lambda todo: todo.__dict__, todos)) })


@app.route('/api/todos', methods=['POST'])
def add_todo_api():
    if 'user_id' not in session:
        return 'Not authorized!', 401
    todo = Storage.add_todo(Todo(None, request.json['title'], session['user_id'], None))
    return jsonify(todo.__dict__)


@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if 'user_id' not in session:
        return 'Not authorized!', 401
    Storage.delete_todo(todo_id)
    return '', 200
