from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship
from app.db import db

from app.resources.config import get as config_get

from string import ascii_lowercase
from random import choice as random_choice

class FloodZone(db.Model):
    """Clase que representa las zonas inundables en la base datos"""
    __tablename__ = "flood_zone"
    id = Column(Integer, primary_key=True)
    code = Column(String(30), unique=True, nullable=false) # Codigo de zona
    name = Column(String(30), nullable=false)
    coordinates = Column(JSON, nullable=false)
    state = Column(Boolean, default=True, nullable=false) # publicado o despublicado
    color = Column(String(7), nullable=false, default='#000000')



    @classmethod
    def create(cls, code, name, coordinates, state, color):
        """Crea una nueva zona inundable."""
        new_fz = FloodZone(code, name, coordinates, state, color)
        db.session.add(new_fz)
        db.session.commit()

    
    @classmethod
    def create_from_name_coord(cls, name, coord):
        num_chars = list(map(lambda x: str(x), range(9)))

        asciinum_chars = list(ascii_lowercase) + num_chars
        code = ''.join([random_choice(asciinum_chars) for i in range(5)])
        while(cls.find_by_code(code)): code = ''.join([random_choice(asciinum_chars) for i in range(5)])

        hex_chars = num_chars + list(ascii_lowercase)[:6]
        color = "#"+"".join([random_choice(hex_chars) for i in range(6)])

        new_fz = FloodZone(code, name, coord, True, color)
        db.session.add(new_fz)
        db.session.commit()

    
    @classmethod
    def create_from_flood_zone(cls, new_flood_zone):
        """Crea una nueva zona inundable con el objeto enviado por parámetro"""
        db.session.add(new_flood_zone)
        db.session.commit()


    @classmethod
    def delete_by_id(cls, id_param=None):
        """Elimina una zona inundable cuya id coincida con el numero mandado como parametro."""
        point_selected = cls.query.filter_by(id=id_param).first()
        db.session.delete(point_selected)
        db.session.commit()


    @classmethod
    def all(cls):
        """Devuelve todas las zonas inundables cargadas en el sistema"""
        return cls.query.all()


    @classmethod
    def all_paginated(cls, page):
        per_page = config_get().elements_per_page
        return cls.query.paginate(page=page, per_page=per_page)
    

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
        fzone = cls.query.filter(
            cls.name.like("%"+name+"%"),
            cls.id.not_in(excep)
        ).all()
        return fzone


    @classmethod
    def find_by_state(cls, publico=None, excep=[]):
        """Devuelve todas las zonas inundables publicas si el parametro publico=true o todos los no publicados si publico=false"""
        fzones = cls.query.filter(
            cls.state == publico,
            cls.id.not_in(excep)
        ).all()
        return fzones


    @classmethod
    def find_by_code(cls, code=None, excep=[]):
        """Devuelve todas las zonas inundables cuyo codigo sea igual al pasado por parametro"""
        fzone = cls.query.filter(
            cls.code == code,
            cls.id.not_in(excep)
        ).all()
        return fzone


    @classmethod
    def update(cls):
        """Actualiza la base de datos"""
        db.session.commit()


    def __init__(self, code=None, name=None, coordinates=None, state=None, color=None):
        self.code = code
        self.name = name
        self.coordinates = coordinates
        self.state = state
        self.color = color