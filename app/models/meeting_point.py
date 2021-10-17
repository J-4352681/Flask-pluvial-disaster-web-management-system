from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from app.db import db

class Meeting_Point(db.Model):
    """Clase que representa los puntos de encuentro en la base datos"""
    __tablename__ = "meeting_points"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=false)
    direction = Column(String(100), nullable=false)
    coordinates = Column(String(100), nullable=false)
    state = Column(Boolean, default=True, nullable=false) # publicado o despublicado
    telephone = Column(String(30), nullable=false)
    email = Column(String(100), nullable=false)

    @classmethod
    def create(cls, name, direction, coordinates, telephone, email): #params
        """Crea un nuevo punto de encuentro."""
        new_user = Meeting_Point(name, direction, coordinates, telephone, email)
        db.session.add(new_user)
        db.session.commit()

    @classmethod
    def delete(cls, id_param=None):
        """Elimina un punto de encuentro cuyo nombre coincide con el id mandado como parametro."""
        point_selected = Meeting_Point.query.filter_by(id=id_param).first()
        db.session.delete(point_selected)
        db.session.commit()

    @classmethod
    def all(cls):
        """Devuelve todos los puntos de encuentro"""
        return cls.query.all()
    
    @classmethod
    def allPublic(cls):
        """Devuelve todos los puntos de encuentro publicos"""
        res = cls.query.filter(
            cls.state == True
        ).all() 
        return res
    
    @classmethod
    def allNotPublic(cls):
        """Devuelve todos los puntos de encuentro publicos"""
        res = cls.query.filter(
            cls.state == false
        ).all() 
        return res
    
    @classmethod
    def find_by_name(cls, name=None, excep=[]):
        """Devuelve el punto de encuentro cuyo nombre sea igual al mandado como parametro"""
        users = cls.query.filter(
            cls.name.like('%'+name+'%'),
            cls.id.not_in(excep)
        ).all()
        return users

    @classmethod
    def find_by_state(cls, publico=None, excep=[]):
        """Devuelve todos los puntos de encuentro publicos si el parametro publico=true o todos los no publicados si publico=false"""
        users = cls.query.filter(
            cls.state == publico,
            cls.id.not_in(excep)
        ).all()
        return users

    @classmethod
    def find_by_id(cls, id=None):
        """Devuelve el primer punto de id cuyo id es iguales al que se mando como parametros"""
        user = cls.query.filter(
            cls.id == id
        ).first()
        return user
    
    @classmethod
    def update(cls):
        db.session.commit()

    def __init__(self, name=None, direction=None, coordinates=None, telephone=None, email=None):
        self.name = name
        self.direction = direction
        self.coordinates = coordinates
        self.telephone = telephone
        self.email = email
        # self.state = true