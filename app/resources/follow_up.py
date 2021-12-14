from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.elements import Null
from sqlalchemy.sql.expression import false, true

from app.models.follow_up import Follow_up
from app.models.complaint import Complaint
from app.models.role import Role

from app.helpers.auth import assert_permit, authenticated
from app.helpers.filter import Filter
from app.helpers.template_pages import FormPage, DBModelIndexPage, ItemDetailsPage, SubDBModelIndexPage
from app.helpers.controllers_redirect import url_or_home

from app.forms.follow_up_forms import FollowUpForm

# Protected resources
def index(complaint_id): #, page=None):
    """Muestra la lista seguimientos para una denuncia."""
    assert_permit(session, "follow_up_index")

    fups = Follow_up.find_by_complaint_id(complaint_id)
    com = Complaint.find_by_id(complaint_id)

    temp= SubDBModelIndexPage(
        com, url_for('complaint_show', complaint_id=complaint_id),
        title="Lista de seguimientos de denuncia "+str(com.title),
        subtitle="Seguimientos de denuncia "+str(com.title),
    )

    return render_template("follow_up/pages/index.html", temp_interface=temp, followUps = fups, complaint_id=complaint_id)

def new(complaint_id=None):
    """Devuelve el template para crear un nuevo seguimiento."""
    assert_permit(session, "follow_up_new")

    us = session.get("user")
    com = Complaint.find_by_id(complaint_id)

    if ( not ( us.is_admin() )):
        if (not (us.id == com.assigned_user_id)):
            abort(403)

    fup = Follow_up()
    form = FollowUpForm(obj=fup)

    fup.author_id = session.get("user").id
    fup.complaint_id = complaint_id

    if form.validate_on_submit():
        create(form, fup)
        return redirect(url_or_home("follow_up_index", complaint_id=fup.complaint_id))
    else:
        temp_interface = FormPage(
            form, url_for("follow_up_new", complaint_id=fup.complaint_id),
            title="Creación de seguimiento", subtitle="Creando un nuevo seguimiento",
            return_url=url_or_home("follow_up_index", complaint_id=fup.complaint_id)
        )

        return render_template("generic/pages/form.html", temp_interface=temp_interface)

def create(form, follow_up):
    """Verifica que que quien crea el seguimiento tenga permisos apropiados."""
    assert_permit(session, "follow_up_create")

    form.populate_obj(follow_up)
    Follow_up.create_from_follow_up(follow_up)

def delete(follow_up_id):
    """Borra un seguimiento."""
    assert_permit(session, "follow_up_delete")

    fup = Follow_up.find_by_id(follow_up_id)
    Follow_up.delete(fup.id)

    return redirect(url_or_home("follow_up_index", complaint_id=fup.complaint_id))

def modify(follow_up_id):
    """Modifica los datos de un seguimiento."""
    assert_permit(session, "follow_up_modify")

    fup = Follow_up.find_by_id(follow_up_id)
    form = FollowUpForm(obj=fup)

    if form.validate_on_submit():
        form.populate_obj(fup)
        Follow_up.update()
        return redirect(url_or_home("follow_up_index", complaint_id=fup.complaint_id))

    temp_interface = FormPage(
        form, url_for("follow_up_modify", follow_up_id=fup.id),
        title="Edición de seguimiento", subtitle="Editando seguimiento",
        return_url=url_or_home("follow_up_index", complaint_id=fup.complaint_id)
    )
    
    return render_template("generic/pages/form.html", temp_interface=temp_interface)
   