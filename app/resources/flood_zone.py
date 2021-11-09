from flask import redirect, render_template, request, url_for, session, flash
from sqlalchemy.sql.expression import false, true
from json import loads

from app.models.flood_zone import FloodZone

from app.helpers.auth import assert_permit, authenticated
from app.helpers.filter import Filter
from app.helpers.template_pages import FormPage, DBModelIndexPage, ItemDetailsPage

from app.forms.fzone_forms import FloodZoneForm
from app.forms.filter_forms import FZoneFilter

from csv import reader as csv_reader
from werkzeug.utils import secure_filename
from io import StringIO

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

    if form.validate_on_submit():
        create(form, flood_zone)
        return redirect(url_for("fzone_index"))
    else:
        temp_interface = FormPage(
            form, url_for("fzone_new"),
            title="Creación de zona inundable", subtitle="Creando una nueva zona inundable",
            return_url=url_for('fzone_index')
        )

        return render_template("flood_zone/pages/form.html", temp_interface=temp_interface)


def create(form, flood_zone):
    """Verifica que los datos unicos no esten repetidos antes de crear un nuevo usuario con los datos pasados por request."""
    assert_permit(session, "fzone_create")

    form.populate_obj(flood_zone)
    flood_zone.coordinates = loads(flood_zone.coordinates)
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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == "csv"


def csv_import():
    if request.method == 'POST':
        if "file_import" not in request.files:
            flash('Sin archivo')
            return redirect(url_for("fzone_index"))
        file = request.files["file_import"]
        
        if file.filename == '':
            flash("No se seleccionó archivo")
            return redirect(url_for("fzone_index"))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.stream = StringIO(file.read().decode("utf-8"))
            reader = csv_reader(file.stream, delimiter=",")
            next(reader)

            for row in reader:
                coords = list(map(lambda x: x.strip(",[] "), row[1].split(",")))
                row[1] = [{"lat": coords[i], "lng": coords[i+1]} for i in range(0, len(coords), 2)]
                FloodZone.create_from_name_coord(*row)
                break
            return redirect(url_for("fzone_index"))

    else: flash("No se seleccionó archivo")
    
    return redirect(url_for("fzone_index"))