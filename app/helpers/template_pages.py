class NamedPage():
    """Interfaz paramétrica base de página nombrada"""
    def __init__(self, name=None):
        self._name = name


    @property
    def name(self):
        return self._name


class TitledPage(NamedPage):
    """Interfaz paramétrica base de página con título y subtítulo"""
    def __init__(self, title, subtitle, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._title = title
        self._subtitle = subtitle
        if not self._name: self._name=title


    @property
    def title(self):
        return self._title


    @property
    def subtitle(self):
        return self._subtitle


class TitledBackPage(TitledPage):
    """Interfaz paramétrica base de página de con título y botón de regreso"""
    def __init__(self, return_url, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._return_url = return_url


    @property
    def return_url(self):
        return self._return_url


class FormPage(TitledBackPage):
    """Interfaz paramétrica para una página de template con formulario"""
    def __init__(self, form, action_url, method="POST", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._form = form
        self._action_url = action_url
        self._method = method


    @property
    def form(self):
        return self._form


    @property
    def action_url(self):
        return self._action_url


    @property
    def method(self):
        return self._method


class ItemDetailsPage(TitledBackPage):
    """Interfaz paramétrica para una página que muestra los detalles de un item de la db."""
    def __init__(self, attributes, item, edit_url=None, delete_url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._attributes = attributes
        self._item = item
        self._edit_url = edit_url
        self._delete_url = delete_url


    @property
    def attributes(self):
        return self._attributes


    @property
    def item(self):
        return self._item


    @property
    def edit_url(self):
        return self._edit_url


    @property
    def delete_url(self):
        return self._delete_url


class DBModelIndexPage(TitledPage):
    """Interfaz paramétrica para una página para el listado de un modelo de la db"""
    def __init__(self, filt, page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._filt = filt
        self._page = self._filt.get_query(page)


    @property
    def page(self):
        return self._page


    @property
    def filt(self):
        return self._filt


class SubDBModelIndexPage(TitledBackPage):
    """Interfaz paramétrica base de página de con título y botón de regreso de un elemento relacionado a otro de la bd"""
    def __init__(self, super_item, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._super_item = super_item


    @property
    def super_item(self):
        return self._super_item
