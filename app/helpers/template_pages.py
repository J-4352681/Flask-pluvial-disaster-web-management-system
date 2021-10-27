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

class ListDBModelPage(TitledPage):
    """Interfaz paramétrica para una página para el listado de un modelo de la db"""
    def __init__(self, filter_obj, page, attr_names, headers, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._filter_obj = filter_obj
        self._page_obj = self._filter_obj.get_query(page)
        self._headers = headers
        self._attr_names = attr_names

    @property
    def items(self):
        return self._page_obj.items
    
    @property
    def page_obj(self):
        return self._page_obj

    @property
    def headers(self):
        return self._headers

    @property
    def attr_names(self):
        return self._attr_names

    @property
    def form(self):
        return self._filter_obj.form

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