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
    """Modifica los datos de la configuracion."""
    