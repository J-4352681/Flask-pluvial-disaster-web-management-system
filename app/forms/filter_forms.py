from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class UserFilter(FlaskForm): # Los atributos llevan el nombre de los métodos del modelo que realizan la query
    find_by_first_name = StringField("Nombre")
    find_by_last_name = StringField("Apellido")
    find_by_email = StringField("Email")
    find_by_username = StringField("Username")
    find_by_roles = StringField("Roles")
    find_by_permits = StringField("Permiso")
    find_all_active_or_blocked = SelectField("Estado", choices=[(1, 'Activo'), (0, 'Bloqueado')])
    submit = SubmitField("Aceptar")

class PointFilter(FlaskForm):
    submit = SubmitField("Aceptar")