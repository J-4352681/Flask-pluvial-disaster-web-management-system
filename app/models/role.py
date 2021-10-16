from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.orm import relationship
from app.db import db

from app.models import permit

"""Este modulo incluye todo la informacion relacionada al modelado de los roles, es capaz de devolver objetos "Role" y contiene funciones utiles para manejarlos."""

association_table_role_has_permit = Table('role_has_permit', db.Model.metadata,
    Column('role_id', ForeignKey('roles.id')),
    Column('permit_id', ForeignKey('permits.id'))
)
class Role(db.Model):
    """Clase que representa los roles de la base datos"""
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=false, unique=True)
    permits = relationship("Permit", secondary=association_table_role_has_permit)

    @classmethod
    def all(cls):
        """Devuelve todos los roles"""
        return cls.query.all()

    @classmethod
    def get_admin(cls):
        """Devuelve el rol con el trabajo del administrador. Si hay algun cambio a la reprecentacion del rol admin en la base datos solo se cambiara este metodo."""
        return get_by_name("admin")

    @classmethod
    def get_operator(cls):
        """Devuelve el rol con el trabajo del operador/a. Si hay algun cambio a la reprecentacion del rol operador/a en la base datos solo se cambiara este metodo."""
        return get_by_name("operator")

    @classmethod
    def get_by_name(cls, role_name):
        """Retorna el rol con nombre role_name"""
        return cls.query.get(
            cls.name == role_name
        )
    
    @classmethod
    def get_by_ids(cls, roles_id=[]):
        """Retorna todos los roles correspondientes a los id pasados por parametro"""
        return cls.query.filter(cls.id.in_(roles_id)).all()

    def __init__(self, name=None):
        self.name = name
