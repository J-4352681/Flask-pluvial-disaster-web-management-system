from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import false, true
from app.db import db

class Category(db.Model):
    """Clase que representa las categorias de denuncias en la aplicacion"""
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=false, unique=true)


    @classmethod
    def all(cls):
        """Devuelve todas las categorias que existen en el sistema."""
        return cls.query.all()


    @classmethod
    def create(cls, name):
        """Crea una nueva categoria con el nombre enviado."""
        new_cat = Category(name)
        db.session.add(new_cat)
        db.session.commit()


    @classmethod
    def find_by_id(cls, id):
        """Encuentra una categoria por id."""
        cat = cls.query.filter(
            cls.id == id
        ).first()
        return cat


    @classmethod
    def find_by_name(cls, name):
        """Encuentra una categoria por nombre."""
        cat = cls.query.filter(
            cls.name == name
        ).first()
        return cat


    def __init__(self, name=None):
        self.name = name