from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.expression import false, true

from app.models.user import User
from app.models.role import Role
from app.helpers.auth import assert_permit
from app.helpers.user import username_or_email_already_exist
from app.helpers.filter import Filter
from app.db import db

from app.forms.user_forms import UserModificationForm, UserCreationForm
from app.forms.filter_forms import UserFilter
from app.resources.generic import ModificationTemplateParamsWrapper


# Protected resources
def index():
    """Muestra la lista de usuarios."""
    assert_permit(session, "user_index")

    filt = Filter(UserFilter, User, request.args)
        
    return render_template("user/index.html", form=filt.form, users=filt.get_query())


def new():
    """Devuelve el template para crear un nuevo usuario."""
    assert_permit(session, "user_new")
    user = User()
    form = UserCreationForm(obj=user)

    if form.validate_on_submit():
        create(form, user)
        return redirect(url_for("user_index"))
    else:
        param_wrapper = ModificationTemplateParamsWrapper(
            form, url_for("user_new"), "Usuario", "un nuevo usuario"
        )

        return render_template("generic/edit_item.html", param_wrapper=param_wrapper)

def create(form, user):
    """Verifica que los datos unicos no esten repetidos antes de crear un nuevo usuario con los datos pasados por request."""
    assert_permit(session, "user_create")

    # user_attrs["roles"] = Role.get_by_ids([int(i) for i in user_attrs["roles"]])
    form.populate_obj(user)
    User.create_from_user(user)

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
    session["user_permits"] = user.get_permits()
    return redirect(url_for("user_index"))

def unassign_role(user, role):
    """Le quita un rol a un usuario existente."""
    assert_permit(session, "user_unassign_rol")
    User.unassign_role(user, role)
    session["user_permits"] = user.get_permits()
    return redirect(url_for("user_index"))

def modify(user_id):
    """Modifica los datos de un usuario."""
    assert_permit(session, "user_modify")
    user = User.find_by_id(user_id)
    form = UserModificationForm(obj=user)

    if form.validate_on_submit():
        form.populate_obj(user)
        User.update()
        return redirect(url_for('user_index'))
    
    param_wrapper = ModificationTemplateParamsWrapper(
        form, url_for("user_modify", user_id=user.id), "Usuario", user.first_name, user.id
    )
    
    return render_template("generic/edit_item.html", param_wrapper=param_wrapper)
    
    
