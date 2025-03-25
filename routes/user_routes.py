# routes/user_routes.py
from flask import Blueprint, request, render_template, redirect, url_for
from models.user import db, User
from werkzeug.security import generate_password_hash, check_password_hash

user_bp = Blueprint('user', __name__)


@user_bp.route('/', methods=['GET'])
def list_users():
    users = User.query.all()
    return render_template('users.html', users=users)


@user_bp.route('/users/new', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        senha = request.form['senha']
        
        hash_senha = generate_password_hash(
            senha, method='pbkdf2:sha256', salt_length=16)
        
        new_user = User(name=name, email=email, senha=hash_senha)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('user.list_users'))
    return render_template('new_user.html')


@user_bp.route('/users/edit/<int:id>', methods=['GET', 'POST'])
def edit_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.name = request.form['name']
        user.email = request.form['email']
        db.session.commit()
        return redirect(url_for('user.list_users'))
    return render_template('edit_user.html', user=user)


@user_bp.route('/users/delete/<int:id>', methods=['POST'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('user.list_users'))
