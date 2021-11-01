from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.orm import relationship
from app.db import db

from app.models import palette, color

"""Este modulo incluye todo la informacion relacionada al modelado de la configuracion de la app en base de datos."""

class Config(db.Model):
    """Clase que reprecenta las opciones de configuracion por defecto en la base datos"""
    __tablename__ = "config"
    id = Column(Integer, primary_key=True)
    elements_per_page = Column(Integer, nullable=false)
    sort_users= Column(String(30), nullable=false, default="first_name") # Criterio de ordenamiento por defecto de los usuarios
    sort_meeting_points= Column(String(30), nullable=false) # criterio de ordenamiento por defecto de los meeting points
    sort_flood_zones = Column(String(30), nullable=false) # Criterio de ordenamiento por defecto de zoans inundables
    
    palette_private_id = Column(Integer, ForeignKey("palettes.id"))
    palette_private = relationship("Palette", foreign_keys=[palette_private_id])
    palette_public_id = Column(Integer, ForeignKey("palettes.id"))
    palette_public = relationship("Palette", foreign_keys=[palette_public_id])

    @classmethod
    def get(cls):
        """Devuelve los datos de configuracion"""
        return cls.query.first()

    @classmethod
    def create(cls):
        """Crea una nueva configuracion por defecto si no existe una ya en el sistema"""
        configExists = Config.get()
        if ( not configExists ):
            new_conf = Config(elements_per_page=10, sort_users="username", sort_meeting_points="name")

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
    def modify_sort_criterion_flood_zones(cls, config, criteria):
        """actualiza el criterio por defecto de ordenamiento de las zonas inundables"""
        config.sort_flood_zones = criteria
        db.session.commit()

    @classmethod
    def newPrivatePalette(cls, config, newPalette):
        """reemplaza la paleta de colores privada por otra. Recibe una lista de objeto Color."""
        palette.Palette.newColor1(config.palette_private, newPalette[0])
        palette.Palette.newColor2(config.palette_private, newPalette[1])
        palette.Palette.newColor3(config.palette_private, newPalette[2])
        db.session.commit()
    
    @classmethod
    def newPublicPalette(cls, config, newPalette):
        """reemplaza la paleta de colores publica por otra. Recibe una lista de objeto Color."""
        palette.Palette.newColor1(config.palette_public, newPalette[0])
        palette.Palette.newColor2(config.palette_public, newPalette[1])
        palette.Palette.newColor3(config.palette_public, newPalette[2])
        db.session.commit()
    
    @classmethod
    def update(cls):
        """Actualiza los datos de la configuracion."""
        db.session.commit()

    @classmethod
    def translateCriteria(*criteria):
        """Traduce los campos de la base de datos a etiquetas en español"""
        names={"name":"Nombre","last_name":"Apellido","email":"Mail","username":"Nombre de usuario", "direction":"Direccion",
        "coordinates": "Coordenadas","state":"Estado","telephone": "Telefono"}
        return names[criteria[1]] # Se usa en [1] ya que criteria es una tupla

    def __init__(self, elements_per_page=None, sort_users=None, sort_meeting_points=None, sort_flood_zones=None):
        self.elements_per_page = elements_per_page
        self.sort_users = sort_users
        self.sort_meeting_points = sort_meeting_points
        self.sort_flood_zones = sort_flood_zones
        self.palette_private = palette.Palette()
        self.palette_public = palette.Palette()
        
