import os
from flask.helpers import url_for
from werkzeug.utils import redirect, secure_filename
from ..models.modelos import *
from flask import Blueprint, app, render_template, request
from flask_login import login_required, current_user
from ..app import app

main = Blueprint('main', __name__)

@main.route('/')
def home():
    lugares = Lugares.query.all()
    return render_template('Home.html', lugares = lugares)

@main.route('/categorias')
def categorias():
    categorias= Categorias.query.all()
    return render_template('lugares.html', categorias = categorias)

@main.route('/profile')
@login_required
def profile():
    categorias= Categorias.query.all()
    return render_template('auth/profile.html', name=current_user.name, categorias=categorias)

@main.route('/insert', methods = ['POST'])
def insert():
    
    if request.method == 'POST':
        f= request.files['imagen']
        nombre_fichero = secure_filename(f.filename)
        f.save(app.root_path+'/static/images/lugares/'+nombre_fichero)
        nombre= request.form['nombre']
        descripcion=request.form['descripcion']
        contacto=request.form['contacto']
        direccion=request.form['direccion']
        categoriaId=request.form['categoria']
        imagen=nombre_fichero
        guardar_lugar= Lugares(nombre=nombre,descripcion=descripcion,contacto=contacto,direccion=direccion,imagen=imagen,categoriaId=categoriaId)
        db.session.add(guardar_lugar)
        db.session.commit()
        return redirect(url_for('main.profile'))