from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import false
from app.db import db

class Color(db.Model):
    """Clase que representa los colores usados en las paletas de la aplicacion"""
    __tablename__ = "colors"
    id = Column(Integer, primary_key=True)
    value = Column(String(30), nullable=false) #Los permisos han de tener el nombre apropiado al modulo y la funcion que dan permiso a usar, escritos como: ModuleName_Function

    @classmethod
    def all(cls):
        """Devuelve todos los colores que hay cargados en la base de datos."""
        return cls.query.all()

    def __init__(self, value=None):
        self.value = value