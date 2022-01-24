from sqlalchemy import Column, Integer, true
from app.models.complaint import Complaint
from app.models.category import Category
from app.db import db


class Statistics(db.Model):
    __abstract__ = true

    @classmethod
    def count(cls, model):
        """Cuenta denuncias por el atributo del modelo enviado por parametro"""
        collection = model.all()
        # si model es Category, Category.__name__.lower() = category
        method_name = f'find_by_{model.__name__.lower()}'
        method = getattr(Complaint, method_name)
        dic = {}
        for c in collection:
            cant_denuncias = len(method(c.id))  # aca ejecuto el metodo
            dic[c.name] = {"denuncias": cant_denuncias}
        return dic
