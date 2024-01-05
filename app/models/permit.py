from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import false
from app.db import db

class Permit(db.Model):
    """Clase que representa los permisos de la base datos"""
    __tablename__ = "permits"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=false) #Los permisos han de tener el nombre apropiado al modulo y la funcion que dan permiso a usar, escritos como: ModuleName_Function


    @classmethod
    def create(cls, *args):
        """Crea un nuevo permiso"""
        permit = cls(*args)
        db.session.add(permit)
        db.session.commit()
        return permit


    @classmethod
    def all(cls):
        """Devuelve todos los permisos"""
        return cls.query.all()


    def __init__(self, name=None):
        self.name = name