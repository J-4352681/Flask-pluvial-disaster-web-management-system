from flask import redirect, render_template, request, url_for, session, abort
from sqlalchemy.sql.expression import false, true

from app.models.meeting_point import MeetingPoint

from app.helpers.auth import assert_permit
from app.helpers.filter import Filter
from app.helpers.template_pages import FormPage, DBModelIndexPage, ItemDetailsPage

from app.forms.filter_forms import PointFilter
from app.forms.point_forms import MeetingPointModificationForm

# Protected resources
def index(page=None):
    """Muestra la lista de puntos de encuentro."""
    assert_permit(session, "points_index")

    #points = allPublic()
    filt = Filter(PointFilter, MeetingPoint, request.args)

    temp_interface = DBModelIndexPage(
        filt, page,
        title="Administración de puntos de encuentro",
        subtitle="Administración, adición y eliminación de los puntos de encuentro del sitio"
    )
    
    return render_template("points/pages/index.html", temp_interface=temp_interface)

def show(point_id):
    """Muestra la lista de puntos de encuentro."""
    assert_permit(session, "points_show")

    point = MeetingPoint.find_by_id(point_id)
    
    temp_interface = ItemDetailsPage(
        {
          "Nombre": point.name,
          "Dirección": point.direction,
          "Coordenadas": point.coordinates,
          "Público": point.state,
          "Teléfono": point.telephone,
          "E-Mail": point.email
        }, point,
        title="Puntos de encuentro", subtitle="Detalles del punto " + str(point.name),
        return_url=url_for("points_index"),
        edit_url=url_for("points_modify", point_id=point.id),
        delete_url=url_for("points_delete", point_id=point.id)
    )
    
    return render_template("generic/pages/item_details.html", temp_interface=temp_interface)

def allPublic():
    """Devuelve la lista completa de los puntos de encuentro publicos gurdados en la base de datos."""
    return MeetingPoint.allPublic()

def allNotPublic():
    """Devuelve la lista completa de los puntos de encuentro no publicos gurdados en la base de datos."""
    return MeetingPoint.allNotPublic()

def all():
    """Devuelve la lista completa de los puntos de encuentro gurdados en la base de datos."""
    return MeetingPoint.all()

def new():
    """Devuelve el template para crear un nuevo punto de encuentro."""
    assert_permit(session, "points_new")
    form = MeetingPointModificationForm()

    if form.validate_on_submit():
        create(form.name.data, form.direction.data, form.latitude.data, form.longitude.data, form.telephone.data, form.email.data, form.state.data)
        return redirect(url_for('points_index'))
    else:
        temp_interface = FormPage(
            form, url_for("points_new"),
            title="Creación de punto de encuentro", subtitle="Creando un nuevo punto de encuentro",
            return_url=url_for('points_index')
        )

        return render_template("generic/pages/form.html", temp_interface=temp_interface)

def create(name, direction, latitude, longitude, telephone, email, state):
    """Crea un punto de encuentro con los datos envuados por request."""
    assert_permit(session, "points_create")

    MeetingPoint.create(name, direction, latitude, longitude, telephone, email, state)# **request.form)

def modify(point_id):
    """Modifica los datos de un usuario."""
    assert_permit(session, "points_modify")
    point = MeetingPoint.find_by_id(point_id)
    form = MeetingPointModificationForm(obj=point,
        latitude = point.coordinates[0],
        longitude = point.coordinates[1])

    if form.validate_on_submit():
        form.populate_obj(point)
        MeetingPoint.updateCoordinates(point, form.latitude.data,form.longitude.data) #Agregado por Tomi
        MeetingPoint.update()
        return redirect(url_for('points_index'))
    
    temp_interface = FormPage(
        form, url_for("points_modify", point_id=point.id),
        title="Edición de punto de encuentro", subtitle="Editando el punto de encuentro "+str(point.name),
        return_url=url_for('points_index')
    )

    return render_template("generic/pages/form.html", temp_interface=temp_interface)
    
def delete(point_id):
    """Permite eliminar puntos de encuentro."""
    assert_permit(session, "points_delete") 

    MeetingPoint.delete(point_id)
    
    return redirect(url_for("points_index"))
