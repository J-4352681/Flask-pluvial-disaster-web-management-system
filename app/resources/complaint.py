from flask import redirect, render_template, request, url_for, session, flash

from json import loads

from app.helpers.auth import assert_permit, authenticated
from app.helpers.filter import Filter
from app.helpers.template_pages import FormPage, DBModelIndexPage, ItemDetailsPage

from app.models.complaint import Complaint
from app.models.user import User
from app.models.category import Category

from app.forms.complaint_forms import ComplaintForm, ComplaintModificactionForm
from app.forms.filter_forms import ComplaintFilter

def index(page=None):
    """Muestra la lista de denuncias."""
    assert_permit(session, "complaint_index")

    filt = Filter(ComplaintFilter, Complaint, request.args)
    
    temp_interface = DBModelIndexPage(
        filt, page, title="Administración de denuncias",
        subtitle="Administración, adición y eliminación de las denuncias del sitio"
    )

    return render_template("complaint/pages/index.html", temp_interface=temp_interface)


def new():
    """Devuelve el template para crear una nueva denuncia."""
    assert_permit(session, "complaint_new")
    complaint = Complaint()
    form = ComplaintForm(User.all(), Category.all(), obj=complaint)

    if form.validate_on_submit():
        create(form, complaint)
        return redirect(url_for("complaint_index"))
    else:
        temp_interface = FormPage(
            form, url_for("complaint_new"),
            title="Creación de denuncia", subtitle="Creando una nueva denuncia",
            return_url=url_for('complaint_index')
        )

        return render_template("generic/pages/zone_form.html", temp_interface=temp_interface)


def create(form, complaint):
    """Verifica que los datos unicos no esten repetidos
    antes de crear una nueva denuncia con los datos pasados por request."""
    assert_permit(session, "complaint_create")

    form.populate_obj(complaint)
    complaint.coordinates = loads(complaint.coordinates)
    Complaint.create_from_complaint(complaint)


def modify(complaint_id):
    """Modifica los datos de una denuncia."""
    assert_permit(session, "complaint_modify")

    complaint = Complaint.find_by_id(complaint_id)
    form = ComplaintModificactionForm(User.all(), Category.all(), obj=complaint)

    if form.validate_on_submit():
        form.populate_obj(complaint)
        complaint.coordinates = loads(complaint.coordinates)
        Complaint.update()
        return redirect(url_for('complaint_index'))

    temp_interface = FormPage(
        form, url_for("complaint_modify", complaint_id=complaint.id),
        title="Edición de denuncia", subtitle="Editando la denuncia "+str(complaint.title),
        return_url=url_for('complaint_index')
    )
    
    return render_template("generic/pages/zone_form.html", temp_interface=temp_interface)


def delete(complaint_id):
    """Borra una zona inundable"""
    assert_permit(session, "complaint_delete")
    Complaint.delete_by_id(complaint_id)

    return redirect(url_for("complaint_index"))


def show(complaint_id):
    """Muestra los datos de la zona inundable."""
    assert_permit(session, "complaint_show")

    complaint = Complaint.find_by_id(complaint_id)
    
    temp_interface = ItemDetailsPage(
        {
          "Título": complaint.title,
          "Día y fecha de creación": complaint.creation_date, 
          "Día y fecha de cierre": complaint.closure_date,
          "Descripción": complaint.description,
          "Coordenadas": complaint.coordinates,
          "Estado": complaint.state,
          "Categoría": complaint.category.name,
          "Usuario asignado": complaint.assigned_user.username + " - " + complaint.assigned_user.email,
          "Nombre del autor": complaint.author_first_name,
          "Apellido del autor": complaint.author_last_name,
          "Teléfono del autor": complaint.author_telephone,
          "Email del autor": complaint.author_email,
        }, complaint,
        title="Denuncias", subtitle="Detalles de la denuncia " + str(complaint.title),
        return_url=url_for("complaint_index"),
        edit_url=url_for("complaint_modify", complaint_id=complaint.id),
        delete_url=url_for("complaint_delete", complaint_id=complaint.id)
    )
    
    return render_template("complaint/pages/zone_item_details.html", temp_interface=temp_interface)


def close_complaint(complaint_id):
    Complaint.close_complaint(complaint_id)
    return redirect(url_for("follow_up_index", complaint_id=complaint_id))