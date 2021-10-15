from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import false, true
from app.db import db

class Color(db.Model):
    """Clase que representa los colores usados en las paletas de la aplicacion"""
    __tablename__ = "colors"
    id = Column(Integer, primary_key=True)
    value = Column(String(30), nullable=false, unique=true) # El nombre con el que HTML lo reconozca

    @classmethod
    def all(cls):
        """Devuelve todos los colores que hay cargados en la base de datos."""
        return cls.query.all()

    @classmethod
    def create(cls, value):
        """Crea un nuevo color con los parametros mandados."""
        new_color = Color(value)
        db.session.add(new_color)
        db.session.commit()
    
    @classmethod
    def find_by_id(cls, id):
        """Encuentra un color por id con su valor apropiado. Su valor es su nombre reconocido por HTML."""
        color = cls.query.filter(
            cls.value == id
        ).first()
        return color


    @classmethod
    def find_by_value(cls, value):
        """Encuentra un nombre con su valor apropiado. Su valor es su nombre reconocido por HTML."""
        color = cls.query.filter(
            cls.value == value
        ).first()
        return color

    def __init__(self, value=None):
        self.value = value