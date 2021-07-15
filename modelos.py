from sqlalchemy.sql.schema import ForeignKey
from app import db
from sqlalchemy.orm import relationship

class Lugares(db.Model):
    __tablename__ = 'lugares'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))
    contacto = db.Column(db.Integer)
    direccion = db.Column(db.String(100))
    imagen = db.Column(db.String(100))
    categoriaId = db.Column(db.Integer,ForeignKey('categorias.id'), nullable=False)
    categoria = relationship('Categorias', backref='Lugares')


class Categorias(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(25))
    lugares = relationship('Lugares', backref='Categorias', lazy='dynamic')