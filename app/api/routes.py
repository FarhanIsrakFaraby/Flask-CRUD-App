from flask import Blueprint, jsonify, request, render_template, redirect, url_for, json
from app.models import User
from app import db
from flask import current_app as app


bp = Blueprint('api', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@bp.route('/users/add', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Username and email are required'}), 400
    user = User(username=data['username'] )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

# @app.route('/user/add', methods=['GET', 'POST'])
# def create_user():
#     if request.method == 'POST':
#         user = User(fname=request.form['fname'], lastname=request.form['lastname'], username=request.form['username'])
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('add_user.html')


@bp.route('/user/edit<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    if 'username' in data:
        user.username = data['username']
    if 'email' in data:
        user.email = data['email']
    db.session.commit()
    return jsonify(user.to_dict())

@bp.route('/user/delete<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return '', 204



@app.route('/')
def index():
    users = User.query.all()
    return render_template('list_users.html', users=users)

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())


# @app.route('/user/add', methods=['GET', 'POST'])
# def create_user():
#     if request.method == 'POST':
#         user = User(fname=request.form['fname'], lastname=request.form['lastname'], username=request.form['username'])
#         db.session.add(user)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('add_user.html')

# @app.route('/user/edit/<int:id>', methods=['GET', 'POST'])
# def edit_user(id):
    
#     user = User.query.get_or_404(id)
#     if request.method == 'POST':
#         user.fname = request.form['fname']
#         user.lastname = request.form['lastname']
#         user.username = request.form['username']
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('edit_user.html', user=user)

# @app.route('/user/delete/<int:id>', methods=['GET', 'POST'])
# def delete_user(id):
#     user = User.query.get_or_404(id)
#     db.session.delete(user)
#     db.session.commit()
#     return redirect(url_for('index'))