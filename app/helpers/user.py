from sqlalchemy.sql.expression import false, true
from flask import flash

from app.models.user import User


def username_or_email_already_exist(username, email):
    """Chequea que el nombre de usuario e email esten ya en uso"""
    return username_already_exists(username) or email_already_exists(email)

def username_already_exists(username):
    """Chequea que el username pasado como parametro exista en la BD"""
    if User.find_by_username(username):
        flash("Ese nombre de usuario ya existe.")
        return true
    
    return false

def email_already_exists(email):
    """Chequea que el username pasado como parametro exista en la BD"""
    if User.find_by_email(email):
        flash("Ese email ya existe.")
        return true
    
    return false