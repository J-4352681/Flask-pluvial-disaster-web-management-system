from wtforms.validators import ValidationError
from app.models.user import User

class Unique(object):
    def __init__(self, model, query, message=u'Ya hay un elemento con este atributo y no puede haber repetidos'):
        self._model = model
        self._query = query
        self._message = message

    def __call__(self, form, field):
        form_data = form.data
        check = self._query(field.data, [form.id.data] if "id" in form_data.keys() and form_data["id"] else [])
        if check:
            raise ValidationError(self._message)