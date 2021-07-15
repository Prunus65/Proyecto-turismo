from app import app
from modelos import *
from flask import render_template

@app.route('/')
def home():
    lugares = Lugares.query.all()
    return render_template('Home.html', lugares = lugares)

@app.route('/about')
def home():
    lugares = Lugares.query.all()
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada..."), 404
