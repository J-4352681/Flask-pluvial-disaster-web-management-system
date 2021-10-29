from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, PasswordField, BooleanField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length

class MeetingPointModificationForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(), Length(1,30,'El nombre debe de ser de entre 1 y 30 caracteres')]) # , Length(30)])
    direction = StringField("Dirección", validators=[DataRequired(), Length(1,100,'La direccion debe de ser de entre 1 y 100 caracteres')]) # , Length(100)])
    # coordinates = StringField("Coordenadas", validators=[DataRequired(), Length(1,100,'Las coordenadas debe de ser de entre 1 y 100 caracteres')]) # , Length(100)])
    latitude = IntegerField("Latitud", validators=[DataRequired()])
    longitude = IntegerField("Longitud", validators=[DataRequired()])
    telephone = StringField("Teléfono", validators=[DataRequired(), Length(1,30,'El telefono debe de ser de entre 1 y 30 caracteres')])
    email = EmailField("E-mail", validators=[DataRequired(), Length(1,100,'El email debe de ser de entre 1 y 100 caracteres')])
    state = BooleanField("Publicado", default="checked")
    submit = SubmitField("Aceptar") 
    