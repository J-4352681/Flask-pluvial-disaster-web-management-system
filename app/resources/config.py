from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.expression import false, true

from app.models.config import Config
from app.resources.colors import getById as getColorById, all as allColors
from app.resources.colors import new as newColor
from app.resources.colors import get as getColor
from app.helpers.auth import assert_permit
# from app.helpers.filter import apply_filter

from app.forms.config_forms import Config_forms

# Protected resources
def index():
    """Muestra las opciones de configuracion y permite editarlas."""
    assert_permit(session, "config_index")
    
    config=get()
    private_palette = getPrivatePalette()
    public_palette = getPublicPalette()
    
    return render_template("config/index.html", config=config, private_palette = private_palette, public_palette = public_palette, filters={"first_name": "Nombre", "last_name":"Apellido"})

def get():
    """Devuelve la configuracion del sistema. Si no existe una configuracion crea una nueva."""
    # assert_permit(session, "config_get")

    configExists = Config.get()
    if ( not configExists ): 
        configExists = Config.create()

    return configExists

#GET PARA USO PUBLICO

def getElementsPerPage():
    """Devuelve la cantidad de elementos que se podran tener en una pagina de un listado en la app."""

    configExists = get()

    return configExists.elements_per_page

def getSortCriterionUsers():
    """Devuelve el criterio de ordenacion por defecto para los listados de usuarios."""

    configExists = get()

    return configExists.sort_users

def getSortCriterionMeetingPoints():
    """Devuelve el criterio de ordenacion por defecto para los listados de puntos de encuentro."""

    configExists = get()

    return configExists.sort_meeting_points

def getPrivatePalette():
    """Devuelve una lista de nombres de colores reconocidos por HTML. [0] color primario, [1] secundario y [2] accento. Si no existe una lista de colores para la aplicacion privadada especificada en la configuracion se deuvelve una por defecto."""
    configuration = get()
    if ( configuration.palette_private.color1 and configuration.palette_private.color2 and configuration.palette_private.color3): # una lista vacia es falso
        return [configuration.palette_private.color1.value, configuration.palette_private.color2.value, configuration.palette_private.color3.value]
    else:
        return ["Snow", "Gray", "Salmon"] # Colores por defecto, reconocidos por HTML

def getPublicPalette():
    """Devuelve una lista de nombres de colores reconocidos por HTML. [0] color primario, [1] secundario y [2] accento. Si no existe una lista de colores para la aplicacion publica especificada en la configuracion se deuvelve una por defecto."""
    configuration = get()
    if ( configuration.palette_public.color1 and configuration.palette_public.color2 and configuration.palette_public.color3): # una lista vacia es falso
        return [configuration.palette_public.color1.value, configuration.palette_public.color2.value, configuration.palette_public.color3.value]
    else:
        return ["Snow", "Gray", "SkyBlue"] # Colores por defecto, reconocidos por HTML

def getPrivatePrimaryColor():
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_private.color1.value
    else:
        return "Snow" # Colores por defecto, reconocidos por HTML

def getPrivateSecondaryColor():
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_private.color2.value
    else:
        return "Gray" # Colores por defecto, reconocidos por HTML

def getPrivateAccentColor():
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_private.color3.value
    else:
        return "Salmon" # Colores por defecto, reconocidos por HTML

def getPublicPrimaryColor():
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_public.color1.value
    else:
        return "Snow" # Colores por defecto, reconocidos por HTML

def getPublicSecondaryColor():
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_public.color2.value
    else:
        return "Gray" # Colores por defecto, reconocidos por HTML

def getPublicAccentColor():
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_public.color3.value
    else:
        return "SkyBlue" # Colores por defecto, reconocidos por HTML


#MODIFY

def modifyElementsPerPage( config, cant ):
    """Actualiza la cantidad de elementos que se muestran por pagina del listado."""
    # assert_permit(session, "config_modifyElementsPerPage")

    Config.modifyElementsPerPage( config, cant )

def modifySortCriterionUser( config, criteria ):
    """Actualiza el criterio por defecto de ordenamiento de los usuarios."""
    # assert_permit(session, "config_modifySortCriterionUser")

    Config.modifySortCriterionUser( config, criteria )

def modifySortCriterionMeetingPoints( config, criteria ):
    """Actualiza el criterio por defecto de ordenamiento de los puntos de encuentro."""
    # assert_permit(session, "config_modifySortCriterionMeetingPoints")

    Config.modifySortCriterionMeetingPoints( config, criteria )

def newPrivatePallete( config, colorList ):
    """Actualiza la paleta privada de colores en configuracion. Recibe una lista de objetos 'Color'."""
    # assert_permit(session, "config_newPrivatePallete")
    if (len(colorList) >= 3):
        Config.newPrivatePalette( config, colorList )
    else:
        flash("La paleta nueva debe de contener al menos 3 colores.")

def newPublicPallete( config, colorList ):
    """Actualiza la paleta privada de colores en configuracion. Recibe una lista de objetos 'Color', si la lista es de menos de 3 elementos no se actualiza."""
    # assert_permit(session, "config_newPublicPallete")
    if (len(colorList) >= 3):
        Config.newPublicPalette( config, colorList )
    else:
        flash("La paleta nueva debe de contener al menos 3 colores.")

def modify():
    """Modifica todos los datos de la configuracion."""
    assert_permit(session, "config_modify")
    config = get()

    #Initialice form
    if (config and config.palette_private and config.palette_public):
        form = Config_forms(obj=config, 
            private_color1 = config.palette_private.color1.id,
            private_color2 = config.palette_private.color2.id,
            private_color3 = config.palette_private.color3.id,
            public_color1 = config.palette_public.color1.id,
            public_color2 = config.palette_public.color2.id,
            public_color3 = config.palette_public.color3.id
        )
    else:
        form = Config_forms(obj=config)
    
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
        modifyElementsPerPage(config, form.elements_per_page.data)
        if(form.sort_users.data): modifySortCriterionUser(config, form.sort_users.data)
        if(form.sort_meeting_points.data):modifySortCriterionMeetingPoints(config, form.sort_meeting_points.data)
        if(form.private_color1.data and form.private_color2.data and form.private_color3.data):
            coloresPrivados = [getColor(dict(colores).get(form.private_color1.data)), getColor(dict(colores).get(form.private_color2.data)), getColor(dict(colores).get(form.private_color3.data))]
            newPrivatePallete(config, coloresPrivados)
        if(form.public_color1.data and form.public_color2.data and form.public_color3.data):
            coloresPublicos = [getColor(dict(colores).get(form.public_color1.data)), getColor(dict(colores).get(form.public_color2.data)), getColor(dict(colores).get(form.public_color3.data))]
            newPublicPallete(config, coloresPublicos)
        
        return redirect(url_for('config_index'))

    return render_template("config/edit.html", form=form, config=config)