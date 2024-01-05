from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class FollowUpForm(FlaskForm):
    description = StringField("Descripcion", validators=[DataRequired(), Length(1,255,'La descripcion debe de contener de entre 1 y 255 caracteres')])
    submit = SubmitField("Aceptar") 
    