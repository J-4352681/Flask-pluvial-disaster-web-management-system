from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.expression import false, true

from app.models.user import User
from app.helpers.auth import assert_permit
from app.helpers.user import username_or_email_already_exist
from app.helpers.filter import apply_filter


# Protected resources
def index():
    """Muestra la lista de usuarios."""
    assert_permit(session, "user_index")

    query = {k: v for k, v in request.args.items() if v != ''}

    if query == {}:
        users = User.all()
    else:
        # print(getattr(User, list(request.args.keys())[2]))
        users = apply_filter(User, query)
    
    return render_template("user/index.html", users=users, filters={
        "find_by_email": "Email",
        "find_by_first_name": "Nombre", 
        "find_by_last_name": "Apellido", 
        "find_by_roles": "Roles",
        "find_by_permits": "Permisos"
        })


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

def unassign_role(user, role):
    """Le quita un rol a un usuario existente."""
    assert_permit(session, "user_unassign_rol")
    User.unassign_role(user, role)
    return redirect(url_for("user_index"))

def modify(user):
    """Modifica los datos de un usuario."""