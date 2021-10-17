from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.expression import false, true

from app.models.user import User
from app.models.role import Role
from app.helpers.auth import assert_permit
from app.helpers.user import username_or_email_already_exist
from app.helpers.filter import Filter
from app.models.role import Role

from app.forms.user_forms import UserCreationForm, UserModificationForm
from app.forms.filter_forms import UserFilter
from app.resources.generic import FormTemplateParamsWrapper

from app.resources.config import getSortCriterionUsers

# Protected resources
def index(page=None):
    """Muestra la lista de usuarios."""
    assert_permit(session, "user_index")

    filt = Filter(UserFilter, User, request.args)
        
    return render_template("user/index.html", form=filt.form, users=filt.get_query(page))

def new():
    """Devuelve el template para crear un nuevo usuario."""
    assert_permit(session, "user_new")
    user = User()
    form = UserCreationForm(obj=user)

    if form.validate_on_submit():
        create(form, user)
        return redirect(url_for("user_index"))
    else:
        param_wrapper = FormTemplateParamsWrapper(
            form, url_for("user_new"), "creación", url_for('user_index'), "Usuario", "un nuevo usuario"
        )

        return render_template("generic/base_form.html", param_wrapper=param_wrapper)

def create(form, user):
    """Verifica que los datos unicos no esten repetidos antes de crear un nuevo usuario con los datos pasados por request."""
    assert_permit(session, "user_create")

    # user_attrs["roles"] = Role.get_by_ids([int(i) for i in user_attrs["roles"]])
    form.populate_obj(user)
    User.create_from_user(user)

def block(user_id):
    """Cambiara el estado de un usuario de "activo" a "bloqueado". Los usuarios administradores no pueden ser bloqueados."""
    user = User.find_by_id(user_id)
    if not user.is_admin():
        assert_permit(session, "user_block")
        User.block(user)
    else:
        flash("El usuario seleccionado no puede ser bloqueado.")
    
    return redirect(url_for("user_index"))

def delete(user_id):
    """Borra un usuario que no sea el que tiene la sesion iniciada."""
    user = User.find_by_id(user_id)
    
    if user_id != session.get("user").id:
        assert_permit(session, "user_delete")
        User.delete(user)
    else:
        flash("El usuario seleccionado no puede ser borrado.")

    return redirect(url_for("user_index"))

def unblock(user_id):
    """Cambiara el estado de un usuario de "bloqueado" a "activo". Los usuarios administradores no pueden ser bloqueados."""
    assert_permit(session, "user_unblock")
    user = User.find_by_id(user_id)
    User.unblock(user)
    return redirect(url_for("user_index"))

def assign_role(user, role):
    """Le otorgara un nuevo rol a un usuario existente, determinado por su user."""
    assert_permit(session, "user_assign_role")
    User.assign_role(user, role)
    session["user_permits"] = user.get_permits()
    return redirect(url_for("user_index"))

def unassign_role(user, role):
    """Le quita un rol a un usuario existente."""
    assert_permit(session, "user_unassign_role")
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
    
    param_wrapper = FormTemplateParamsWrapper(
        form, url_for("user_modify", user_id=user.id), "edición", url_for('user_index') , "Usuario", user.first_name, user.id
    )
    
    return render_template("generic/base_form.html", param_wrapper=param_wrapper)
    
    
