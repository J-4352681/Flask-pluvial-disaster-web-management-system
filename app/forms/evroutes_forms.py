from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length
from app.models.evacuation_route import EvacuationRoute

class EvacuationRouteForm(FlaskForm):
    name = StringField("Nombre de ruta", validators=[DataRequired(), Length(1,30,'El nombre debe de ser de entre 1 y 30 caracteres')])
    description = StringField("Descripcion", validators=[DataRequired(), Length(1,255,'La descripcion debe de contener de entre 1 y 255 caracteres')])
    state = BooleanField("Ruta de evacuación activa")
    coordinates = StringField("Área de la ruta", validators=[DataRequired()])
    submit = SubmitField("Aceptar")
