from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.widgets.html5 import ColorInput
from wtforms.validators import DataRequired, Length
from wtforms.widgets import HiddenInput

from app.models.flood_zone import FloodZone

from .validators import Unique

class FloodZoneForm(FlaskForm):
    code = StringField("Código de zona", validators=[DataRequired(), Length(1, 30, "El código debe de ser de entre 1 y 30 caracteres"), Unique(FloodZone, FloodZone.find_by_code)])
    name = StringField("Nombre de zona", validators=[DataRequired(), Length(1, 30, "El nombre debe de ser de entre 1 y 30 caracteres"), Unique(FloodZone, FloodZone.find_by_name)])
    state = BooleanField("Zona inundable activa")
    color = StringField(widget=ColorInput())
    coordinates = StringField("Área de la zona", validators=[DataRequired()])
    submit = SubmitField("Aceptar")

class FloodZoneModificationForm(FloodZoneForm):
    id = IntegerField(widget=HiddenInput())