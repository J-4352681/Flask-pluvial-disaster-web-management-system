from flask import redirect, render_template, request, url_for, session, flash
# from sqlalchemy.sql.expression import false, true

from app.models.flood_zone import FloodZone

from app.helpers.auth import assert_permit, authenticated
from app.helpers.filter import Filter
from app.helpers.template_pages import FormPage, DBModelIndexPage, ItemDetailsPage

from app.forms.fzone_forms import FloodZoneForm
from app.forms.filter_forms import FZoneFilter

# Protected resources
def index(page=None):
    """Muestra la lista de usuarios."""
    # assert_permit(session, "fzone_index")

    filt = Filter(FZoneFilter, FloodZone, request.args)
    
    temp_interface = DBModelIndexPage(
        filt, page, title="Administración de zonas inundables",
        subtitle="Administración, adición y eliminación de las zonas inundables del sitio"
    )

    return render_template("flood_zone/pages/index.html", temp_interface=temp_interface)


def new():
    """Devuelve el template para crear un nuevo usuario."""
    assert_permit(session, "fzone_new")
    flood_zone = FloodZone()
    form = FloodZoneForm(obj=flood_zone)

    print(vars(form)["_fields"]['color'])

    if form.validate_on_submit():
        create(form, flood_zone)
        return redirect(url_for("fzone_index"))
    else:
        temp_interface = FormPage(
            form, url_for("fzone_new"),
            title="Creación de zona inundable", subtitle="Creando una nueva zona inundable",
            return_url=url_for('fzone_index')
        )

        return render_template("generic/pages/form.html", temp_interface=temp_interface)


def create(form, flood_zone):
    """Verifica que los datos unicos no esten repetidos antes de crear un nuevo usuario con los datos pasados por request."""
    assert_permit(session, "fzone_create")

    form.populate_obj(flood_zone)
    FloodZone.create_from_flood_zone(flood_zone)


def modify(fzone_id):
    pass


def delete(fzone_id):
    """Borra una zona inundable"""
    assert_permit(session, "fzone_delete")
    FloodZone.delete_by_id(fzone_id)

    return redirect(url_for("fzone_index"))


def show(fzone_id):
    pass