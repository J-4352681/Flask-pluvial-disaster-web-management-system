from flask import redirect, render_template, request, url_for, session, abort
from sqlalchemy.sql.expression import false, true
from app.models.user import User
from app.helpers.auth import authenticated
from app.resources.config import get
import app.db

# Protected resources
def getPrivatePalette():
    """Devuelve una lista de nombres de colores reconocidos por HTML. Si no existe una lista de colores para la aplicacion privadada especificada en la configuracion se deuvelve una por defecto."""
    configuration = get()
    if ( configuration.palette_private): # una lista vacia es falso
        return configuration.palette_private
    else:
        return ["Snow", "Gray", "Salmon"] # Colores por defecto, reconocidos por HTML

def getPublicPalette():
    """Devuelve una lista de nombres de colores reconocidos por HTML. Si no existe una lista de colores para la aplicacion publica especificada en la configuracion se deuvelve una por defecto."""
    configuration = get()
    if ( configuration.palette_public): # una lista vacia es falso
        return configuration.palette_public
    else:
        return ["Snow", "Gray", "SkyBlue"] # Colores por defecto, reconocidos por HTML