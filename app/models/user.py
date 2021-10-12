from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship
from app.db import db

from datetime import datetime
from role import Role

"""Este modulo incluye todo la informacion relacionada al modelo de usuarios, y como pedir informacion a la base de datos en relacion a estos"""
class User(db.Model):
    """Classe que representa los usuarios de la base datos"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)

    first_name = Column(String(30), nullable=false)
    last_name = Column(String(30), nullable=false)
    username = Column(String(30), nullable=false, unique=True)
    email = Column(String(30), nullable=false, unique=True) #¿Que tan largo puede ser un mail?
    password = Column(String(30), nullable=false)
    active = Column(Boolean, nullable=false, default=true) #Activo o bloqueado. Los usuarios de rol administrador no podran ser bloqueados
    roles = relationship("roles")
    created_at = Column(DateTime(), default=datetime.now()) #No es necesario pero puede ser util

    @classmethod
    def create(cls, params):
        """Crea un nuevo usuario con los parametros mandados"""
        new_user = User(params)
        db.session.add(new_user)
        db.session.commit()

    @classmethod
    def delete(cls, username_param=None):
        """Elimina un usuario cuyo username sea igual al enviado como parametro"""
        user_selected = User.query.filter_by(username=username_param).first()
        db.session.delete(user_selected)
        db.session.commit()

    @classmethod
    def all(cls):
        """Devuelve todos los usuarios"""
        return cls.query.all()

    @classmethod
    def find_by_email_and_password(cls, email=None, password=None):
        """Devuelve el primer usuario cuyo email y password son iguales a los que se mandaron como parametros"""
        user = cls.query.filter(
            cls.email == email and cls.password == password
        ).first()
        return user

    @classmethod
    def find_by_username(cls, username=None): #No funciona para coincidencias parciales
        """Devuelve el usuario cuyo nombre de usuario sea igual al mandado como parametro. No funciona con coincidencias parciales."""
        user = cls.query.filter(
            cls.username == username
        ).first() 
        return user
    
    @classmethod
    def find_by_email(cls, email=None):
        """Devuelve el primer usuario cuyo email es igual al que se mando como parametro"""
        user = cls.query.filter(
            cls.email == email
        ).first()
        return user
    
    @classmethod
    def find_all_active_or_blocked(cls, activo=None):
        """Devuelve todos los usuarios activos si el parametro activo=true o todos los usuarios bloqueados si el parametro activo=false"""
        res = cls.query.filter(
            cls.active == activo
        ).all() 
        return res #Devuelve todos los usuarios activos o bloqueados, cambie el nombre a res porque "users" es el nombre de la tabla y queria evitar confusion

    @classmethod
    def block_user(cls, username_param=None):
        """Bloquea un usuario cuyo username coincida con el parametro enviado. Si ya estaban bloqueados no hace nada. Usar "unblock_user" para desbloquear."""
        user_selected = User.query.filter_by(username=username_param).first()
        if ( ( user_selected.active ) and ( Role.get_admin() not in user_selected.roles )): #En el TP: "los únicos usuarios que no puedan ser bloqueados, sean aquellos con el rol Administrador"
            user_selected.active = false
            db.session.commit()

    @classmethod
    def unblock_user(cls, username_param=None):
        """Desbloquea un usuario cuyo username coincida con el parametro enviado. Si ya estaban activos no hace nada.  Usar "block_user" para bloquear."""
        user_selected = User.query.filter_by(username=username_param).first()
        if ( not user_selected.activo ):
            user_selected.active = true
            db.session.commit()

    @classmethod
    def assign_rol(cls, username_param=None, role_param=None):
        """Asigna un rol a un usuario existente."""
        user_selected = User.query.filter_by(username=username_param).first()
        user_selected.roles.append(role_param)
        db.session.commit()
    
    @classmethod
    def unassign_rol(cls, username_param=None, role_param=None):
        """Asigna un rol a un usuario existente."""
        user_selected = User.query.filter_by(username=username_param).first()
        if ( role_param in user_selected.roles):
            user_selected.roles.remove(role_param)
            db.session.commit()

    def __init__(self, first_name=None, last_name=None, username=None, email=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password #Los roles se pueden agregar a parte y el resto de atributos se agregan por defecto
