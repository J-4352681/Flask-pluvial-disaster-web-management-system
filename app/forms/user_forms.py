from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, PasswordField
from wtforms.validators import DataRequired

# from app.models.role import Role


class UserModificationForm(FlaskForm):
    first_name = StringField("Nombre del usuario", validators=[DataRequired()])
    last_name = StringField("Apellido del usuario", validators=[DataRequired()])
    email = StringField("Email del usuario", validators=[DataRequired()])
    username = StringField("Nickname del usuario", validators=[DataRequired()])
    # roles = SelectMultipleField("Roles", choices=[role.name for role in Role.query.all()])
    submit = SubmitField("Aceptar")