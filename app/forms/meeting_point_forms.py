from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class MeetingPointModificationForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(), Length(1,30,'El nombre debe de ser de entre 1 y 30 caracteres')]) # , Length(30)])
    direction = StringField("Direccion", validators=[DataRequired(), Length(1,100,'La direccion debe de ser de entre 1 y 100 caracteres')]) # , Length(100)])
    coordinates = StringField("Coordenadas", validators=[DataRequired(), Length(1,100,'Las coordenadas debe de ser de entre 1 y 100 caracteres')]) # , Length(100)])
    telephone = StringField("Telefono", validators=[DataRequired(), Length(1,30,'El telefono debe de ser de entre 1 y 30 caracteres')])
    email = StringField("E-mail", validators=[DataRequired(), Length(1,100,'El email debe de ser de entre 1 y 100 caracteres'), Email()]) # , Email()]) # "Install 'email_validator' for email validation support."
    state = BooleanField("Publicado", validators=[DataRequired()])
    submit = SubmitField("Aceptar") 
    