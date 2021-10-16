from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, PasswordField, IntegerField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from wtforms.widgets import HiddenInput
from app.models.user import User
from .validators import Unique
from app.models.role import Role


class NonValidatingSelectMultipleField(SelectMultipleField):
    """
    Selector de múltiples campos/alternativas sin validación
    de ingreso de datos y carga de datos en dummy funcional 
    """

    def pre_validate(self, form):
        """Hace una prevalidación de los datos ingresados"""
        pass


class UserModificationForm(FlaskForm):
    id = IntegerField(widget=HiddenInput())
    first_name = StringField("Nombre del usuario", validators=[DataRequired()])
    last_name = StringField("Apellido del usuario", validators=[DataRequired()])
    email = StringField("Email del usuario", validators=[DataRequired(), Unique(User, User.find_by_email_exact)])
    username = StringField("Username del usuario", validators=[DataRequired(), Unique(User, User.find_by_username_exact)])
    roles = NonValidatingSelectMultipleField("Roles", filters=[lambda x: Role.get_by_ids(x)])
    submit = SubmitField("Aceptar")

    def __init__(self, *args, **kwargs):
        super(UserModificationForm, self).__init__(*args, **kwargs)
        self.roles.choices = {role.id: role.name for role in Role.all()}
        self.roles.default = [role.id for role in User.find_by_id(kwargs["obj"].id).roles]


class UserCreationForm(UserModificationForm):
    password = PasswordField("Contraseña", validators=[DataRequired()])
    confirm_password = PasswordField("Confirmar contraseña", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Aceptar")