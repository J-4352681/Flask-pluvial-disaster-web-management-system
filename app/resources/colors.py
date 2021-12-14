from flask import redirect, render_template, request, url_for, session, abort, flash
from sqlalchemy.sql.expression import false, label, true

from app.models.color import Color
from app.helpers.auth import assert_permit
# from app.helpers.filter import apply_filter


# Protected resources
def index():
    """Muestra todos los colores. NO ES NECESARIO POR AHORA. NO ESTA IMPLEMENTADO"""
    #assert_permit(session, "colors_index")
    
    #return render_template("user/index.html")

def all():
    """Devuelve todos los colores que hay cargados en el sistema."""
    # assert_permit(session, "colors_all")

    return Color.all()

def all_values():
    """Devuelve todos los colores que hay cargados en el sistema."""
    # assert_permit(session, "colors_all")

    return list(map(lambda x: x.value, all() ))

def new(name):
    """crea un nuevo color en el sistema si su nombre (value) no se repite con uno existente"""
    #assert_permit(session, "colors_new")
    if ( not Color.find_by_value(name) ):
        Color.create(name)

def get(name):
    # assert_permit(session, "colors_get")
    return Color.find_by_value(name)

def get_by_id(name):
    # assert_permit(session, "colors_get")
    return Color.find_by_id(name)
