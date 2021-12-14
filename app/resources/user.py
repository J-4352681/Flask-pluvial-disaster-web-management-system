from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.expression import false, true

from app.models.user import User
from app.models.role import Role

from app.helpers.auth import assert_permit, authenticated
from app.helpers.filter import Filter
from app.helpers.template_pages import FormPage, DBModelIndexPage, ItemDetailsPage
from app.helpers.controllers_redirect import url_or_home

from app.forms.user_forms import UserCreationForm, UserModificationForm, UserProfileModificationForm, UnapprovedUserModificationForm
from app.forms.filter_forms import UserFilter

# Protected resources
def index(page=None):
    """Muestra la lista de usuarios."""
    assert_permit(session, "user_index")

    filt = Filter(UserFilter, User, request.args)
    
    temp_interface = DBModelIndexPage(
        filt, page, title="Administración de usuarios",
        subtitle="Administración, adición y eliminación de los usuarios del sitio"
    )

    return render_template("user/pages/index.html", temp_interface=temp_interface)

def new():
    """Devuelve el template para crear un nuevo usuario."""
    assert_permit(session, "user_new")
    user = User()
    form = UserCreationForm(obj=user)

    if form.validate_on_submit():
        create(form, user)
        return redirect(url_or_home("user_index"))
    else:
        temp_interface = FormPage(
            form, url_for("user_new"),
            title="Creación de usuario", subtitle="Creando un nuevo usuario",
            return_url=url_or_home("user_index")
        )

        return render_template("generic/pages/form.html", temp_interface=temp_interface)

def create(form, user):
    """Verifica que que quien crea el usuario tenga los permisos de modificar la BD con un alta de usuario"""
    assert_permit(session, "user_create")

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
    
    return redirect(url_or_home("user_index"))

def delete(user_id):
    """Borra un usuario que no sea el que tiene la sesion iniciada."""
    user = User.find_by_id_if_has_no_complaints(user_id)

    if user and user_id != session.get("user").id:
        assert_permit(session, "user_delete")
        User.delete(user)
    else:
        flash("El usuario seleccionado no puede ser borrado.")

    return redirect(url_or_home("user_index"))

def unblock(user_id):
    """Cambiara el estado de un usuario de "bloqueado" a "activo". Los usuarios administradores no pueden ser bloqueados."""
    assert_permit(session, "user_unblock")
    user = User.find_by_id(user_id)
    User.unblock(user)
    return redirect(url_or_home("user_index"))

def assign_role(user, role):
    """Le otorgara un nuevo rol a un usuario existente, determinado por su user."""
    assert_permit(session, "user_assign_role")
    User.assign_role(user, role)
    session["user_permits"] = user.get_permits()
    return redirect(url_or_home("user_index"))

def unassign_role(user, role):
    """Le quita un rol a un usuario existente."""
    assert_permit(session, "user_unassign_role")
    User.unassign_role(user, role)
    session["user_permits"] = user.get_permits()
    return redirect(url_or_home("user_index"))

def modify(user_id):
    """Modifica los datos de un usuario."""
    assert_permit(session, "user_modify")

    user = User.find_by_id(user_id)
    form = UserModificationForm(obj=user)

    if user_id == session.get("user").id:
        return redirect(url_for("profile_modify", user_id=user_id))

    if not user.approved:
        return redirect(url_for("user_approve", user_id=user_id))

    if form.validate_on_submit():
        form.populate_obj(user)
        User.update()
        return redirect(url_or_home("user_index"))

    temp_interface = FormPage(
        form, url_for("user_modify", user_id=user.id),
        title="Edición de usuario", subtitle="Editando el usuario "+str(user.first_name),
        return_url=url_or_home("user_index")
    )
    
    return render_template("generic/pages/form.html", temp_interface=temp_interface)

def approve(user_id):
    """Modifica los datos de un usuario no aprovado."""
    assert_permit(session, "user_approve")

    user = User.find_by_id(user_id)
    form = UnapprovedUserModificationForm(obj=user)

    if form.validate_on_submit():
        form.populate_obj(user)
        User.update()
        return redirect(url_or_home("user_index"))

    temp_interface = FormPage(
        form, url_for("user_approve", user_id=user.id),
        title="Edición de usuario no aprovado", subtitle="Editando el usuario no aprovado "+str(user.first_name),
        return_url=url_or_home("user_index")
    )
    
    return render_template("generic/pages/form.html", temp_interface=temp_interface)

def profile():
    user = authenticated(session)

    temp_interface = ItemDetailsPage(
        {
          "Nombre": user.first_name,
          "Apellido": user.last_name,
          "Email": user.email,
          "Username": user.username
        }, user,
        title="Perfil del usuario "+ str(user.first_name), subtitle="Datos del usuario",
        return_url=url_or_home("user_index"),
        edit_url=url_for("profile_modify", user_id=user.id)
    )
    
    return render_template("generic/pages/item_details.html", temp_interface=temp_interface)

def profile_modify():
    """Modifica los datos de un usuario."""
    user = authenticated(session)
    user = User.find_by_id(user.id)
    form = UserProfileModificationForm(obj=user)

    if not user.approved:
        flash("Debes esperar a ser aprobado para poder editar tus datos.")
        return redirect(url_for("profile_index"))

    if form.validate_on_submit():
        form.populate_obj(user)
        User.update()
        session["user"] = User.find_by_id(user.id)
        return redirect(url_for("profile_index"))
    
    temp_interface = FormPage(
        form, url_for("profile_modify"),
        title="Perfil del usuario "+ str(user.first_name), subtitle="Editando datos personales",
        return_url=url_for("profile_index")
    )
    
    return render_template("generic/pages/form.html", temp_interface=temp_interface)