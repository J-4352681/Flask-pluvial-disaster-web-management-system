from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.widgets.html5 import ColorInput
from wtforms.validators import DataRequired, Length
from app.models.flood_zone import FloodZone

class EvacuationRouteForm(FlaskForm):
    code = StringField("Código de zona", validators=[DataRequired(), Length(1,30,'El apellido debe de ser de entre 1 y 30 caracteres')])
    name = StringField("Nombre de zona", validators=[DataRequired(), Length(1,30,'El apellido debe de ser de entre 1 y 30 caracteres')])
    state = BooleanField("Zona inundable activa")
    color = StringField(widget=ColorInput())
    coordinates = StringField("Área de la zona", validators=[DataRequired()])
    submit = SubmitField("Aceptar")