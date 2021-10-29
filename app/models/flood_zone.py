from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from app.db import db

class Flood_zone(db.Model):
    """Clase que representa las zonas inundables en la base datos"""
    __tablename__ = "flood_zones"
    id = Column(Integer, primary_key=True)
    code = Column(Integer, unique=true) # Codigo de zona
    name = Column(String(30), nullable=false)
    coordinates = Column(JSON, nullable=false) # Json
    state = Column(Boolean, default=True, nullable=false) # publicado o despublicado
    color = Column(String(30), nullable=false) # Color del mapa

    @classmethod
    def create(cls, code, name, coordinates, state, color): #params
        """Crea una nueva zona inundable."""
        new_mp = Flood_zone(code, name, coordinates, state, color)
        db.session.add(new_mp)
        db.session.commit()

    @classmethod
    def delete(cls, id_param=None):
        """Elimina una zona inundable cuya id coincida con el numero mandado como parametro."""
        point_selected = Flood_zone.query.filter_by(id=id_param).first()
        db.session.delete(point_selected)
        db.session.commit()

    @classmethod
    def all(cls):
        """Devuelve todas las zonas inundables cargadas en el sistema"""
        return cls.query.all()
    
    @classmethod
    def allPublic(cls):
        """Devuelve todas las zonas inundables publicas"""
        res = cls.query.filter(
            cls.state == True
        ).all() 
        return res
    
    @classmethod
    def allNotPublic(cls):
        """Devuelve todas las zonas inundables no publicas"""
        res = cls.query.filter(
            cls.state == False
        ).all() 
        return res
    
    @classmethod
    def find_by_id(cls, id=None):
        """Devuelve la primer zona inundable id cuyo id es iguales al que se mando como parametros"""
        user = cls.query.filter(
            cls.id == id
        ).first()
        return user

    @classmethod
    def find_by_name(cls, name=None, excep=[]):
        """Devuelve la zona inundable cuyo nombre sea igual al mandado como parametro"""
        users = cls.query.filter(
            cls.name.like('%'+name+'%'),
            cls.id.not_in(excep)
        ).all()
        return users

    @classmethod
    def find_by_state(cls, publico=None, excep=[]):
        """Devuelve todas las zonas inundables publicas si el parametro publico=true o todos los no publicados si publico=false"""
        users = cls.query.filter(
            cls.state == publico,
            cls.id.not_in(excep)
        ).all()
        return users
    
    @classmethod
    def update(cls):
        db.session.commit()

    def __init__(self, code=None, name=None, coordinates=None, state=None, color=None):
        self.code = code
        self.name = name
        self.coordinates = coordinates
        self.state = state
        self.color = color