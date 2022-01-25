from pymysql import Date
from sqlalchemy import true
from app.models.complaint import Complaint
from app.models.category import Category
from app.models.user import User
from app.db import db


class Statistics(db.Model):
    __abstract__ = true

    @classmethod
    def count(cls):
        """Cuenta denuncias por categoria"""
        cats = Category.all()
        dic = {}
        for c in cats:
            cant_denuncias = len(Complaint.find_by_category(c.id))  
            dic[c.name] = {"denuncias": cant_denuncias}
        return dic

    @classmethod
    def count_by_user(cls):
        """Cuenta denuncias por usuario asignado"""
        users = User.all_actives()
        dic = {}
        for u in users:
            cant_denuncias = len(Complaint.all_by_assigned_user_id(u.id))  
            dic[u.username] = {"denuncias": cant_denuncias}
        return dic

    
