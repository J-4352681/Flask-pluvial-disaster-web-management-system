from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, PasswordField
from wtforms.validators import DataRequired

class UserFilter(FlaskForm): # Los atributos llevan el nombre de los métodos del modelo que realizan la query
    find_by_first_name = StringField("Nombre")
    find_by_last_name = StringField("Apellido")
    find_by_email = StringField("Email")
    find_by_username = StringField("Nickname")
    find_by_roles = StringField("Roles")
    submit = SubmitField("Aceptar")