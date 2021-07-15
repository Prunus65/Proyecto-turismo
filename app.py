from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Estoesunsecreto'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/turismapp.db'

db = SQLAlchemy(app)

from controlador import *

if __name__ == '__main__':
    app.run(debug=True)
