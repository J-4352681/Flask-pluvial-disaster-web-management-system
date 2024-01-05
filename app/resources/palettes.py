from flask import redirect, render_template, request, url_for, session, abort
from sqlalchemy.sql.expression import false, true

from app.models.palette import Palette

from app.helpers.auth import assert_permit
from app.helpers.filter import Filter
from app.helpers.template_pages import FormPage, DBModelIndexPage, ItemDetailsPage
from app.helpers.controllers_redirect import url_or_home

from app.forms.filter_forms import PaletteFilter
from app.forms.palette_forms import PaletteModificationForm

# Protected resources
def index(page=None):
    """Muestra la lista de puntos de encuentro."""
    assert_permit(session, "palettes_index")

    filt = Filter(PaletteFilter, Palette, request.args)

    temp_interface = DBModelIndexPage(
        filt, page,
        title="Paletas de color",
        subtitle="Administración, adición y eliminación de las paletas del sitio"
    )

    return render_template("palettes/pages/index.html", temp_interface=temp_interface)

def show(palette_id):
    """Muestra la lista de puntos de encuentro."""
    assert_permit(session, "palettes_show")

    palette = Palette.find_by_id(palette_id)

    temp_interface = ItemDetailsPage(
        {
          "Color primario": palette.color1,
          "Color secundario": palette.color2,
          "Color acento": palette.color3,
        }, palette,
        title="Paleta de colores", subtitle="Colores de la paleta" + str(palette.name),
        return_url=url_or_home("palettes_index"),
        edit_url=url_for("palettes_modify", palette_id=palette.id),
        delete_url=url_for("palettes_delete", palette_id=palette.id)
    )

    return render_template("generic/pages/item_details.html", temp_interface=temp_interface)

def all():
    """Devuelve la lista completa de los paletas guardadas en la base de datos."""
    return Palette.all()

def new():
    """Devuelve el template para crear una nueva paleta."""
    assert_permit(session, "palettes_new")
    form = PaletteModificationForm()

    if form.validate_on_submit():
        create(form.name.data, form.color1.data, form.color2.data, form.color3.data)
        return redirect(url_or_home("palettes_index"))
    else:
        temp_interface = FormPage(
            form, url_for("palettes_new"),
            title="Creación de paleta de color", subtitle="Creando una nueva paleta",
            return_url=url_or_home("palettes_index")
        )

        return render_template("generic/pages/form.html", temp_interface=temp_interface)

def create(name, direction, latitude, longitude, telephone, email, state):
    """Crea un punto de encuentro con los datos envuados por request."""
    assert_permit(session, "palettes_create")

    Palette.create(name, direction, latitude, longitude, telephone, email, state)

def modify(palette_id):
    """Modifica los datos de un punto de encuentro."""
    assert_permit(session, "palettes_modify")
    palette = Palette.find_by_id(palette_id)
    form = PaletteModificationForm(
        obj=palette, name=palette.name, color1=palette.color1,
        color2=palette.color2, color3=palette.color3,
    )

    if form.validate_on_submit():
        form.populate_obj(palette)
        Palette.update_data(
            palette, form.name.data, form.color1.data,
            form.color2.data, form.color3.data,
        )
        Palette.update()
        return redirect(url_or_home("palettes_index"))

    temp_interface = FormPage(
        form, url_for("palettes_modify", palette_id=palette.id),
        title="Edición de paleta de color", subtitle="Editando la paleta "+str(palette.name),
        return_url=url_or_home("palettes_index")
    )

    return render_template("generic/pages/form.html", temp_interface=temp_interface)

def delete(palette_id):
    """Permite eliminar una paleta de color."""
    assert_permit(session, "palettes_delete")

    Palette.delete(palette_id)

    return redirect(url_or_home("palettes_index"))
