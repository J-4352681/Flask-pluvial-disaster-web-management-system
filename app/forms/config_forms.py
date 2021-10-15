from typing import DefaultDict
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

from flask import flash
#from app.resources.colors import all

#def my_length_check(form, field):
#    if len(field.data) > 50:
#        raise ValidationError('Field must be less than 50 characters')
class Config_forms(FlaskForm):
    elements_per_page = IntegerField("Elementos por pagina (no puede ser 0)", validators=[DataRequired(), NumberRange(1, None, 'No pueden haber 0 elementos por pagina')])
    sort_users = SelectField("Criterio de ordenamiento de los usuarios", validators=[DataRequired()], choices=['username', 'first_name', 'last_name', 'email']) 
    sort_meeting_points = SelectField("Criterio de ordenamiento de los puntos de encuentro", validators=[DataRequired()], choices=['name', 'direction', 'coordinates', 'telephone', 'email']) 
    #palette_private = SelectMultipleField("Colores de la aplicacion privada, elegir 3", coerce=int, validators=[DataRequired()])
    private_color1 = SelectField("Color 1 de la aplicacion privada", coerce=int, validators=[DataRequired()])
    private_color2 = SelectField("Color 2 de la aplicacion privada", coerce=int, validators=[DataRequired()])
    private_color3 = SelectField("Color 3 de la aplicacion privada", coerce=int, validators=[DataRequired()])
    #palette_public = SelectMultipleField("Colores de la aplicacion publica, elegir 3", choices=[] , validators=[DataRequired()]) 
    public_color1 = SelectField("Color 1 de la aplicacion publica", coerce=int, validators=[DataRequired()])
    public_color2 = SelectField("Color 2 de la aplicacion publica", coerce=int, validators=[DataRequired()])
    public_color3 = SelectField("Color 3 de la aplicacion publica", coerce=int, validators=[DataRequired()])
    submit = SubmitField("Aceptar") 

    def validate(self):
        if not super().validate():
            return False
        result = True
        seen = set()
        for field in [self.private_color1, self.private_color2, self.private_color3]:
            if field.data in seen:
                field.errors.append('Debe elegir 3 colores distintos para cada app.')
                flash('ERROR')
                result = False
            else:
                seen.add(field.data)
        
        seen1 = set()
        for field in [self.public_color1, self.public_color2, self.public_color3]:
            if field.data in seen1:
                field.errors.append('Debe elegir 3 colores distintos para cada app.')
                flash('ERROR')
                result = False
            else:
                seen1.add(field.data)
        return result