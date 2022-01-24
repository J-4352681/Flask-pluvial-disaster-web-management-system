from pstats import Stats
from flask import jsonify, Blueprint, request, abort
from flask_cors import cross_origin
from app.models.statistics import Statistics, Complaint, Category
from app.schemas.statistics import StatisticsFetchSchema
import logging
logger = logging.getLogger(__name__) 

statistics_api = Blueprint("estadisticas", __name__, url_prefix="/estadisticas")

@statistics_api.get("/by-category")
@cross_origin()
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

@statistics_api.get("/by-user")
@cross_origin()
def fetch_all_users():

    try:
        statistics = Statistics.count_by_user()
        print(statistics)
    except:
        logger.exception("Error al traer la informacion sobre las estadisticas.")
        abort(500)

    if statistics: 
        return jsonify(stats = statistics)
    else:
        abort(404)