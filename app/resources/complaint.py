from flask import redirect, render_template, request, url_for, session, flash

from app.helpers.auth import assert_permit, authenticated
from app.helpers.filter import Filter
from app.helpers.template_pages import FormPage, DBModelIndexPage, ItemDetailsPage

from app.models.complaint import Complaint

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
    pass


def create():
    pass


def modify(complaint_id):
    pass


def delete(complaint_id):
    pass


def show(complaint_id):
    pass