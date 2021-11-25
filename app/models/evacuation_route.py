from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from app.db import db
from app.resources.config import Config

class EvacuationRoute(db.Model):
    """Clase que representa los recorridos de evacuacion guardados en la aplicacion"""
    __tablename__ = "evacuation_routes"
    id = Column(Integer, primary_key=True)

    name = Column(String(30), unique=True, nullable=False)
    description = Column(String(255), nullable=false) 
    coordinates = Column(JSON, nullable=false) # Json
    state = Column(Boolean, default=True, nullable=false) # publicado o despublicado

    @classmethod
    def create(cls, name, description, coordinates, state): #params
        """Crea un nuevo recorrido de evacuacion."""
        new_evroute = EvacuationRoute(name, description, coordinates, state)
        db.session.add(new_evroute)
        db.session.commit()

    @classmethod
    def create_from_evacuation_route(cls, new_evacuation_route):
        """Crea una nueva ruta de evacuacion con el objeto enviado por parámetro"""
        db.session.add(new_evacuation_route)
        db.session.commit()

    @classmethod
    def delete(cls, id_param=None):
        """Elimina un recorrido de evacuacion cuyo id coincida con el numero mandado como parametro."""
        er_selected = EvacuationRoute.query.filter_by(id=id_param).first()
        db.session.delete(er_selected)
        db.session.commit()

    @classmethod
    def all(cls):
        """Devuelve todos los recorridos de evacuacion cargados en el sistema"""
        return cls.query.all()
    
    @classmethod
    def all_paginated(cls, page):
        per_page = Config.get().elements_per_page
        return cls.query.paginate(page=page, per_page=per_page)
    
    @classmethod
    def allPublic(cls):
        """Devuelve todos los recorridos de evacuacion publicos"""
        res = cls.query.filter(
            cls.state == True
        ).all() 
        return res
    
    @classmethod
    def allNotPublic(cls):
        """Devuelve todos los recorridos de evacuacion no publicos"""
        res = cls.query.filter(
            cls.state == False
        ).all() 
        return res
    
    @classmethod
    def find_by_id(cls, id=None):
        """Devuelve el primer recorrido de evacuacion id cuyo id es igual al que se mando como parametros"""
        res = cls.query.filter(
            cls.id == id
        ).first()
        return res

    @classmethod
    def find_by_name(cls, name=None, excep=[]):
        """Devuelve la ruta de evacuacion cuyo nombre sea igual al mandado por parametro"""
        res = cls.query.filter(
            cls.name == name,
            cls.id.not_in(excep)
        ).first() 
        return res

    @classmethod
    def find_by_state(cls, publico=None, excep=[]):
        """Devuelve todos los recorrido de evacuacion publicos si el parametro publico=true o todos los no publicados si publico=false"""
        res = cls.query.filter(
            cls.state == publico,
            cls.id.not_in(excep)
        ).all()
        return res
    
    @classmethod
    def update(cls):
        """Actualiza la base de datos"""
        db.session.commit()

    @classmethod
    def get_sorting_atributes(cls):
        """Devuelve los atributos para ordenar las listas"""
        return [("name", "Nombre"), ("state", "Estado")]

    def __init__(self, name=None, description=None, coordinates=None, state=None):
        self.name = name
        self.description = description
        self.coordinates = coordinates
        self.state = state