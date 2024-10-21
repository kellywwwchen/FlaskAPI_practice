from io import StringIO
from flask import Blueprint, request, jsonify
from services.user_service import UserService

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    if 'name' not in data or 'age' not in data:
        return jsonify({'error': 'name or age cannot be empty'}), 400

    name = request.json['name']
    age = request.json['age']

    if age >= 150 or age < 0:
        return jsonify({'error': f'Age must be more than 0 or less than 150'}), 400
    
    if UserService.create_user(name, age):
        return jsonify({'message': f'user: {name} created successfully.'}), 201
    else:
        return jsonify({'message': f'user: {name} already exists.'}), 409

@bp.route('/', methods=['GET'])
def get_all_users():
    users = UserService.get_all_users()
    return jsonify(users)

@bp.route('/<name>', methods=['DELETE'])
def delete_user(name):
    if UserService.delete_user(name):
        return jsonify({'message': f'user: {name} deleted successfully.'}), 200
    else:
        return jsonify({'message': f'user: {name} does not exist.'}), 404    

@bp.route('/upload', methods=['POST'])
def upload_users():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_data = StringIO(file.read().decode('utf-8'))
    UserService.upload_users(file_data)
    return jsonify({'message': 'Users be added from uploaded file'}), 201

@bp.route('/average-age', methods=['GET'])
def average_age():
    if not UserService.average_age():
        return jsonify({'message': 'No users'}), 404
    result = UserService.average_age()
    return jsonify(result)