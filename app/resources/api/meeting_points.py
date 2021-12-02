from flask import jsonify, Blueprint, request, abort
from app.models.meeting_point import MeetingPoint
from app.schemas.meeting_points import MeetingPointsPaginationSchema, MeetingPointsSchema
import logging
logger = logging.getLogger(__name__) 

meeting_points_api = Blueprint("meeting_points", __name__, url_prefix="/puntos-encuentro")

@meeting_points_api.get("/")
def index():
    page = request.args.get("page", "1")

    try:
        page = int(page)
        meeting_points_page = MeetingPoint.all_paginated(page)
    except:
        logger.exception("Error al traer la informacion sobre puntos de encuentro.")
        abort(500)

    if meeting_points_page.items: 
        meeting_points = MeetingPointsPaginationSchema().dump(meeting_points_page)
        return jsonify(meeting_points)
    else:
        abort(404)