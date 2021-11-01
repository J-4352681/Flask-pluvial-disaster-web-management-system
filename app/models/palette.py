from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.orm import relationship
from app.db import db

from app.models import color

"""Este modulo incluye la repreentacion de la paleta de colores que recuerda el color principal de la aplicacion, el color secundario y el ."""

class Palette(db.Model):
    """Clase que representa las paletas de colores que se usaran en la app. color1 = color primario, color2 = colores secundario, color3 = color acento."""
    __tablename__ = "palettes"
    id = Column(Integer, primary_key=True)

    color1_id = Column(Integer, ForeignKey('colors.id'))
    color1 = relationship("Color", foreign_keys=color1_id)
    color2_id = Column(Integer, ForeignKey('colors.id'))
    color2 = relationship("Color", foreign_keys=color2_id)
    color3_id = Column(Integer, ForeignKey('colors.id'))
    color3 = relationship("Color", foreign_keys=color3_id)

    @classmethod
    def all(cls):
        """Devuelve las paletas que existen"""
        return cls.query.all()

    @classmethod
    def newColor1(cls, palette_param, newColor):
        """reemplaza un color en la paleta"""
        palette_param.color1 = newColor
        db.session.commit()

    @classmethod
    def newColor2(cls, palette_param, newColor):
        """reemplaza un color en la paleta"""
        palette_param.color2 = newColor
        db.session.commit()
    
    @classmethod
    def newColor3(cls, palette_param, newColor):
        """reemplaza un color en la paleta"""
        palette_param.color3 = newColor
        db.session.commit()

    def __init__(self):
        self.color1 = color.Color.find_by_id(1)
        self.color2 = color.Color.find_by_id(2)
        self.color3 = color.Color.find_by_id(3)
        
