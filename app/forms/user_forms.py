from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, PasswordField, IntegerField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets import HiddenInput
from app.models.user import User
from .forms import Unique

class UserModificationForm(FlaskForm):
    id = IntegerField(widget=HiddenInput())
    first_name = StringField("Nombre del usuario", validators=[DataRequired()])
    last_name = StringField("Apellido del usuario", validators=[DataRequired()])
    email = StringField("Email del usuario", validators=[DataRequired(), Unique(User, User.find_by_email_exact)])
    username = StringField("Username del usuario", validators=[DataRequired(), Unique(User, User.find_by_username_exact)])
    # roles = SelectMultipleField("Roles", choices=[role.name for role in Role.query.all()])
    submit = SubmitField("Aceptar")