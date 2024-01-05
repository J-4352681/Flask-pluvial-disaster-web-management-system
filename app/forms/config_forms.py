from typing import DefaultDict
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from wtforms.widgets.html5 import ColorInput

from app.models.config import Config
from app.models.palette import Palette
from app.models.user import User
from app.models.meeting_point import MeetingPoint
from app.models.flood_zone import FloodZone
from app.models.complaint import Complaint
from app.models.evacuation_route import EvacuationRoute

from app.forms.fields import NonValidatingSelectField

from flask import flash

class ConfigForm(FlaskForm):
    elements_per_page = IntegerField("Elementos por pagina (no puede ser 0)", validators=[DataRequired(), NumberRange(1, None, 'No pueden haber 0 elementos por pagina')])
    sort_users = SelectField("Criterio de ordenamiento de los usuarios", validators=[DataRequired()], choices=[])
    sort_meeting_points = SelectField("Criterio de ordenamiento de los puntos de encuentro", validators=[DataRequired()], choices=[])
    sort_flood_zones = SelectField("Criterio de ordenamiento de las zonas inundables", validators=[DataRequired()], choices=[])
    sort_evacuation_routes = SelectField("Criterio de ordenamiento de las rutas de evacuacion", validators=[DataRequired()], choices=[])
    sort_complaints = SelectField("Criterio de ordenamiento de las denuncias", validators=[DataRequired()], choices=[])
    sort_palettes = SelectField("Criterio de ordenamiento de las paletas", validators=[DataRequired()], choices=[])
    palette_public = SelectField("Paleta de colores de la app pública", validators=[DataRequired()], choices=[], coerce=int)
    palette_private = SelectField("Paleta de colores de la app privada", validators=[DataRequired()], choices=[], coerce=int)

    submit = SubmitField("Aceptar")

    def __init__(self, *args, **kwargs):
        super(ConfigForm, self).__init__(*args, **kwargs)

        config = Config.get_current_config()
        palettes = list(map(lambda p: (p.id, p.name), Palette.all()))

        self.palette_public.choices = palettes
        self.palette_public.data = config.palette_public_id
        # self.palette_public.default = config.palette_public_id

        self.palette_private.choices = palettes
        self.palette_private.data = config.palette_private_id
        # self.palette_private.default = config.palette_private_id

        self.sort_users.choices = User.get_sorting_atributes()
        self.sort_meeting_points.choices = MeetingPoint.get_sorting_atributes()
        self.sort_flood_zones.choices = FloodZone.get_sorting_atributes()
        self.sort_evacuation_routes.choices = EvacuationRoute.get_sorting_atributes()
        self.sort_complaints.choices = Complaint.get_sorting_atributes()
        self.sort_palettes.choices = Palette.get_sorting_atributes()
