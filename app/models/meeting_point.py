from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from app.db import db

class Meeting_point(db.Model):
    """Clase que representa los puntos de encuentro en la base datos"""
    __tablename__ = "meeting_points"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=false)
    direction = Column(String(100), nullable=false)
    coordinates = Column(String(100), nullable=false)
    state = Column(Boolean, default=true, nullable=false) # publicado o despublicado
    telephone = Column(String(30), nullable=false)
    email = Column(String(100), nullable=false)

    @classmethod
    def create(cls, params):
        """Crea un nuevo punto de encuentro."""
        new_user = Meeting_point(params)
        db.session.add(new_user)
        db.session.commit()

    @classmethod
    def delete(cls, name_param=None):
        """Elimina un punto de encuentro cuyo nombre coincide con el nombre mandado como parametro."""
        user_selected = Meeting_point.query.filter_by(name=name_param).first()
        db.session.delete(user_selected)
        db.session.commit()

    @classmethod
    def all(cls):
        """Devuelve todos los puntos de encuentro"""
        return cls.query.all()

    def __init__(self, name=None, direction=None, coordinates=None, telephone=None, email=None):
        self.name = name
        self.direction = direction
        self.coordinates = coordinates
        self.telephone = telephone
        self.email = email