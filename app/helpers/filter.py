from app.resources.config import get as config_get
from app.models.user import User
from app.models.meeting_point import MeetingPoint
from app.models.flood_zone import FloodZone
from app.models.evacuation_route import EvacuationRoute


class Filter():
    def __init__(self, filter_form_class, model, request_args):
        self._model = model
        self._filter_form_class = filter_form_class
        self._request_args = request_args
        self._form_query_fields = {k: v for k, v in request_args.items() if v != '' and k not in ["csrf_token", "submit", "page"]}
        self._config = config_get()
    
    @property
    def model(self):
        return self._model

    @property
    def config(self):
        return self._config
    
    @property
    def form(self):
        return self._filter_form_class(self._request_args)
    
    @property
    def form_query_fields(self):
        return self._form_query_fields

    def get_query(self, page):
        if self.form_query_fields:
            query = self.model.query.order_by(self.get_default_sort_criteria()).filter_by(**self.form_query_fields)
        else:
            query = self.model.query.order_by(self.get_default_sort_criteria())

        return query.paginate(page=page, per_page=self.config.elements_per_page)

    def get_default_sort_criteria(self):
        if self.model == User:
            criteria = self.config.sort_users
        elif self.model == MeetingPoint:
            criteria = self.config.sort_meeting_points
        elif self.model == FloodZone:
            criteria = self.config.sort_flood_zones
        elif self.model == EvacuationRoute:
            criteria = self.config.sort_evacuation_routes

        return criteria

    def has_filter(self):
        return bool(self.form_query_fields)
