from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length
from wtforms.widgets.html5 import ColorInput

class PaletteModificationForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(), Length(1,30,'El nombre debe tener entre 1 y 30 caracteres')]) # , Length(30)])
    color1 = StringField("Color primario", widget=ColorInput())
    color2 = StringField("Color secundario", widget=ColorInput())
    color3 = StringField("Color acento", widget=ColorInput())
    submit = SubmitField("Aceptar")
