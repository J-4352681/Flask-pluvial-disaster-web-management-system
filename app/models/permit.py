from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.orm import relationship
from app.db import db

class Role(db.Model):
    """Clase que representa los permisos de la base datos"""
    __tablename__ = "permits"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=false) #Los permisos han de tener el nombre apropiado al modulo y la funcion que dan permiso a usar, escritos como: ModuleName_Function

    @classmethod
    def all(cls):
        """Devuelve todos los permisos"""
        return cls.query.all()

    def __init__(self, name=None):
        self.name = name