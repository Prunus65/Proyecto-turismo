from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from ..models.modelos import User
from ..app import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    # Control de permisos
    if current_user.is_authenticated:
        return redirect(url_for("main.profile"))
    else: 
        return render_template('auth/login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remenber = True if request.form.get('remenber') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remenber)

    return redirect(url_for('main.profile'))

@auth.route('/signup')
def signup():
    # Control de permisos
    if current_user.is_authenticated:
        return redirect(url_for("main.profile"))
    else: 
        return render_template('auth/signup.html')

@auth.route('/signup', methods=['POST'])
def sign_up():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email addres alredy exists')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()
    flash('Cuenta creada existosamente')
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))