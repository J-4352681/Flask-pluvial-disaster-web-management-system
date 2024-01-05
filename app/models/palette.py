from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.expression import false, true
from sqlalchemy.orm import relationship
from app.db import db

import re


"""Este modulo incluye la repreentacion de la paleta de colores que recuerda el color principal de la aplicacion, el color secundario y el ."""

class Palette(db.Model):
    """Clase que representa las paletas de colores que se usaran en la app. color1 = color primario, color2 = colores secundario, color3 = color acento."""
    __tablename__ = "palettes"
    id = Column(Integer, primary_key=True)

    name = Column(String(30), nullable=false, unique=True)

    color1 = Column(String(7), nullable=false, default='#000000')
    color2 = Column(String(7), nullable=false, default='#000000')
    color3 = Column(String(7), nullable=false, default='#000000')

    _rgbstring = re.compile(r'#[a-fA-F0-9]{6}$')

    @classmethod
    def all(cls):
        """Devuelve las paletas que existen"""
        return cls.query.all()

    @classmethod
    def _isrgbcolor(cls, value):
        return bool(_rgbstring.match(value))

    @classmethod
    def _checkColorOrRaise(cls, color):
        if not _isrgbcolor(newColor): raise Exception("Color inválido")

    @classmethod
    def newColor1(cls, palette_param, newColor):
        """reemplaza un color en la paleta"""
        _checkColorOrRaise(newColor)
        palette_param.color1 = newColor
        db.session.commit()

    @classmethod
    def newColor2(cls, palette_param, newColor):
        """reemplaza un color en la paleta"""
        _checkColorOrRaise(newColor)
        palette_param.color2 = newColor
        db.session.commit()

    @classmethod
    def newColor3(cls, palette_param, newColor):
        """reemplaza un color en la paleta"""
        _checkColorOrRaise(newColor)
        palette_param.color3 = newColor
        db.session.commit()

    @classmethod
    def get_sorting_atributes(cls):
        """Devuelve los atributos para ordenar las listas"""
        return [("name","Nombre")]

    @classmethod
    def all_paginated(cls, page):
        per_page = Config.get().elements_per_page
        return cls.query.paginate(page=page, per_page=per_page)

    @classmethod
    def find_by_name(cls, name=None, excep=[]):
        """Devuelve la paleta cuyo nombre sea igual al enviado como parametro"""
        palettes = cls.query.filter(
            cls.name.like("%"+name+"%"),
            cls.id.not_in(excep)
        ).all()
        return palettes

    @classmethod
    def find_by_id(cls, id=None):
        """Devuelve la primer paleta de id cuyo id es iguales al que se envio como parametros"""
        palette = cls.query.filter(
            cls.id == id
        ).first()
        return palette

    @classmethod
    def update_data(cls, palette=None, name=None, color1=None, color2=None, color3=None):
        palette.name = name
        palette.color1 = color1
        palette.color2 = color2
        palette.color3 = color3

    @classmethod
    def update(cls):
        """Actualiza la base de datos"""
        db.session.commit()

    # def __init__(self):
    #     self.color1 = color.Color.find_by_id(1)
    #     self.color2 = color.Color.find_by_id(2)
    #     self.color3 = color.Color.find_by_id(3)
