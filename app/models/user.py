from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.orm import relationship
from app.db import db
from flask import session

from datetime import datetime
# from app.models import role
from app.models.role import Role
from app.models.permit import Permit

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
    def create(cls, **params):
        """Crea un nuevo usuario con los parametros mandados."""
        new_user = User(**params)
        db.session.add(new_user)
        db.session.commit()

    @classmethod
    def create_from_user(cls, new_user):
        """Crea un nuevo usuario con los parametros mandados."""
        db.session.add(new_user)
        db.session.commit()

    @classmethod
    def update(cls):
        """Actualiza los datos de un usuario enviado como parametro."""
        db.session.commit()

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
    def find_by_id(cls, id):
        return cls.query.get(id)
    
    @classmethod
    def get_user_roles_by_id(cls, id):
        return cls.find_by_id(id).roles

    @classmethod
    def find_by_email_and_password(cls, email=None, password=None):
        """Devuelve el primer usuario cuyo email y password son iguales a los que se mandaron como parametros"""
        user = cls.query.filter(
            cls.email == email and cls.password == password
        ).first()
        return user
    
    @classmethod
    def find_by_first_name(cls, first_name=None):
        """Devuelve el usuario cuyo first_name sea igual al mandado como parametro"""
        users = cls.query.filter(
            cls.first_name.like('%'+first_name+'%')
        )
        return users

    @classmethod
    def find_by_last_name(cls, last_name=None):
        """Devuelve el usuario cuyo last_name sea igual al mandado como parametro"""
        users = cls.query.filter(
            cls.last_name.like('%'+last_name+'%')
        )
        return users

    @classmethod
    def find_by_username(cls, username=None, excep=[]):
        """Devuelve el usuario cuyo nombre de usuario sea igual al mandado como parametro"""
        users = cls.query.filter(
            cls.username.like('%'+username+'%'),
            cls.id.not_in(excep)
        ).all()
        return users

    @classmethod
    def find_by_username_exact(cls, username=None, excep=[]):
        """Devuelve el usuario cuyo nombre de usuario sea igual al mandado como parametro"""
        users = cls.query.filter(
            cls.username.like(username),
            cls.id.not_in(excep)
        ).all()
        return users
    
    @classmethod
    def find_by_email(cls, email=None, excep=[]):
        """Devuelve el primer usuario cuyo email es igual al que se mando como parametro"""
        users = cls.query.filter(
            cls.email.like('%'+email+'%'),
            cls.id.not_in(excep)
        ).all()
        return users

    @classmethod
    def find_by_email_exact(cls, email=None, excep=[]):
        """Devuelve el primer usuario cuyo email es igual al que se mando como parametro"""
        users = cls.query.filter(
            cls.email.like(email),
            cls.id.not_in(excep)
        ).all()
        return users
    
    @classmethod
    def find_by_permits(cls, permits_names):
        """Devuelve todos los usuarios que tienen TODOS los permisos pasados por parámetro"""
        # users = db.session.query(User).join(User.roles).join(Role.permits).filter(Permit.name.in_(permits_names))
        users = db.session.query(User).join(User.roles).join(Role.permits).filter(Permit.name==permits_names)
        return users
    
    @classmethod
    def find_by_roles(cls, roles_names):
        """Devuelve todos los usuarios que tienen TODOS los roles pasados por parámetro"""
        # users = db.session.query(User).join(User.roles).filter(Role.name.in_(roles_names))
        users = db.session.query(User).join(User.roles).filter(Role.name==roles_names)
        return users
    
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
        """Asigna un rol a un usuario."""
        if role not in user.roles:
            user.roles.append(role)
            db.session.commit()

    @classmethod
    def assign_roles(cls, user=None, roles=[]):
        """Asigna un rol a un usuario."""
        roles_to_assign = filter(lambda r: r in user.roles, roles)
        map(lambda r: user.roles.append(r), roles)
        db.session.commit()
    
    @classmethod
    def unassign_role(cls, user=None, role=None):
        """Quita un rol de un usuario existente."""
        if role in user.roles:
            user.roles.remove(role)
            db.session.commit()

    def __init__(self, first_name=None, last_name=None, username=None, email=None, password=None, active=False, roles=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password #Los roles se pueden agregar a parte y el resto de atributos se agregan por defecto
        self.active = active
        self.roles = roles

    def is_admin(self):
        """Retorna si el usuario es admin"""
        return "admin" in self.roles # Esto no genera problemas? Los roles no son un nombre sino objetos

    def get_permits(self):
        """Retorna los permisos del usuario"""
        permits = set([
            permit.name for permits in map(lambda rol: rol.permits, self.roles) 
            for permit in permits
            ])
        return permits

    def assign_roles(self, roles=[]):
        """Asigna un rol al usuario."""
        roles_to_assign = filter(lambda r: r not in self.roles, roles)
        self.roles.extend(list(roles_to_assign))



