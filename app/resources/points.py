from flask import redirect, render_template, request, url_for, session, abort
from sqlalchemy.sql.expression import false, true
from app.models.meeting_point import Meeting_Point
from app.helpers.auth import authenticated
import app.db

# Protected resources
def index():
    """Muestra la lista de puntos de encuentro."""
    if not authenticated(session):
        abort(401)

    points = Meeting_Point.all()
    
    return render_template("points/index.html", points=points)