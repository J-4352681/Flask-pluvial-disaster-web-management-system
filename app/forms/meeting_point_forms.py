from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length # , Email

class MeetingPointModificationForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired()]) # , Length(30)])
    direction = StringField("Direccion", validators=[DataRequired()]) # , Length(100)])
    coordinates = StringField("Coordenadas", validators=[DataRequired()]) # , Length(100)])
    telephone = StringField("Telefono", validators=[DataRequired()])
    email = StringField("E-mail", validators=[DataRequired()]) # , Email()]) # "Install 'email_validator' for email validation support."
    state = BooleanField("Publicado", validators=[DataRequired()])
    submit = SubmitField("Aceptar") 
    