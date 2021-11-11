from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired

class UserFilter(FlaskForm):
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

class FZoneFilter(FlaskForm):
    code = IntegerField("Código de zona")
    name = StringField("Nombre de zona")
<<<<<<< HEAD
    state = StringField("Público", choices=[('', 'Todos'), (1, 'Si'), (0, 'No')])
=======
    state = SelectField("Público", choices=[('', 'Todos'), (1, 'Si'), (0, 'No')])
>>>>>>> development
    submit = SubmitField("Aceptar")