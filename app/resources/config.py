from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.expression import false, true

from app.models.config import Config
#from app.resources.colors import all as allColors
from app.resources.colors import new as newColor
from app.resources.colors import get as getColor
from app.helpers.auth import assert_permit
from app.helpers.filter import apply_filter

"""Contine la logica necesareia para modificar las opciones de la configuracion del sistema y pedir la configuracion. Si se necesita solo la paleta de colores usar Resourses/palette."""
# Protected resources
def index():
    """Muestra las opciones de configuracion y permite editarlas."""
    assert_permit(session, "config_index")

    query = {k: v for k, v in request.args.items() if v != ''}

    if query == {}:
        config = get()
    else:
        config = apply_filter(Config, query) #Esto no se usa
    
    private_palette = getPrivatePalette()
    public_palette = getPublicPalette()
    
    return render_template("config/index.html", config=config, private_palette = private_palette, public_palette = public_palette, filters={"first_name": "Nombre", "last_name":"Apellido"})

def get():
    """Devuelve la configuracion del sistema. Si no existe una configuracion crea una nueva."""
    assert_permit(session, "config_get")

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
    assert_permit(session, "config_modifyElementsPerPage")

    Config.modifyElementsPerPage( config, cant )

def modifySortCriterionUser( config, criteria ):
    """Actualiza el criterio por defecto de ordenamiento de los usuarios."""
    assert_permit(session, "config_modifySortCriterionUser")

    Config.modifySortCriterionUser( config, criteria )

def modifySortCriterionMeetingPoints( config, criteria ):
    """Actualiza el criterio por defecto de ordenamiento de los puntos de encuentro."""
    assert_permit(session, "config_modifySortCriterionMeetingPoints")

    Config.modifySortCriterionMeetingPoints( config, criteria )

def newPrivatePallete( config, colorList ):
    """Actualiza la paleta privada de colores en configuracion. Recibe una lista de objetos 'Color'."""
    assert_permit(session, "config_newPrivatePallete")
    if (len(colorList) >= 3):
        Config.newPrivatePalette( config, colorList )
    else:
        flash("La paleta nueva debe de contener al menos 3 colores.")

def newPublicPallete( config, colorList ):
    """Actualiza la paleta privada de colores en configuracion. Recibe una lista de objetos 'Color', si la lista es de menos de 3 elementos no se actualiza."""
    assert_permit(session, "config_newPublicPallete")
    if (len(colorList) >= 3):
        Config.newPublicPalette( config, colorList )
    else:
        flash("La paleta nueva debe de contener al menos 3 colores.")

def editForm(): # Todavia no funciona, crear layout edit
    """Devuelve el formulario para editar las opciones."""
    assert_permit(session, "config_editForm")

    config = get()
    private_palette = getPrivatePalette()
    public_palette = getPublicPalette()
    
    return render_template("config/index.html", config=config, private_palette = private_palette, public_palette = public_palette, filters={"first_name": "Nombre", "last_name":"Apellido"})


def update(config, cant, criteriaUser, criteriaMeetingPoint, privatePallete, publicPallete):
    """Modifica todos los datos de la configuracion."""
    assert_permit(session, "config_update")

    modifyElementsPerPage(config, cant)
    modifySortCriterionUser(config, criteriaUser)
    modifySortCriterionMeetingPoints(config, criteriaMeetingPoint)
    newPrivatePallete(config, privatePallete)
    newPublicPallete(config, publicPallete)