from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.orm import relationship
from app.db import db

from app.models import color

"""Este modulo incluye todo la informacion relacionada al modelado de la configuracion de la app en base de datos."""

association_private_palett_has_color = Table('private_palett_has_color', db.Model.metadata,
    Column('config_id', ForeignKey('config.id')),
    Column('color_id', ForeignKey('colors.id'))
)
association_public_palett_has_color = Table('public_palett_has_color', db.Model.metadata,
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
    palette_private = relationship("Color", secondary=association_private_palett_has_color)
    palette_public = relationship("Color", secondary=association_public_palett_has_color)

    @classmethod
    def get(cls):
        """Devuelve los datos de configuracion"""
        return cls.query.first()

    @classmethod
    def create(cls):
        """Crea una nueva configuracion por defecto si no existe una ya en el sistema"""
        configExists = Config.get()
        if ( not configExists ):
            new_conf = Config(elements_per_page=10, sort_users='username', sort_meeting_points='name')
            db.session.add(new_conf)
            db.session.commit()

    @classmethod
    def modifyElementsPerPage(cls, config, cant):
        """actualiza la cantidad de elementos por pagina."""
        config.elements_per_page = cant
        db.session.commit()

    @classmethod
    def modifySortCriterionUser(cls, config, criteria):
        """actualiza el criterio por defecto de ordenamiento de los usuarios"""
        config.sort_users = criteria
        db.session.commit()

    @classmethod
    def modifySortCriterionMeetingPoints(cls, config, criteria):
        """actualiza el criterio por defecto de ordenamiento de los puntos de encuentro"""
        config.sort_meeting_points = criteria
        db.session.commit()

    @classmethod
    def newPrivatePalette(cls, config, newPalette):
        """reemplaza la paleta de colores privada por otra"""
        config.palette_private = newPalette
        db.session.commit()
    
    @classmethod
    def newPublicPalette(cls, config, newPalette):
        """reemplaza la paleta de colores publica por otra"""
        config.palette_public = newPalette
        db.session.commit()

    def __init__(self, elements_per_page=None, sort_users=None, sort_meeting_points=None):
        self.elements_per_page = elements_per_page
        self.sort_users = sort_users
        self.sort_meeting_points = sort_meeting_points
        
