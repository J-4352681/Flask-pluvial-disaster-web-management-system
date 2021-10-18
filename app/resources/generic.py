
class FormTemplateParamsWrapper():
    """Permite compatbilidad de interfaces con el template de modificacion"""
    def __init__(self, form, action_url, action, return_url, item_type, item_name, item_id=None):
        self._form = form
        self._action_url = action_url
        self._action = action
        self._return_url = return_url
        self._item_type = item_type
        self._item_name = item_name
        self._item_id = item_id
    
    @property
    def form(self):
        return self._form
    
    @property
    def action_url(self):
        return self._action_url

    @property
    def action(self):
        return self._action

    @property
    def return_url(self):
        return self._return_url
    
    @property
    def item_type(self):
        return self._item_type
    
    @property
    def item_name(self):
        return self._item_name
    
    @property
    def item_id(self):
        return self._item_id