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

@main.route('/lugar/<string:name>')
def lugar(name):
    sitio = Lugares.query.filter_by(nombre=name).first()
    comentarios = Comentarios.query.filter_by(lugarId=1).all()
    return render_template('lugar.html', lugar=sitio, comentarios=comentarios, login=current_user.is_authenticated)

@main.route('/comentar/<id>', methods = ['POST'])
def comentar(id):
    if request.method == 'POST':
        lugarId = id
        comentario = request.form["comentario"]
        usuarioId = current_user.id
        saveComentario = Comentarios(comentario=comentario, usuarioId=usuarioId, lugarId=lugarId)
        db.session.add(saveComentario)
        db.session.commit()
        sitio = Lugares.query.filter_by(id=id).first()
        return redirect(url_for('main.lugar', name=sitio.nombre))


@main.route('/categorias')
def categorias():
    categorias= Categorias.query.all()
    return render_template('categorias.html', categorias = categorias)

@main.route('/categoria/<id>')
def categoria(id):
    lugaresByCat = Lugares.query.filter_by(categoriaId=id)
    categoria = Categorias.query.filter_by(id=id).first()
    colorOptions = {
        1: 'warning',
        2: 'primary',
        3: 'danger',
        4: 'success'
    }
    color = colorOptions.get(categoria.id)
    return render_template('lugares.html', lugares = lugaresByCat, categoria=categoria, color=color)

@main.route('/profile')
@login_required
def profile():
    categorias= Categorias.query.all()
    lugares = Lugares.query.all()
    return render_template('auth/profile.html', categorias=categorias, lugares = lugares)

@main.route('/insert', methods = ['POST'])
@login_required
def insert():
    if request.method == 'POST':
        f= request.files['imagen']
        nombre_fichero = secure_filename(f.filename)
        f.save(app.root_path+'/static/images/lugares/'+nombre_fichero)
        nombre= request.form['nombre']
        descripcion=request.form['descripcion']
        contacto=request.form['contacto']
        direccion=request.form['direccion']
        coordenadas=request.form['coordenadas']
        categoriaId=request.form['categoria']
        imagen=nombre_fichero
        guardar_lugar= Lugares(nombre=nombre,descripcion=descripcion,contacto=contacto,direccion=direccion,imagen=imagen,coordenadas=coordenadas,categoriaId=categoriaId)
        db.session.add(guardar_lugar)
        db.session.commit()
        return redirect(url_for('main.profile'))

@main.route('/update/<id>', methods = ['POST'])
@login_required
def update(id):
    if request.method == 'POST':
        lugar = Lugares.query.filter_by(id=id).first()
        os.remove(app.root_path+'/static/images/lugares/'+lugar.imagen)
        f= request.files['imagen']
        nombre_fichero = secure_filename(f.filename)
        f.save(app.root_path+'/static/images/lugares/'+nombre_fichero)
        lugar.nombre=request.form['nombre']
        lugar.descripcion=request.form['descripcion']
        lugar.contacto=request.form['contacto']
        lugar.direccion=request.form['direccion']
        lugar.coordenadas=request.form['coordenadas']
        lugar.categoriaId=request.form['categoria']
        lugar.imagen=nombre_fichero
        db.session.commit()
        return redirect(url_for('main.profile'))

@main.route('/delete/<id>', methods= ['GET', 'POST'])
@login_required
def delete(id):
    lugar = Lugares.query.filter_by(id=id).first()
    os.remove(app.root_path+'/static/images/lugares/'+lugar.imagen)
    Lugares.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('main.profile'))
