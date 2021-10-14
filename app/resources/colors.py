from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.expression import false, true

from app.models.color import Color
from app.helpers.auth import assert_permit
from app.helpers.filter import apply_filter


# Protected resources
def index():
    """Muestra todos los colores. NO ES NECESARIO POR AGORA"""
    # assert_permit(session, "config_index")

    query = {k: v for k, v in request.args.items() if v != ''}

    if query == {}:
        config = all()
    else:
        config = apply_filter(Color, query)
    
    return render_template("user/index.html")

def all():
    """Devuelve todos los colores que hay cargados en el sistema."""
    # assert_permit(session, "config_get")

    return Color.all()

def new(name):
    """crea un nuevo color en el sistema si su nombre (value) no se repite con uno existente"""
    if ( not Color.find_by_value(name) ):
        Color.create(name)

def get(name):
    return Color.find_by_value(name)
