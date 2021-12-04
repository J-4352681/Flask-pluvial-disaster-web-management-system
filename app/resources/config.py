from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.expression import false, true

from app.models.config import Config

from app.resources.colors import getById as getColorById, all as allColors
from app.resources.colors import new as newColor
from app.resources.colors import get as getColor

from app.models.meeting_point import MeetingPoint
from app.models.user import User
from app.models.evacuation_route import EvacuationRoute
import app.models
from app.models.complaint import Complaint


from app.helpers.auth import assert_permit
# from app.helpers.filter import apply_filter

from app.forms.config_forms import ConfigForm

from app.helpers.template_pages import FormPage, ItemDetailsPage

# Protected resources
def index():
    """Muestra las opciones de configuracion y permite editarlas."""
    assert_permit(session, "config_index")
    
    config=get()
    private_palette = get_private_palette()
    public_palette = get_public_palette()

    temp_interface = ItemDetailsPage(
        {
          "Elementos por página": config.elements_per_page,
          "Criterio de ordenamiento de usuarios": config.translate_criteria(config.sort_users),
          "Criterio de ordenamiento de puntos de encuentro": config.translate_criteria(config.sort_meeting_points),
          "Criterio de ordenamiento de zonas inundables": config.translate_criteria(config.sort_flood_zones),
          "Criterio de ordenamiento de rutas de evacuacion": config.translate_criteria(config.sort_evacuation_routes),
          "Criterio de ordenamiento de denuncias": config.translate_criteria(config.sort_complaints),
          "Paleta de colores app privada": private_palette[0] + ", " + private_palette[1] + ", " + private_palette[2],
          "Paleta de colores app publica": public_palette[0] + ", " + public_palette[1] + ", " + public_palette[2]
        }, config,
        title="Configuración", subtitle="Configuración de los datos del sistema",
        return_url=None, edit_url=url_for('config_modify')
    )

    return render_template("generic/pages/item_details.html", temp_interface=temp_interface)

def get():
    """Devuelve la configuracion del sistema. Si no existe una configuracion crea una nueva."""
    # assert_permit(session, "config_get")

    configExists = Config.get()
    if ( not configExists ): 
        configExists = Config.create()

    return configExists

#GET PARA USO PUBLICO

def get_elements_per_page():
    """Devuelve la cantidad de elementos que se podran tener en una pagina de un listado en la app."""

    configExists = get()

    return configExists.elements_per_page

def get_sort_criterion_users():
    """Devuelve el criterio de ordenacion por defecto para los listados de usuarios."""

    configExists = get()

    return configExists.sort_users

def get_sort_criterion_meeting_points():
    """Devuelve el criterio de ordenacion por defecto para los listados de puntos de encuentro."""

    configExists = get()

    return configExists.sort_meeting_points

def get_sort_criterion_flood_zones():
    """Devuelve el criterio de ordenacion por defecto para los listados de zonas inundables."""

    configExists = get()

    return configExists.sort_flood_zones

def get_private_palette():
    """Devuelve una lista de nombres de colores reconocidos por HTML. [0] color primario, [1] secundario y [2] accento. Si no existe una lista de colores para la aplicacion privadada especificada en la configuracion se deuvelve una por defecto."""
    configuration = get()
    if ( configuration and configuration.palette_private): # una lista vacia es falso
        return [configuration.palette_private.color1.value, configuration.palette_private.color2.value, configuration.palette_private.color3.value]
    else:
        return ["Snow", "Gray", "Salmon"] # Colores por defecto, reconocidos por HTML

def get_public_palette():
    """Devuelve una lista de nombres de colores reconocidos por HTML. [0] color primario, [1] secundario y [2] accento. Si no existe una lista de colores para la aplicacion publica especificada en la configuracion se deuvelve una por defecto."""
    configuration = get()
    if ( configuration.palette_public.color1 and configuration.palette_public.color2 and configuration.palette_public.color3): # una lista vacia es falso
        return [configuration.palette_public.color1.value, configuration.palette_public.color2.value, configuration.palette_public.color3.value]
    else:
        return ["Snow", "Gray", "SkyBlue"] # Colores por defecto, reconocidos por HTML

def get_private_primary_color():
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_private.color1.value
    else:
        return "Snow" # Colores por defecto, reconocidos por HTML

def get_private_secondary_color():
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_private.color2.value
    else:
        return "Gray" # Colores por defecto, reconocidos por HTML

def get_private_accent_color():
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_private.color3.value
    else:
        return "Salmon" # Colores por defecto, reconocidos por HTML

def get_public_primary_color():
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_public.color1.value
    else:
        return "Snow" # Colores por defecto, reconocidos por HTML

def get_public_secondary_color():
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_public.color2.value
    else:
        return "Gray" # Colores por defecto, reconocidos por HTML

def get_public_accent_color():
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_public.color3.value
    else:
        return "SkyBlue" # Colores por defecto, reconocidos por HTML


#MODIFY

def modify_elements_per_page(config, cant):
    """Actualiza la cantidad de elementos que se muestran por pagina del listado."""

    Config.modify_elements_per_page(config, cant)

def modify_sort_criterion_user(config, criteria):
    """Actualiza el criterio por defecto de ordenamiento de los usuarios."""

    Config.modify_sort_criterion_user(config, criteria)

def modify_sort_criterion_meeting_points( config, criteria ):
    """Actualiza el criterio por defecto de ordenamiento de los puntos de encuentro."""

    Config.modify_sort_criterion_meeting_points(config, criteria)

def modify_sort_criterion_flood_zones(config, criteria):
    """Actualiza el criterio por defecto de ordenamiento de las zonas inundables."""

    Config.modify_sort_criterion_flood_zones(config, criteria)

def new_private_pallete(config, colorList):
    """Actualiza la paleta privada de colores en configuracion. Recibe una lista de objetos 'Color'."""
    # assert_permit(session, "config_new_private_pallete")
    if (len(colorList) >= 3):
        Config.new_private_palette(config, colorList)
    else:
        flash("La paleta nueva debe de contener al menos 3 colores.")

def new_public_pallete(config, colorList):
    """Actualiza la paleta privada de colores en configuracion. Recibe una lista de objetos 'Color', si la lista es de menos de 3 elementos no se actualiza."""
    # assert_permit(session, "config_new_public_pallete")
    if (len(colorList) >= 3):
        Config.new_public_palette(config, colorList)
    else:
        flash("La paleta nueva debe de contener al menos 3 colores.")

def modify():
    """Modifica todos los datos de la configuracion."""
    assert_permit(session, "config_modify")
    config = get()

    #Initialice form
    if (config and config.palette_private and config.palette_public):
        form = ConfigForm(obj=config, 
            private_color1 = config.palette_private.color1.id,
            private_color2 = config.palette_private.color2.id,
            private_color3 = config.palette_private.color3.id,
            public_color1 = config.palette_public.color1.id,
            public_color2 = config.palette_public.color2.id,
            public_color3 = config.palette_public.color3.id
        )
    else:
        form = ConfigForm(obj=config)
    
    # Ordenamiendo
    form.sort_users.choices =  User.get_sorting_atributes()
    form.sort_meeting_points.choices = MeetingPoint.get_sorting_atributes()
    form.sort_flood_zones.choices = app.models.flood_zone.FloodZone.get_sorting_atributes()
    form.sort_evacuation_routes.choices = EvacuationRoute.get_sorting_atributes()
    form.sort_complaints.choices = Complaint.get_sorting_atributes()

    #Obtener colores
    colores = [(g.id, g.value) for g in allColors()]
    form.private_color1.choices = colores
    form.private_color2.choices = colores
    form.private_color3.choices = colores
    form.public_color1.choices = colores
    form.public_color2.choices = colores
    form.public_color3.choices = colores

    #form.palette_private.choices = colores #Select fields no esta devolviendo los valores que selecciono
    if request.method == "POST" and form.validate():
        modify_elements_per_page(config, form.elements_per_page.data)
        if(form.sort_users.data): modify_sort_criterion_user(config, form.sort_users.data)
        if(form.sort_meeting_points.data):modify_sort_criterion_meeting_points(config, form.sort_meeting_points.data)
        if(form.private_color1.data and form.private_color2.data and form.private_color3.data):
            coloresPrivados = [getColor(dict(colores).get(form.private_color1.data)), getColor(dict(colores).get(form.private_color2.data)), getColor(dict(colores).get(form.private_color3.data))]
            new_private_pallete(config, coloresPrivados)
        if(form.public_color1.data and form.public_color2.data and form.public_color3.data):
            coloresPublicos = [getColor(dict(colores).get(form.public_color1.data)), getColor(dict(colores).get(form.public_color2.data)), getColor(dict(colores).get(form.public_color3.data))]
            new_public_pallete(config, coloresPublicos)
        
        return redirect(url_for("config_index"))

    temp_interface = FormPage(
        form, url_for("config_modify"),
        title="Edición de configuración", subtitle="Editando el apartado de configuración",
        return_url=url_for("config_index")
    )

    return render_template("generic/pages/form.html", temp_interface=temp_interface)