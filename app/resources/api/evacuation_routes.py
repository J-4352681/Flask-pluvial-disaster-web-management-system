from flask import jsonify, Blueprint, request, abort
from app.models.evacuation_route import EvacuationRoute
from app.schemas.evacuation_routes import EvacuationRoutesPaginationSchema, EvacuationRoutesSchema
import logging
logger = logging.getLogger(__name__) 

evacuation_routes_api = Blueprint("evacuation_routes", __name__, url_prefix="/recorridos-evacuacion")

@evacuation_routes_api.get("/")
def index():
    page = request.args.get("page", "1")

    try:
        page = int(page)
        evacuation_routes_page = EvacuationRoute.all_paginated(page)
    except:
        logger.exception("Error al traer la informacion sobre rutas de evacuacion.")
        abort(500)

    if evacuation_routes_page.items: 
        evacuation_routes = EvacuationRoutesPaginationSchema().dump(evacuation_routes_page)
        return jsonify(evacuation_routes)
    else:
        abort(404)

@evacuation_routes_api.get("/all")
def fetch_all():

    try:
        evacuation_routes_all = EvacuationRoute.all_public()
    except:
        logger.exception("Error al traer la informacion sobre rutas de evacuacion.")
        abort(500)

    if evacuation_routes_all: 
        evacuation_routes = EvacuationRoutesSchema(many=True).dump(evacuation_routes_all)
        return jsonify(routes = evacuation_routes)
    else:
        abort(404)
