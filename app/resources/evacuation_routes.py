from flask import redirect, render_template, request, url_for, session, abort
from sqlalchemy.sql.expression import false, true
from json import loads

from app.models.evacuation_route import EvacuationRoute
from app.helpers.auth import assert_permit
from app.helpers.filter import Filter
from app.helpers.template_pages import FormPage, DBModelIndexPage, ItemDetailsPage
from app.forms.filter_forms import EvRouteFilter
from app.forms.evroutes_forms import EvacuationRouteForm

# Protected resources
def index(page=None):
    """Muestra la lista de recorridos de evacuación."""
    assert_permit(session, "evroutes_index")

    filt = Filter(EvRouteFilter, EvacuationRoute, request.args)

    temp_interface = DBModelIndexPage(
        filt, page,
        title="Administración de recorridos de evacuación",
        subtitle="Administración, adición y eliminación de los recorridos de evacuación del sitio"
    )
    
    return render_template("evacuation_routes/pages/index.html", temp_interface=temp_interface)

def show(evroute_id):
    """Muestra la lista de recorridos de evacuación."""
    assert_permit(session, "evroutes_show")

    evroute = EvacuationRoute.find_by_id(evroute_id)
    
    temp_interface = ItemDetailsPage(
        {
        "Nombre": evroute.name,
        "Descripción": evroute.description,
        "Coordenadas": evroute.coordinates,
        "Público": evroute.state,
        }, evroute,
        title="Recorrido de evacuación", subtitle="Detalles del recorrido " + str(evroute.name)
    )
    
    return render_template("evacuation_routes/pages/show.html", temp_interface=temp_interface)

def create():
    return

def modify(evroute_id):
    """Modifica los datos de una denuncia."""
    assert_permit(session, "evroutes_modify")

    evroute = EvacuationRoute.find_by_id(evroute_id)
    form = EvacuationRouteForm(obj=evroute)

    if form.validate_on_submit():
        form.populate_obj(evroute)
        evroute.coordinates = loads(evroute.coordinates)
        EvacuationRoute.update()
        return redirect(url_for('evroutes_index'))

    temp_interface = FormPage(
        form, url_for("evroutes_modify", evroute_id=evroute.id),
        title="Edición de ruta de evacuación", subtitle="Editando la ruta de evacuación "+str(evroute.name),
        return_url=url_for('evroutes_index')
    )
    
    return render_template("generic/pages/zone_form.html", temp_interface=temp_interface)

def delete(evroute_id):
    return