from flask import redirect, render_template, request, url_for, session, abort
from sqlalchemy.sql.expression import false, true

from app.models.meeting_point import Meeting_Point
from app.helpers.auth import assert_permit
from app.forms.meeting_point_forms import MeetingPointModificationForm
from app.helpers.filter import Filter
from app.forms.filter_forms import PointFilter

# Protected resources
def index():
    """Muestra la lista de puntos de encuentro."""
    assert_permit(session, "points_index")

    points = allPublic()
    filt = Filter(PointFilter, Meeting_Point, request.args)
    
    return render_template("points/index.html", points=filt.get_query(), form=filt.form)

def show(point_id):
    """Muestra la lista de puntos de encuentro."""
    assert_permit(session, "points_show")

    point = Meeting_Point.find_by_id(point_id)
    
    return render_template("points/show.html", point=point)

def allPublic():
    """Devuelve la lista completa de los puntos de encuentro publicos gurdados en la base de datos."""
    return Meeting_Point.allPublic()

def allNotPublic():
    """Devuelve la lista completa de los puntos de encuentro no publicos gurdados en la base de datos."""
    return Meeting_Point.allNotPublic()

def all():
    """Devuelve la lista completa de los puntos de encuentro gurdados en la base de datos."""
    return Meeting_Point.all()

def new():
    """Devuelve el template para crear un nuevo punto de encuentro."""
    assert_permit(session, "points_new")
    form = MeetingPointModificationForm()

    if request.method == "POST" and form.validate():
        create(form.name.data, form.direction.data, form.coordinates.data, form.telephone.data, form.email.data)
        return redirect(url_for('points_index'))

    return render_template("points/new.html", form=form, item_type="Punto de encuentro") #point=point

def create(name, direction, coordinates, telephone, email):
    """Crea un punto de encuentro con los datos envuados por request."""
    assert_permit(session, "points_create")

    Meeting_Point.create(name, direction, coordinates, telephone, email)# **request.form)
    return redirect(url_for("points_index"))

def modify(point_id):
    """Modifica los datos de un usuario."""
    assert_permit(session, "points_modify")
    point = Meeting_Point.find_by_id(point_id)
    form = MeetingPointModificationForm(obj=point)
    form.populate_obj(point)

    if request.method == "POST" and form.validate():
        Meeting_Point.update()
        return redirect(url_for('points_show', point_id=point_id))
    return render_template("points/edit.html", form=form, point=point, item={"type": "Punto de encuentro", "name": point.name})
    
def delete(point_id):
    """Permite eliminar puntos de encuentro."""
    assert_permit(session, "points_delete") 

    Meeting_Point.delete(point_id)
    
    return redirect(url_for("points_index"))