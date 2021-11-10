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
from string import ascii_lowercase
from random import choice as random_choice

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
    fzone = FloodZone()
    form = FloodZoneForm(obj=fzone)

    if form.validate_on_submit():
        create(form, fzone)
        return redirect(url_for("fzone_index"))
    else:
        temp_interface = FormPage(
            form, url_for("fzone_new"),
            title="Creación de zona inundable", subtitle="Creando una nueva zona inundable",
            return_url=url_for('fzone_index')
        )

        return render_template("flood_zone/pages/form.html", temp_interface=temp_interface)


def create(form, fzone):
    """Verifica que los datos unicos no esten repetidos antes de crear un nuevo usuario con los datos pasados por request."""
    assert_permit(session, "fzone_create")

    form.populate_obj(fzone)
    fzone.coordinates = loads(fzone.coordinates)
    FloodZone.create_from_flood_zone(fzone)


def modify(fzone_id):
    """Modifica los datos de una zona inundable."""
    assert_permit(session, "fzone_modify")

    fzone = FloodZone.find_by_id(fzone_id)
    form = FloodZoneForm(obj=fzone)

    if form.validate_on_submit():
        form.populate_obj(fzone)
        fzone.coordinates = loads(fzone.coordinates)
        FloodZone.update()
        return redirect(url_for('fzone_index'))

    temp_interface = FormPage(
        form, url_for("fzone_modify", fzone_id=fzone.id),
        title="Edición de zona inundable", subtitle="Editando la zona "+str(fzone.name),
        return_url=url_for('fzone_index')
    )
    
    return render_template("flood_zone/pages/form.html", temp_interface=temp_interface)


def delete(fzone_id):
    """Borra una zona inundable"""
    assert_permit(session, "fzone_delete")
    FloodZone.delete_by_id(fzone_id)

    return redirect(url_for("fzone_index"))


def show(fzone_id):
    """Muestra la lista de puntos de encuentro."""
    assert_permit(session, "points_show")

    fzone = FloodZone.find_by_id(fzone_id)
    
    temp_interface = ItemDetailsPage(
        {
          "Código": fzone.code,
          "Nombre": fzone.name,
          "Público": fzone.state,
          "Color": fzone.color,
          "Coordenadas": fzone.coordinates
        }, fzone,
        title="Zonas inundables", subtitle="Detalles del zona " + str(fzone.name),
        return_url=url_for("fzone_index"),
        edit_url=url_for("fzone_modify", fzone_id=fzone.id),
        delete_url=url_for("fzone_delete", fzone_id=fzone.id)
    )
    
    return render_template("flood_zone/pages/item_details.html", temp_interface=temp_interface)


def allowed_file(filename):
    """Determina si un archivo cumple con el formato deseado."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() == "csv"


def from_string_coord(string_coord):
    """Transforma un texto con formato de listas de python sobre coordenadas
    a una estructura de listas de python efectivamente."""
    return list(map(lambda x: x.strip(",[] "), string_coord.split(",")))


def jsonify_list_coord(list_coord):
    """Pasa a formato json datos de coordenadas en formato de listas."""
    return [{"lat": float(list_coord[i]), "lng": float(list_coord[i+1])} for i in range(0, len(list_coord), 2)]


def create_from_name_coord(fzone):
    """Crea una zona inundable con datos nombre y coordenadas."""
    num_chars = list(map(lambda x: str(x), range(9)))

    asciinum_chars = list(ascii_lowercase) + num_chars
    code = ''.join([random_choice(asciinum_chars) for i in range(5)])
    while (FloodZone.find_by_code(code)): code = ''.join([random_choice(asciinum_chars) for i in range(5)])

    hex_chars = num_chars + list(ascii_lowercase)[:6]
    color = "#"+"".join([random_choice(hex_chars) for i in range(6)])

    fzone.code = code
    fzone.state = True
    fzone.color = color

    FloodZone.create_from_flood_zone(fzone)


def get_or_create_by_name(fzone):
    """Obtiene y modifica o crea una zona inundable pasada por parámetro
    en base al nombre de la misma."""
    saved_fzone = FloodZone.find_by_name(fzone.name)

    if (saved_fzone):
        for i in filter(lambda x: x[1] != None and x[0][0] != "_", vars(fzone).items()):
            setattr(saved_fzone, i[0], i[1])
        FloodZone.update()
    else:
        create_from_name_coord(fzone)


def csv_import():
    """Importa zonas desde archivo csv."""
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
                row[1] = jsonify_list_coord(from_string_coord(row[1]))
                get_or_create_by_name(FloodZone(name=row[0], coordinates=row[1]))
            return redirect(url_for("fzone_index"))

    else: flash("No se seleccionó archivo")
    
    return redirect(url_for("fzone_index"))