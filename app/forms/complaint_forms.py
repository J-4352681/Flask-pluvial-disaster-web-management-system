from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField, SelectField, DateTimeField
from wtforms.fields.html5 import EmailField
from wtforms.widgets.html5 import ColorInput
from wtforms.validators import DataRequired, Length

from app.models.complaint import Complaint
from app.models.category import Category
from app.models.user import User

from app.forms.fields import NonValidatingSelectField

class ComplaintForm(FlaskForm):
    title = StringField("Título de la denuncia", validators=[DataRequired(), Length(1, 255, "El título debe de ser de entre 1 y 255 carácteres")])
    # closure_date = DateTimeField("Fecha de cierre (dd/mm/aaaa hh:mm)", format="%d/%m/%Y %H:%M")
    description = StringField("Descripción de la denuncia", validators=[DataRequired(), Length(1, 255, "La descripción debe de ser de entre 1 y 255 carácteres")])
    coordinates = StringField("Área de la denuncia", validators=[DataRequired()])
    state = SelectField("Estado de la denuncia", choices=Complaint.get_states(), validators=[DataRequired()])
    category = SelectField("Categoría de la denuncia", choices=[], validators=[DataRequired()])
    assigned_user = SelectField("Usuario asignado a al denuncia", choices=[], validators=[DataRequired()])
    author_first_name = StringField("Nombre del autor de la denuncia", validators=[DataRequired(), Length(1, 30, "El nombre del autor debe de ser de entre 1 y 30 carácteres")])
    author_last_name = StringField("Apellido del autor de la denuncia", validators=[DataRequired(), Length(1, 30, "El apellido del autor debe de ser de entre 1 y 30 carácteres")])
    author_telephone = StringField("Número de teléfono del autor de la denuncia", validators=[DataRequired(), Length(1, 30, "El número de teléfono del autor debe de ser de entre 1 y 30 carácteres")])
    author_email = EmailField("Email del autor de la denuncia", validators=[DataRequired(), Length(1, 100, "El email del autor de la denuncia debe de ser de entre 1 y 100 caracteres")])
    submit = SubmitField("Aceptar")