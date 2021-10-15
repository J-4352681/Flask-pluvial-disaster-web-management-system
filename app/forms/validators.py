from wtforms.validators import ValidationError
from app.models.user import User

class Unique(object):
    def __init__(self, model, query, message=u'Ya hay un elemento con este atributo y no puede haber repetidos'):
        self._model = model
        self._query = query
        self._message = message

    def __call__(self, form, field):
        check = self._query(field.data, [form.id.data] if form.id.data else [])
        if check:
            raise ValidationError(self._message)