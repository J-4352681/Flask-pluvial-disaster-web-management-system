from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.expression import false, true

from app.models.config import Config
from app.helpers.auth import assert_permit
from app.helpers.user import username_or_email_already_exist
from app.helpers.filter import apply_filter


# Protected resources
def index():
    """Muestra las opciones de configuracion."""
    assert_permit(session, "config_index")

    query = {k: v for k, v in request.args.items() if v != ''}

    if query == {}:
        options = Config.all()
    else:
        options = apply_filter(Config, query)
    
    return render_template("user/index.html")

def get():
    """Devuelve la configuracion del sistema. Si no existe una configuracion crea una nueva."""
    assert_permit(session, "config_get")

    configExists = Config.get()
    if ( not configExists ): 
        configExists = Config.create()

    return configExists

def modifyElementsPerPage( cant ):
    """Actualiza la cantidad de elementos que se muestran por pagina del listado."""
    assert_permit(session, "config_modifyElementsPerPage")

    Config.modifyElementsPerPage( Config.get(), cant )

    return render_template("user/index.html")

def modifySortCriterionUser( criteria ):
    """Actualiza el criterio por defecto de ordenamiento de los usuarios."""
    assert_permit(session, "config_modifySortCriterionUser")

    Config.modifySortCriterionUser( Config.get(), criteria )

    return render_template("user/index.html")

def modifySortCriterionMeetingPoints( criteria ):
    """Actualiza el criterio por defecto de ordenamiento de los puntos de encuentro."""
    assert_permit(session, "config_modifySortCriterionMeetingPoints")

    Config.modifySortCriterionMeetingPoints( Config.get(), criteria )

    return render_template("user/index.html")

def newPrivatePallete( colorList ):
    """Actualiza la paleta privada de colores en configuracion. Recibe una lista de objetos 'Color'."""
    assert_permit(session, "config_newPrivatePallete")

    configExists = Config.get()
    Config.newPrivatePalette( configExists, colorList)

    return render_template("user/index.html")

def newPublicPallete( colorList ):
    """Actualiza la paleta privada de colores en configuracion. Recibe una lista de objetos 'Color'."""
    assert_permit(session, "config_newPublicPallete")

    configExists = Config.get()
    Config.newPublicPalette( configExists, colorList)

    return render_template("user/index.html")
    
def modify(config, cant):
    """Modifica los datos de la configuracion. POR AHORA NO FUNCIONA. USAR INDIVIDUALES."""
    