import os
from flask.helpers import url_for
from werkzeug.utils import redirect, secure_filename
from ..models.modelos import *
from flask import Blueprint, app, render_template, request
from flask_login import login_required, current_user
from ..app import app

admin = Blueprint('admin', __name__)

@admin.route('/admin/categoria/<id>')
def categoria(id):
    lugaresByCat = Lugares.query.filter_by(categoriaId=id)
    categoria = Categorias.query.filter_by(id=id).first()
    return render_template('lugares.html', lugares = lugaresByCat, categoria=categoria)

@admin.route('/comercial')
def comercial():
    categorias= Categorias.query.all()
    return render_template('lugares.html', categorias = categorias)

@admin.route('/gastronomia')
def categorias():
    categorias= Categorias.query.all()
    return render_template('lugares.html', categorias = categorias)

@admin.route('/viveros')
@login_required
def profile():
    categorias= Categorias.query.all()
    lugares = Lugares.query.all()
    return render_template('auth/profile.html', categorias=categorias, lugares = lugares)