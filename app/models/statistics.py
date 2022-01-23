from typing import Dict
from unicodedata import category
from flask import jsonify
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from app.db import db
from app.models.complaint import Complaint
from app.models.category import Category
from app.schemas.category import CategoryFetchSchema

class Statistics(db.Model):
    """Clase que representa las estadisticas en la base datos."""
    __tablename__ = "statistics"
    id = Column(Integer, primary_key=true)
    name = Column(String(30), nullable=false)
    data = Column(String(255), nullable=false)

    @classmethod
    def create(cls, name, data):
        """Crea una nueva estadistica."""
        new_s = cls(name, data)
        db.session.add(new_s)
        db.session.commit()
    
    @classmethod
    def delete(cls, id_param=None):
        """Elimina una estadistica cuyo id coincida con el numero mandado como parametro."""
        s = Statistics.query.filter_by(id=id_param).first()
        db.session.delete(s)
        db.session.commit()


    @classmethod
    def all(cls):
        """Devuelve todas las estadisticas del sistema"""
        return cls.query.all()

    @classmethod
    def count(cls):
        """Cuenta denuncias por categoria"""
        #cats = CategoryFetchSchema(many=True).dump(Category.all())
        cats = Category.all()
        dict = {}
        for c in cats:
            denun = Complaint.find_by_category(c.id)
            n=0
            for d in denun:
                n=n+1
            dict[c.name] = { "denuncias": n}
        return dict 

    def __init__(self, name=None, data=None): #pa que sirve esto?? also que es cls???
        self.name = name
        self.data = data