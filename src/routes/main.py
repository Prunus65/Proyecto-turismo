from ..models.modelos import *
from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def home():
    lugares = Lugares.query.all()
    return render_template('Home.html', lugares = lugares)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('auth/profile.html', name=current_user.name)