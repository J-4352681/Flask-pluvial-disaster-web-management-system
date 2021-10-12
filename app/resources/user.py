from flask import redirect, render_template, request, url_for, session, abort
from sqlalchemy.sql.expression import false, true
from app.models.user import User
from app.helpers.auth import authenticated, authorized
import app.db

# Protected resources
def index():
    if not authenticated(session):
        abort(401)

    users = User.all()
    
    return render_template("user/index.html", users=users)


def new():
    """devuelve el template para crear un nuevo usuario."""
    if not authenticated(session):
        abort(401)

    return render_template("user/new.html")

def user_verification( username, email):
    """Si no encuentra un usuario con el mismo username o email devuelve verdadero, si existe uno devuelve falso"""
    if ( not User.find_by_username( username )):
        if ( not User.find_by_email( email )):
            return true #Si no encuentra un usuario con el mismo username o email devuelve verdadero, si existe uno devuelve falso
    return false #Cambiar por un valor distinot si el problema fue user, otro si fue email

def create():
    """Se encarga de delegar la creacion del nuevo usuario al modelo, despues de verificar su validez con userVerification()"""
    if not authenticated(session):
        abort(401)

    if ( user_verification( request.form.username, request.form.email)): #Preguntar si de esta forma se usand los valores
        User.create(**request.form)
    else: abort(404) #Por ahora hace un abort, cambiar a un aviso en la misma pagina de cual se repite

    return redirect(url_for("user_index"))

def block_user( username ):
    """Cambiara el estado de un usuario de "activo" a "bloqueado". Los usuarios administradores no pueden ser bloqueados."""
    if not authenticated(session):
        abort(401)
    #Comprobar permisos adecuados 
    if not authorized(session, "user_block_user"):
        abort(401)

    User.block_user(username)



def unblock_user( username ):
    """Cambiara el estado de un usuario de "bloqueado" a "activo". Los usuarios administradores no pueden ser bloqueados."""
    if not authenticated(session):
        abort(401)
    #Comprobar permisos adecuados 
    if not authorized(session, "user_unblock_user"):
        abort(401)

    User.unblock_user(username)
    


def assign_rol( username, role ):
    """Le otorgara un nuevo rol a un usuario existende, determinado por su username."""
    if not authenticated(session):
        abort(401)
    #Comprobar permisos adecuados 
    if not authorized(session, "user_assign_rol"):
        abort(401)

    User.assign_rol(username, role)



