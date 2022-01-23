from pstats import Stats
from flask import jsonify, Blueprint, request, abort
from app.models.statistics import Statistics, Complaint
from app.schemas.statistics import StatisticsFetchSchema
import logging
logger = logging.getLogger(__name__) 

statistics_api = Blueprint("estadisticas", __name__, url_prefix="/estadisticas")

@statistics_api.get("/by-category")
def fetch_all():

    try:
        statistics = Statistics.count()
    except:
        logger.exception("Error al traer la informacion sobre las estadisticas.")
        abort(500)

    if statistics: 
        return jsonify(stats = statistics)
    else:
        abort(404)