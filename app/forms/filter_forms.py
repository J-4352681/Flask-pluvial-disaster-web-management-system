from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, PasswordField
from wtforms.validators import DataRequired

class UserFilter(FlaskForm):
    first_name = StringField("Nombre del usuario")
    last_name = StringField("Apellido del usuario")
    email = StringField("Email del usuario")
    username = StringField("Nickname del usuario")
    # roles = SelectField("Roles", choices=[role.name for role in Role.query.all()])
    submit = SubmitField("Aceptar")