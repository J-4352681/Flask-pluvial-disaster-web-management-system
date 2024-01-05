from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired

from app.models.complaint import Complaint
from app.models.user import User

class UserFilter(FlaskForm):
    first_name = StringField("Nombre")
    last_name = StringField("Apellido")
    email = StringField("Email")
    username = StringField("Username")
    roles = StringField("Roles")
    active = SelectField("Estado", choices=[("", "Todos")]+User.get_active_states())
    submit = SubmitField("Aceptar")

class PointFilter(FlaskForm):
    name = StringField("Nombre")
    state = SelectField("Público", choices=[("", "Todos"), (1, "Si"), (0, "No")])
    submit = SubmitField("Aceptar")

class FZoneFilter(FlaskForm):
    code = IntegerField("Código de zona")
    name = StringField("Nombre de zona")
    state = SelectField("Público", choices=[('', 'Todos'), (1, 'Si'), (0, 'No')])
    submit = SubmitField("Aceptar")

class EvRouteFilter(FlaskForm):
    name = StringField("Nombre de ruta")
    state = SelectField("Público", choices=[('', 'Todos'), (1, 'Si'), (0, 'No')])
    submit = SubmitField("Aceptar")

class ComplaintFilter(FlaskForm):
    title = StringField("Título de la denuncia")
    state = SelectField("Estado", choices=[("", "Todos")]+Complaint.get_states())
    first_date = DateField("Rango: Fecha de inicio")
    last_date = DateField("Rango: Fecha de fin")

class PaletteFilter(FlaskForm):
    name = StringField("Nombre")
    submit = SubmitField("Aceptar")
