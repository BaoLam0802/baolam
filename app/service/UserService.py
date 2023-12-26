from flask import Blueprint, jsonify, request
from app.models.User import User, db
from flask_jwt_extended import JWTManager

jwt = JWTManager()

server_bp = Blueprint('server', __name__)

@server_bp.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    new_user = User(UserName=data['username'], Email=data['email'], PassWord=data['password'])

    db.session.add(new_user)
    db.session.commit()  # Lưu thay đổi vào cơ sở dữ liệu

    return jsonify({'message': 'User created successfully'}), 201

# Get all users
@server_bp.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    user_list = [{'UserID': user.UserID, 'UserName': user.UserName, 'Email': user.Email, 'Password': user.PassWord} for user in users]
    return jsonify({'users': user_list})

# Get a specific user by ID
@server_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)

    if user:
        user_info = {'UserID': user.UserID, 'UserName': user.UserName, 'Email': user.Email, 'Password': user.PassWord}
        return jsonify({'user': user_info})
    
    return jsonify({'message': 'User not found'}), 404

# Update a user by ID
@server_bp.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)

    if user:
        data = request.get_json()
        user.UserName = data.get('username', user.UserName)
        user.Email = data.get('email', user.Email)
        user.PassWord = data.get('password', user.PassWord)

        db.session.commit()

        return jsonify({'message': 'User updated successfully'})

    return jsonify({'message': 'User not found'}), 404

# Delete a user by ID
@server_bp.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})

    return jsonify({'message': 'User not found'}), 404