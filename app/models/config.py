from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.orm import relationship
from app.db import db

from app.models import color

"""Este modulo incluye todo la informacion relacionada al modelado de la configuracion de la app en base de datos."""

association_palet_has_colors = Table('palet_has_color', db.Model.metadata,
    Column('config_id', ForeignKey('config.id')),
    Column('color_id', ForeignKey('colors.id'))
)
class Config(db.Model):
    """Clase que representa los roles de la base datos"""
    __tablename__ = "config"
    id = Column(Integer, primary_key=True)
    elements_per_page = Column(Integer, nullable=false)
    sort_users= Column(String(30), nullable=false) # Criterio de ordenamiento por defecto de los usuarios
    sort_meeting_points= Column(String(30), nullable=false) # criterio de ordenamiento por defecto de los meeting points
    palette_private = relationship("Color", secondary=association_palet_has_colors)
    palette_public = relationship("Color", secondary=association_palet_has_colors)

    @classmethod
    def all(cls):
        """Devuelve los datos de configuracion"""
        return cls.query.first()

    def __init__(self, name=None, elements_per_page=None, sort_users=None, sort_meeting_points=None):
        self.name = name
        self.elements_per_page = elements_per_page
        self.sort_users = sort_users
        self.sort_meeting_points = sort_meeting_points
        
