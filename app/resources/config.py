from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.expression import false, true

from app.models.config import Config

from app.models.meeting_point import MeetingPoint
from app.models.flood_zone import FloodZone
from app.models.user import User
from app.models.palette import Palette
from app.models.evacuation_route import EvacuationRoute
import app.models
from app.models.complaint import Complaint

from app.helpers.auth import assert_permit

from app.forms.config_forms import ConfigForm

from app.helpers.template_pages import FormPage, ItemDetailsPage

# Protected resources
def index():
    """Muestra las opciones de configuracion y permite editarlas."""
    assert_permit(session, "config_index")

    config = Config.get_current_config()

    temp_interface = ItemDetailsPage(
        {
          "Elementos por página": config.elements_per_page,
          "Criterio de ordenamiento de usuarios": config.translate_criteria(config.sort_users),
          "Criterio de ordenamiento de puntos de encuentro": config.translate_criteria(config.sort_meeting_points),
          "Criterio de ordenamiento de zonas inundables": config.translate_criteria(config.sort_flood_zones),
          "Criterio de ordenamiento de rutas de evacuacion": config.translate_criteria(config.sort_evacuation_routes),
          "Criterio de ordenamiento de denuncias": config.translate_criteria(config.sort_complaints),
          "Criterio de ordenamiento de paletas de color": config.translate_criteria(config.sort_palettes),
          "Paleta de colores app privada": config.palette_private.name,
          "Paleta de colores app publica": config.palette_public.name
        }, config,
        title="Configuración", subtitle="Configuración de los datos del sistema",
        return_url=None, edit_url=url_for('config_modify')
    )

    return render_template("config/pages/item_details.html", temp_interface=temp_interface)

def modify():
    """Modifica todos los datos de la configuracion."""
    assert_permit(session, "config_modify")
    config = Config.get_current_config()

    form = ConfigForm(obj=config)

    if form.validate_on_submit():
        form.palette_public.data = Palette.find_by_id(int(form.palette_public.raw_data[0]))
        form.palette_private.data = Palette.find_by_id(int(form.palette_private.raw_data[0]))
        form.populate_obj(config)
        Config.update()
        return redirect(url_for("config_index"))

    temp_interface = FormPage(
        form, url_for("config_modify"),
        title="Edición de configuración", subtitle="Editando el apartado de configuración",
        return_url=url_for("config_index")
    )

    return render_template("generic/pages/form.html", temp_interface=temp_interface)
