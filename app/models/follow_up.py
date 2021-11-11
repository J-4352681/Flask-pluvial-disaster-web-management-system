from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DateTime
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship
from app.db import db

from datetime import datetime

class Follow_up(db.Model):
    """Clase que representa los seguimientos de las quejas. Estos seguimientos recopilaran la informacion recogida sobre las quejas de los usuarios."""
    __tablename__ = "follow_ups"
    id = Column(Integer, primary_key=True)

    description = Column(String(255), nullable=false) 
    author_id = Column(Integer, ForeignKey('users.id'), nullable=false) # Debe existir un autor. Le autor sera un usuario de la app privada
    author = relationship("User", foreign_keys=author_id)
    creation_date = Column(DateTime(), default=datetime.now())

    complaint_id = Column(Integer, ForeignKey('complaints.id')) # Por ahora es una relacion solo de complaint a follow_up, se puede agregar back_populate para hacerlo bidireccional

    @classmethod
    def create(cls, description, author_id): #params
        """Crea un nuevo seguimiento."""
        new_fu = Follow_up(description, author_id)
        db.session.add(new_fu)
        db.session.commit()

    @classmethod
    def create_from_follow_up(cls, new_fu): #params
        """Crea un nuevo seguimiento a partir de un seguimiento."""
        db.session.add(new_fu)
        db.session.commit()

    @classmethod
    def delete(cls, id_param=None):
        """Elimina un seguimiento cuyo id coincida con el numero mandado como parametro."""
        fu_selected = Follow_up.query.filter_by(id=id_param).first()
        db.session.delete(fu_selected)
        db.session.commit()

    @classmethod
    def all(cls):
        """Devuelve todos los seguimientos cargados en el sistema"""
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id=None):
        """Devuelve el primer seguimiento cuyo id es igual al que se mando como parametros"""
        res = cls.query.filter(
            cls.id == id
        ).first()
        return res

    @classmethod
    def find_by_author_id(cls, author_id=None):
        """Devuelve todos los seguimientos cuyo id de autor sea igual al mandado como parametro"""
        res = cls.query.filter(
            cls.author_id == author_id
        ).all() 
        return res

    @classmethod
    def find_by_complaint_id(cls, complaint_id=None):
        """Devuelve todos los seguimientos cuyo id de queja sea igual al mandado como parametro"""
        res = cls.query.filter(
            cls.complaint_id == complaint_id
        ).all() 
        return res
    
    @classmethod
    def update(cls):
        """Actualiza la base de datos"""
        db.session.commit()

    def __init__(self, description=None, author_id=None):
        self.description = description
        self.author_id = author_id