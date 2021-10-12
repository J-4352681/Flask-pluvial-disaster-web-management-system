from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.orm import relationship
from app.db import db

class Role(db.Model):
    """Clase que representa los roles de la base datos"""
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=false)
    permits = relationship("permits")

    @classmethod
    def all(cls):
        """Devuelve todos los roles"""
        return cls.query.all()

    @classmethod
    def get_admin(cls):
        """Devuelve el rol con el trabajo del administrador. Si hay algun cambio a la reprecentacion del rol admin en la base datos solo se cambiara este metodo."""
        rol = cls.query.filter(
            cls.name == "admin" 
        ).first()
        return rol

    @classmethod
    def get_operator(cls):
        """Devuelve el rol con el trabajo del operador/a. Si hay algun cambio a la reprecentacion del rol operador/a en la base datos solo se cambiara este metodo."""
        rol = cls.query.filter(
            cls.name == "operator" 
        ).first()
        return rol

    def __init__(self, name=None):
        self.name = name