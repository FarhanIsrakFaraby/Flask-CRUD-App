# from flask import Blueprint, request, jsonify
# from app.models.user import User
# from app import db

# user_routes = Blueprint('user_routes', __name__)

# @user_routes.route('/api/users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     return jsonify([user.to_dict() for user in users])

# @user_routes.route('/api/users', methods=['POST'])
# def create_user():
#     data = request.get_json()
#     new_user = User(**data)
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(new_user.to_dict()), 201

# @user_routes.route('/api/user/edit/<int:id>', methods=['PUT'])
# def update_user(id):
#     user = User.query.get_or_404(id)
#     data = request.get_json()
#     for key, value in data.items():
#         setattr(user, key, value)
#     db.session.commit()
#     return jsonify(user.to_dict())

# @user_routes.route('/api/user/delete/<int:id>', methods=['DELETE'])
# def delete_user(id):
#     user = User.query.get_or_404(id)
#     db.session.delete(user)
#     db.session.commit()
#     return jsonify({'message': 'User deleted'}), 204


from flask import Blueprint, request, jsonify, flash, app
from flask_mysqldb import MySQL

user_routes = Blueprint('user_routes', __name__)

# Initialize MySQL
mysql = MySQL()

@user_routes.route('/api/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, fname, lastname, username FROM users")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@user_routes.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    fname = data['fname']
    lastname = data['lastname']
    username = data['username']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (fname, lastname, username) VALUES (%s, %s, %s)", (fname, lastname, username))
    mysql.connection.commit()
    return jsonify({'message': 'User created'}), 201

@user_routes.route('/api/user/edit/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    fname = data['fname']
    lastname = data['lastname']
    username = data['username']
    cur = mysql.connection.cursor()
    cur.execute("""
               UPDATE users
               SET fname=%s, lastname=%s, username=%s
               WHERE id=%s
            """, (fname, lastname, username, id))
    mysql.connection.commit()
    return jsonify({'message': 'User updated'})

@user_routes.route('/api/user/delete/<int:id>', methods=['DELETE'])
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (id,))
    mysql.connection.commit()
    return jsonify({'message': 'User deleted'}), 204

@app.route('/api/users')
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    results = cur.fetchall()
    return str(results)
