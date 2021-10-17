from flask import redirect, render_template, request, url_for, session, abort
from sqlalchemy.sql.expression import false, true

from app.models.meeting_point import Meeting_Point
from app.helpers.auth import assert_permit
from app.forms.meeting_point_forms import MeetingPointModificationForm
from app.helpers.filter import Filter
from app.forms.filter_forms import PointFilter

from app.resources.config import getSortCriterionMeetingPoints
from .generic import FormTemplateParamsWrapper

# Protected resources
def index(page=None):
    """Muestra la lista de puntos de encuentro."""
    assert_permit(session, "points_index")

    #points = allPublic()
    filt = Filter(PointFilter, Meeting_Point, request.args)
    
    return render_template("points/index.html", points=filt.get_query(page), form=filt.form)

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

    if form.validate_on_submit():
        create(form.name.data, form.direction.data, form.coordinates.data, form.telephone.data, form.email.data, form.state.data)
        return redirect(url_for('points_index'))
    else:
        param_wrapper = FormTemplateParamsWrapper(
            form, url_for('points_new'), "creacion", url_for('points_index'), "Punto de encuentro", "un nuevo punto de encuentro"
        )

        return render_template("generic/base_form.html", param_wrapper=param_wrapper)
    # return render_template("points/new.html", form=form, item_type="Punto de encuentro") #point=point

def create(name, direction, coordinates, telephone, email, state):
    """Crea un punto de encuentro con los datos envuados por request."""
    assert_permit(session, "points_create")

    Meeting_Point.create(name, direction, coordinates, telephone, email, state)# **request.form)

def modify(point_id):
    """Modifica los datos de un usuario."""
    assert_permit(session, "points_modify")
    point = Meeting_Point.find_by_id(point_id)
    form = MeetingPointModificationForm(obj=point)
    form.populate_obj(point)

    if form.validate_on_submit():
        form.populate_obj(point)
        Meeting_Point.update()
        return redirect(url_for('points_index'))
    
    param_wrapper = FormTemplateParamsWrapper(
        form, url_for('points_modify', point_id=point.id), "edición", url_for('points_index'), "Punto de encuentro", point.name, point.id
    )

    return render_template("points/edit.html", param_wrapper=param_wrapper)
    
def delete(point_id):
    """Permite eliminar puntos de encuentro."""
    assert_permit(session, "points_delete") 

    Meeting_Point.delete(point_id)
    
    return redirect(url_for("points_index"))