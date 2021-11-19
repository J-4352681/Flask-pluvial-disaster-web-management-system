from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DateTime
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db import db
from app.models import category
from app.models import follow_up

class Complaint(db.Model):
    """Clase que representa las quejas de los usuarios, de la aplicacion publica, en la aplicacion privada. El autor de la queja es un usuario de la aplicacion publica."""
    __tablename__ = "complaints"
    id = Column(Integer, primary_key=True)

    title = Column(String(255), nullable=false) 
    creation_date = Column(DateTime(), default=datetime.now())
    closure_date = Column(DateTime())
    description = Column(String(255), nullable=false) 
    coordinates = Column(JSON) # Json # Puede estar definida por una coordenada o un poligono # El PDF no indica que se aun dato necesario, aunque probablemente, funcionalmente termine siendolo
    state = Column(String(30)) # Opciones: Sin confirmar, En curso, Resuelta, Cerrada

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category", foreign_keys=category_id) # Implementacion vieja: category = Column(String(255), nullable=false) 
    
    assigned_user_id = Column(Integer, ForeignKey('users.id')) # No es obligatorio que alguien este asignado, pero solo una persona deberia estar asignada.
    assigned_user = relationship("User", foreign_keys=[assigned_user_id])

    author_first_name = Column(String(30), nullable=false) # Autor es un usuario de la aplicacion publica
    author_last_name = Column(String(30), nullable=false) 
    author_telephone = Column(String(30), nullable=false)
    author_email = Column(String(100), nullable=false)     
    
    follow_ups = relationship("Follow_up") # Literalmente seguimientos. Basicamente comentarios que recompilan mas informacion sobre la investigacion sobre la queja.


    @classmethod
    def create(cls, title, description, coordinates, state, author_first_name, author_last_name, author_telephone, author_email): #params
        """Crea una nueva queja en base a los datos dados."""
        new_c = Complaint(title, description, coordinates, state, author_first_name, author_last_name, author_telephone, author_email)
        db.session.add(new_c)
        db.session.commit()

    
    @classmethod
    def create_from_complaint(cls, new_complaint):
        """Crea una nueva denuncia desde la pasada por parámetro"""
        db.session.add(new_complaint)
        db.session.commit()


    @classmethod
    def create_public(cls, title, description, coordinates, author_first_name, author_last_name, author_telephone, author_email, category_id): #params
        """Crea una nueva queja en base a los datos dados."""
        new_c = Complaint(title, description, coordinates, "Sin confirmar", author_first_name, author_last_name, author_telephone, author_email, category_id)
        db.session.add(new_c)
        db.session.commit()
        return new_c


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
    def close_complaint(cls, complaint_id):
        complaint = cls.find_by_id(complaint_id)
        if complaint: 
            complaint.closure_date = datetime.now()
            complaint.state = dict(Complaint.get_states())['Cerrada']
        db.session.commit()
    

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


    @classmethod
    def delete_by_id(cls, id=None):
        """Elimina una denuncia cuya id coincida con el numero mandado como parametro."""
        complaint_selected = cls.query.filter_by(id=id).first()
        db.session.delete(complaint_selected)
        db.session.commit()


    @classmethod
    def get_sorting_atributes(cls):
        """Devuelve los atributos para ordenar las listas"""
        return [("title", "Código"), ("creation_date", "Fecha de creación"), ("state", "Estado de la denuncia")]
    

    @classmethod
    def get_states(cls):
        "Retorna los estados en los que puede estar una denuncia"
        return [("Sin confirmar", "Sin confirmar"), ("En curso", "En curso"), ("Resuelta", "Resuelta"), ("Cerrada", "Cerrada")]


    @classmethod
    def all_by_assigned_user_id(cls, id):
        return cls.query.filter(
            cls.assigned_user_id == id
        ).all()


    def __init__(self, title=None, description=None, coordinates=None, state=None, author_first_name=None, author_last_name=None, author_telephone=None, author_email=None, category_id=None):
        self.title = title
        self.description = description
        self.coordinates = coordinates
        self.state = state
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.author_telephone = author_telephone
        self.author_email = author_email
        self.category_id = category_id
