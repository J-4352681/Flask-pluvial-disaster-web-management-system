from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship
from app.db import db

from datetime import datetime
from app.models import role

"""Este modulo incluye todo la informacion relacionada al modelo de usuarios, y como pedir informacion a la base de datos en relacion a estos"""

association_table_user_has_role = Table('user_has_role', db.Model.metadata,
    Column('user_id', ForeignKey('users.id')),
    Column('role_id', ForeignKey('roles.id'))
)
class User(db.Model):
    """Classe que representa los usuarios de la base datos"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)

    first_name = Column(String(30), nullable=false)
    last_name = Column(String(30), nullable=false)
    username = Column(String(30), nullable=false, unique=True)
    email = Column(String(30), nullable=false, unique=True)
    password = Column(String(30), nullable=false)
    active = Column(Boolean, nullable=false, default=true) # Los usuarios de rol administrador no podran ser bloqueados
    roles = relationship("Role", secondary=association_table_user_has_role) 
    created_at = Column(DateTime(), default=datetime.now()) # No es necesario pero puede ser util

    @classmethod
    def create(cls, params):
        """Crea un nuevo usuario con los parametros mandados."""
        new_user = User(params)
        db.session.add(new_user)
        db.session.commit()

    @classmethod
    def modify(cls, user=None):
        """Modifica los datos de un usuario enviado como parametro."""

    @classmethod
    def delete(cls, user=None):
        """Elimina un usuario enviado como parametro."""
        db.session.delete(user)
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
    def find_by_username(cls, username=None): # No funciona para coincidencias parciales
        """Devuelve el usuario cuyo nombre de usuario sea igual al mandado como parametro. No funciona con coincidencias parciales."""
        user = cls.query.filter(
            cls.username == username
        ).first() 
        return user
    
    @classmethod
    def find_by_email(cls, email=None): # No funciona para coincidencias parciales
        """Devuelve el primer usuario cuyo email es igual al que se mando como parametro"""
        user = cls.query.filter(
            cls.email == email
        ).first()
        return user
    
    @classmethod
    def find_all_active_or_blocked(cls, activo=None): # Ta dudoso este metodo jaja
        """Devuelve todos los usuarios activos si el parametro activo=true o todos los usuarios bloqueados si el parametro activo=false"""
        res = cls.query.filter(
            cls.active == activo
        ).all() 
        return res #Devuelve todos los usuarios activos o bloqueados, cambie el nombre a res porque "users" es el nombre de la tabla y queria evitar confusion

    @classmethod
    def block(cls, user=None):
        """Bloquea un usuario enviado como parametro. Si ya estaban bloqueados no hace nada. Usar "unblock" para desbloquear."""
        if user.active:
            user.active = false
            db.session.commit()

    @classmethod
    def unblock(cls, user=None):
        """Desbloquea un usuario enviado como parametro. Si ya estaban activos no hace nada. Usar "block" para bloquear."""
        if not user.active:
            user.active = true
            db.session.commit()

    @classmethod
    def assign_role(cls, user=None, role=None):
        """Asigna un rol a un usuario existente."""
        if role not in user.roles:
            user.roles.append(role)
            db.session.commit()
    
    @classmethod
    def unassign_role(cls, user=None, role=None):
        """Quita un rol de un usuario existente."""
        if role in user.roles:
            user.roles.remove(role)
            db.session.commit()

    def __init__(self, first_name=None, last_name=None, username=None, email=None, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password #Los roles se pueden agregar a parte y el resto de atributos se agregan por defecto

    def is_admin(self):
        return "admin" in self.roles