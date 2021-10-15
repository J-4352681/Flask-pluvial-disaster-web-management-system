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

def getPrivatePalette():
    """Devuelve una lista de nombres de colores reconocidos por HTML. Si no existe una lista de colores para la aplicacion privadada especificada en la configuracion se deuvelve una por defecto."""
    configuration = get()
    if ( configuration.palette_private): # una lista vacia es falso
        return list(map(lambda color: color.value, configuration.palette_private))
    else:
        return ["Snow", "Gray", "Salmon"] # Colores por defecto, reconocidos por HTML

def getPublicPalette():
    """Devuelve una lista de nombres de colores reconocidos por HTML. Si no existe una lista de colores para la aplicacion publica especificada en la configuracion se deuvelve una por defecto."""
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return list(map(lambda color: color.value, configuration.palette_public))
    else:
        return ["Snow", "Gray", "SkyBlue"] # Colores por defecto, reconocidos por HTML

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

def flash_errors(form):
    """Flashes form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'error')

def modify():
    """Modifica todos los datos de la configuracion."""
    assert_permit(session, "config_modify")
    config = get()

    #Initialice form
    form = Config_forms(obj=config, 
        private_color1 = config.palette_private[0].id,
        private_color2 = config.palette_private[1].id,
        private_color3 = config.palette_private[2].id,
        public_color1 = config.palette_public[0].id,
        public_color2 = config.palette_public[1].id,
        public_color3 = config.palette_public[2].id
    )
    
    #Obtener colores
    colores = [(g.id, g.value) for g in allColors()]
    form.private_color1.choices = colores
    form.private_color2.choices = colores
    form.private_color3.choices = colores
    form.public_color1.choices = colores
    form.public_color2.choices = colores
    form.public_color3.choices = colores

    #form.palette_private.choices = colores #Select fields no esta devolviendo los valores que selecciono
    flash_errors(form) #No flashea los errores que deberia
    if request.method == "POST" and form.validate():
        modifyElementsPerPage(config, form.elements_per_page.data)
        modifySortCriterionUser(config, form.sort_users.data)
        modifySortCriterionMeetingPoints(config, form.sort_meeting_points.data)
        coloresPrivados = [getColor(dict(colores).get(form.private_color1.data)), getColor(dict(colores).get(form.private_color2.data)), getColor(dict(colores).get(form.private_color3.data))]
        #coloresPrivados = list(map(lambda x: getColor(dict(colores).get(x)), form.palette_private.data))
        newPrivatePallete(config, coloresPrivados)
        coloresPublicos = [getColor(dict(colores).get(form.public_color1.data)), getColor(dict(colores).get(form.public_color2.data)), getColor(dict(colores).get(form.public_color3.data))]
        newPublicPallete(config, coloresPublicos)
        
        return redirect(url_for('config_index'))

    return render_template("config/edit.html", form=form, config=config)