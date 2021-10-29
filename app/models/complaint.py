from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DateTime
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship
from app.db import db

from datetime import datetime

class Complaint(db.Model):
    """Clase que representa las quejas de los usuarios, de la aplicacion publica, en la aplicacion privada. El autor de la queja es un usuario de la aplicacion publica."""
    __tablename__ = "complaints"
    id = Column(Integer, primary_key=True)

    title = Column(String(255), nullable=false) 
    category = Column(String(255), nullable=false) 
    creation_date = Column(DateTime(), default=datetime.now())
    closure_date = Column(DateTime())
    description = Column(String(255), nullable=false) 
    coordinates = Column(JSON) # Json # Puede estar definida por una coordenada o un poligono # El PDF no indica que se aun dato necesario, aunque probablemente, funcionalmente termine siendolo
    state = Column(String(30)) # Opciones: Sin confirmar, En curso, Resuelta, Cerrada
    
    assigned_user_id = Column(Integer, ForeignKey('users.id')) # No es obligatorio que alguien este asignado, pero solo una persona deberia estar asignada.
    assigned_user = relationship("User", foreign_keys=assigned_user_id)

    author_first_name = Column(String(30), nullable=false) # Autor es un usuario de la aplicacion publica
    author_last_name = Column(String(30), nullable=false) 
    author_telephone = Column(String(30), nullable=false)
    author_email = Column(String(100), nullable=false)     
    
    follow_ups = relationship("Follow_up") # Literalmente seguimientos. Basicamente comentarios que recompilan mas informacion sobre la investigacion sobre la queja.

    @classmethod
    def create(cls, flood_zone_name, description, coordinates, state): #params
        """Crea una nueva queja en base a los datos dados."""
        new_c = Complaint(flood_zone_name, description, coordinates, state)
        db.session.add(new_c)
        db.session.commit()

    @classmethod
    def delete(cls, id_param=None):
        """Elimina una queja cuyo id coincida con el numero mandado como parametro."""
        c_selected = Complaint.query.filter_by(id=id_param).first()
        db.session.delete(c_selected)
        db.session.commit()

    @classmethod
    def all(cls):
        """Devuelve todas las quejas cargadas en el sistema"""
        return cls.query.all()
    
    @classmethod
    def find_by_id(cls, id=None):
        """Devuelve la primer queja cuyo id es igual al que se mando como parametro"""
        res = cls.query.filter(
            cls.id == id
        ).first()
        return res

    @classmethod
    def find_by_title(cls, title=None, excep=[]):
        """Devuelve la queja cuyo titulo sea igual al mandado como parametro"""
        users = cls.query.filter(
            cls.title.like('%'+title+'%'),
            cls.id.not_in(excep)
        ).all()
        return users

    @classmethod
    def find_by_state(cls, publico=None, excep=[]):
        """Devuelve todas las quejas cuyos estados coincidan con el String enviado como parametro. Opciones: Sin confirmar, En curso, Resuelta, Cerrada."""
        res = cls.query.filter(
            cls.state == publico,
            cls.id.not_in(excep)
        ).all()
        return res
    
    @classmethod
    def find_by_date_range(cls, first_date=None, last_date=None):
        """Devuelve todas las quejas cuyas fechas de creacion se encuentren entre la primera fecha y la ultima fecha del rango."""
        res = cls.query.filter(
            cls.creation_date >= first_date,
            cls.creation_date <= last_date
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