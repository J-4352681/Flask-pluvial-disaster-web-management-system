from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from app.db import db

class Evacuation_route(db.Model):
    """Clase que representa los recorridos de evacuacion guardados en la aplicacion"""
    __tablename__ = "evacuation_routes"
    id = Column(Integer, primary_key=True)
    flood_zone_name = Column(String(30), ForeignKey('flood_zones.name')) # NOMBRE DE LA ZONA INUNDABLE
    description = Column(String(255), nullable=false) 
    coordinates = Column(JSON, nullable=false) # Json
    state = Column(Boolean, default=True, nullable=false) # publicado o despublicado

    @classmethod
    def create(cls, flood_zone_name, description, coordinates, state): #params
        """Crea un nuevo recorrido de evacuacion."""
        new_er = Evacuation_route(flood_zone_name, description, coordinates, state)
        db.session.add(new_er)
        db.session.commit()

    @classmethod
    def delete(cls, id_param=None):
        """Elimina un recorrido de evacuacion cuyo id coincida con el numero mandado como parametro."""
        er_selected = Evacuation_route.query.filter_by(id=id_param).first()
        db.session.delete(er_selected)
        db.session.commit()

    @classmethod
    def all(cls):
        """Devuelve todos los recorridos de evacuacion cargados en el sistema"""
        return cls.query.all()
    
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
    def find_by_zone_name(cls, zone_name=None):
        """Devuelve todos los recorrido de evacuacion cuyo nombre de zona sea igual al mandado como parametro"""
        res = cls.query.filter(
            cls.flood_zone_name == zone_name
        ).all() 
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

    def __init__(self, flood_zone_name=None, description=None, coordinates=None, state=None):
        self.flood_zone_name = flood_zone_name
        self.description = description
        self.coordinates = coordinates
        self.state = state