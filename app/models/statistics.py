from sqlalchemy import Column, Integer, true
from app.models.complaint import Complaint
from app.models.category import Category
from app.db import db

class Statistics(db.Model):
    __abstract__ = true

    @classmethod
    def count(cls):
        """Cuenta denuncias por categoria"""
        cats = Category.all()
        dic = {}
        for c in cats:
            cant_denuncias = len((Complaint.find_by_category(c.id)))
            dic[c.name] = {"denuncias": cant_denuncias }
        return dic