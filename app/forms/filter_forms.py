from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class UserFilter(FlaskForm): # Los atributos llevan el nombre de los métodos del modelo que realizan la query
    first_name = StringField("Nombre")
    last_name = StringField("Apellido")
    email = StringField("Email")
    username = StringField("Username")
    roles = StringField("Roles")
    active = SelectField("Estado", choices=[('', 'Todos'), (1, 'Activo'), (0, 'Bloqueado')])
    submit = SubmitField("Aceptar")

class PointFilter(FlaskForm):
    name = StringField("Nombre")
    state = SelectField("Público", choices=[('', 'Todos'), (1, 'Si'), (0, 'No')])
    submit = SubmitField("Aceptar")