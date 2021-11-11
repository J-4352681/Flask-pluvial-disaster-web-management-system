from typing import Dict
from flask import jsonify, Blueprint, request, abort
from marshmallow import ValidationError

from app.models.complaint import Complaint
from app.schemas.complaint import ComplaintSchema

<<<<<<< HEAD
=======
import logging
logger = logging.getLogger(__name__) # Nos permite devolver mas informacion sobre una excepcion en el servidor.
>>>>>>> development

complaint_api = Blueprint("denuncias", __name__, url_prefix="/denuncias")

@complaint_api.post("/")
def create():
    
    try:
<<<<<<< HEAD
        ComplaintSchema().load(request.get_json())
=======
        input_args = ComplaintSchema().load(request.get_json())
>>>>>>> development
    except ValidationError as err:
        abort(400)

    try:
<<<<<<< HEAD
        new_complaint = Complaint.create_public(**request.get_json())
    except:
=======
        new_complaint = Complaint.create_public(**input_args)
    except:
        logger.exception("Error creando denuncia.")  # Imprime todo el traceback del error
>>>>>>> development
        abort(500)
    
    response = ComplaintSchema().dump(new_complaint)
    
<<<<<<< HEAD
    return jsonify(response), 201
=======
    return jsonify(atributos=response), 201
>>>>>>> development
