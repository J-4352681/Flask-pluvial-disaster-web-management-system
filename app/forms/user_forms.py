from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, ValidationError, EqualTo, Length
from wtforms.widgets import HiddenInput
from app.models.user import User
from .validators import Unique
from app.models.role import Role
from app.forms.fields import NonValidatingSelectMultipleField


class UserForm(FlaskForm):
    first_name = StringField("Nombre del usuario", validators=[DataRequired(), Length(1,30,'El nombre debe de ser de entre 1 y 30 caracteres')])
    last_name = StringField("Apellido del usuario", validators=[DataRequired(), Length(1,30,'El apellido debe de ser de entre 1 y 30 caracteres')])
    email = EmailField("Email del usuario", validators=[DataRequired(), Length(1,30,'El email debe de ser de entre 1 y 30 caracteres'), Unique(User, User.find_by_email_exact)])
    username = StringField("Username del usuario", validators=[DataRequired(), Length(1,30,'El username debe de ser de entre 1 y 30 caracteres'), Unique(User, User.find_by_username_exact)])
    roles = NonValidatingSelectMultipleField("Roles", filters=[lambda x: Role.get_by_ids([int(i) for i in x])])
    active = BooleanField("Usuario activo")
    submit = SubmitField("Aceptar")

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.roles.choices = {role.id: role.name for role in Role.all()}
        self.roles.default = []


class UserModificationForm(UserForm):
    id = IntegerField(widget=HiddenInput())

    def __init__(self, *args, **kwargs):
        super(UserModificationForm, self).__init__(*args, **kwargs)
        self.roles.default = [role.id for role in User.find_by_id(kwargs["obj"].id).roles]


class UserCreationForm(UserForm):
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(1,30,'El nombre debe de ser de entre 1 y 30 caracteres')])
    confirm_password = PasswordField("Confirmar contraseña", validators=[DataRequired(), Length(1,30,'El nombre debe de ser de entre 1 y 30 caracteres'), EqualTo("password"),])
    submit = SubmitField("Aceptar")