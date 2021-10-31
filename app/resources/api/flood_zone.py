from typing import Dict
from flask import jsonify, Blueprint, request

from app.models.flood_zone import Flood_zone
from app.schemas.flood_zone import FloodZoneSchema


flood_zone_api = Blueprint("zonas_inundables", __name__, url_prefix="/zonas_inundables")

@flood_zone_api.get("/")
def index():
    page = request.args.get("page", 1)
    flood_zone_rows = Flood_zone.all_paginated(int(page)).items

    if flood_zone_rows: 
        flood_zones = FloodZoneSchema.dump(flood_zone_rows, many=True)
        return jsonify(flood_zones=flood_zones)
    else:
        return jsonify(flood_zones=[]), 401

@flood_zone_api.get("/:id")
def fetch_by_id():
    pass