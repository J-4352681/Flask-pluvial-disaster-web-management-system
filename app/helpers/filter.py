
class Filter():
    def __init__(self, filter_form_class, model, request_args):
        self._model = model
        self._filter_form_class = filter_form_class
        self._request_args = request_args
        self._form_query_fields = {k: v for k, v in request_args.items() if v != "" and k not in ["csrf_token", "submit"]}
    
    @property
    def model(self):
        return self._model
    
    @property
    def form(self):
        return self._filter_form_class(self._request_args)
    
    @property
    def form_query_fields(self):
        return self._form_query_fields
    
    def get_query(self):
        if self.form_query_fields:
            elements = []
            for k, v in self.form_query_fields.items():
                elements += getattr(self.model, k)(v)
            return elements
        return self.model.all()