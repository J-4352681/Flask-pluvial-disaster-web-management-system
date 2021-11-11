from flask import redirect, render_template, request, url_for, session, flash

from app.helpers.auth import assert_permit, authenticated
from app.helpers.filter import Filter
from app.helpers.template_pages import FormPage, DBModelIndexPage, ItemDetailsPage

from app.models.complaint import Complaint
from app.models.user import User
from app.models.category import Category

from app.forms.complaint_forms import ComplaintForm

# from app.forms.complaint_forms import ComplaintForm
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
    pass


def delete(complaint_id):
    pass


def show(complaint_id):
    pass