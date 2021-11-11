from flask import jsonify, Blueprint, request, abort

from app.models.flood_zone import FloodZone
from app.schemas.flood_zone import FloodZonePaginationSchema, FloodZoneSchema

import logging
logger = logging.getLogger(__name__) # exception, info, error, warning. Nos permite devolver mas informacion sobre una excepcion en el servidor. # 

flood_zone_api = Blueprint("zonas_inundables", __name__, url_prefix="/zonas_inundables")

@flood_zone_api.get("/")
def index():
    page = request.args.get("page", "1")

    try:
        page = int(page)
        flood_zone_page = FloodZone.all_paginated(page)
    except:
        logger.exception("Error al traer la informacion sobre zonas inundables.")
        abort(500)

    if flood_zone_page.items: 
        flood_zones = FloodZonePaginationSchema().dump(flood_zone_page)
        return jsonify(flood_zones)
    else:
        abort(404)

@flood_zone_api.get("/<id>")
def fetch_by_id(id):
    try:
        flood_zone = FloodZone.find_by_id(id)
    except:
        logger.exception("Error encontrando la zona inundable.")
        abort(500)
    
    if flood_zone:
        return jsonify(atributos=FloodZoneSchema().dump(flood_zone))
    else:
        abort(404)