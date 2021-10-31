from typing import Dict
from flask import jsonify, Blueprint, request

from app.models.complaint import Complaint
from app.schemas.complaint import ComplaintSchema
from app.helpers.validators import ComplaintValidator


complaint_api = Blueprint("denuncias", __name__, url_prefix="/denuncias")

@complaint_api.post("/")
def create():
    data = ComplaintValidator(request.get_json()).validate()  # Siempre devuelve true, tiene que validar
    
    if data.error:
        response = data.error
    else:
        new_complaint = Complaint.create_public(**request.get_json())
        response = ComplaintSchema.dump(new_complaint)
    
    return jsonify(response)