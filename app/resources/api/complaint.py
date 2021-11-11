from typing import Dict
from flask import jsonify, Blueprint, request, abort
from marshmallow import ValidationError

from app.models.complaint import Complaint
from app.schemas.complaint import ComplaintSchema

import logging
logger = logging.getLogger(__name__) # Nos permite devolver mas informacion sobre una excepcion en el servidor.

complaint_api = Blueprint("denuncias", __name__, url_prefix="/denuncias")

@complaint_api.post("/")
def create():
    
    try:
        input_args = ComplaintSchema().load(request.get_json())
    except ValidationError as err:
        abort(400)

    try:
        new_complaint = Complaint.create_public(**input_args)
    except:
        logger.exception("Error creando denuncia.")  # Imprime todo el traceback del error
        abort(500)
    
    response = ComplaintSchema().dump(new_complaint)
    
    return jsonify(atributos=response), 201
