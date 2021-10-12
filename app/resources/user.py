from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.expression import false, true
from app.models.user import User
from app.helpers.auth import assert_permit, authenticated
from app.helpers.user import username_already_exists, username_or_email_already_exist
import app.db

# Protected resources
def index():
    """Muestra la lista de usuarios."""
    assert_permit(session, "user_index")

    users = User.all()
    return render_template("user/index.html", users=users)


def new():
    """Devuelve el template para crear un nuevo usuario."""
    assert_permit(session, "user_new")

    return render_template("user/new.html")

def create():
    """Verifica que los datos unicos no esten repetidos antes de crear un nuevo usuario con los datos pasados por request."""
    assert_permit(session, "user_create")

    if not username_or_email_already_exist(request.form.username, request.form.email):
        User.create(**request.form)
        return redirect(url_for("user_index"))

def block(user):
    """Cambiara el estado de un usuario de "activo" a "bloqueado". Los usuarios administradores no pueden ser bloqueados."""
    if(not user.is_admin()):
        assert_permit(session, "user_block")
        User.block(user)
        return redirect(url_for("user_index"))
    else:
        flash("El usuario seleccionado no puede ser bloqueado.")

def unblock(user):
    """Cambiara el estado de un usuario de "bloqueado" a "activo". Los usuarios administradores no pueden ser bloqueados."""
    assert_permit(session, "user_unblock")
    User.unblock(user)
    return redirect(url_for("user_index"))

def assign_role(user, role):
    """Le otorgara un nuevo rol a un usuario existente, determinado por su user."""
    assert_permit(session, "user_assign_rol")
    User.assign_role(user, role)
    return redirect(url_for("user_index"))

def unassing_role(user, role):
    """Le quita un rol a un usuario existente."""
    assert_permit(session, "user_unassign_rol")
    User.unassign_role(user, role)
    return redirect(url_for("user_index"))

def modify(user):
    """Modifica los datos de un usuario."""