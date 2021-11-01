from typing import Dict
from flask import jsonify, Blueprint, request, abort
from marshmallow import ValidationError

from app.models.complaint import Complaint
from app.schemas.complaint import ComplaintSchema


complaint_api = Blueprint("denuncias", __name__, url_prefix="/denuncias")

@complaint_api.post("/")
def create():
    
    try:
        ComplaintSchema().load(request.get_json())
    except ValidationError as err:
        abort(400)

    try:
        new_complaint = Complaint.create_public(**request.get_json())
    except:
        abort(500)
    
    response = ComplaintSchema().dump(new_complaint)
    
    return jsonify(response), 201