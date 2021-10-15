from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length 

#from app.resources.colors import all

class Config_forms(FlaskForm):
    elements_per_page = IntegerField("Elementos por pagina", validators=[DataRequired()]) 
    sort_users = StringField("Criterio de ordenamiento de los usuarios", validators=[DataRequired()]) 
    sort_meeting_points = StringField("Criterio de ordenamiento de los puntos de encuentro", validators=[DataRequired()]) 
    #palette_private = SelectMultipleField("Colores de la aplicacion privada, elegir 3", choices=[], validators=[DataRequired()])
    private_color1 = SelectField("Color 1 de la aplicacion privada", coerce=int, validators=[DataRequired()])
    private_color2 = SelectField("Color 2 de la aplicacion privada", coerce=int, validators=[DataRequired()])
    private_color3 = SelectField("Color 3 de la aplicacion privada", coerce=int, validators=[DataRequired()])
    #palette_public = SelectMultipleField("Colores de la aplicacion publica, elegir 3", choices=[] , validators=[DataRequired()]) 
    public_color1 = SelectField("Color 1 de la aplicacion publica", coerce=int, validators=[DataRequired()])
    public_color2 = SelectField("Color 2 de la aplicacion publica", coerce=int, validators=[DataRequired()])
    public_color3 = SelectField("Color 3 de la aplicacion publica", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Aceptar") 
    