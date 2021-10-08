from flask import redirect, render_template, request, url_for, session, abort
from sqlalchemy.sql.expression import false, true
from app.models.user import User
from app.helpers.auth import authenticated
import app.db

# Protected resources
def index():
    if not authenticated(session):
        abort(401)

    users = User.all()
    
    return render_template("user/index.html", users=users)


def new():
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")

def userVerification( username, email):
    """Si no encuentra un usuario con el mismo username o email devuelve verdadero, si existe uno devuelve falso"""
    if ( not User.find_by_username( username )):
        if ( not User.find_by_email( email )):
            return true #Si no encuentra un usuario con el mismo username o email devuelve verdadero, si existe uno devuelve falso
    return false #Cambiar por un valor distinot si el problema fue user, otro si fue email

def create():
    """Se encarga de delegar la creacion del nuevo usuario al modelo, despues de verificar su validez con userVerification()"""
    if not authenticated(session):
        abort(401)

    if ( userVerification( request.form.username, request.form.email)): #Preguntar si de esta forma se usand los valores
        User.create(**request.form)
    else: abort(404) #Por ahora hace un abort, cambiar a un aviso en la misma pagina de cual se repite

    return redirect(url_for("user_index"))
