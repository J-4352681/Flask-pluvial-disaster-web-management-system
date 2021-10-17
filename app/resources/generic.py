
class ModificationTemplateParamsWrapper():
    """Permite compatbilidad de interfaces con el template de modificacion"""
    def __init__(self, form, action_url, item_type, item_name, item_id=None):
        self._form = form
        self._action_url = action_url
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
    def item_type(self):
        return self._item_type
    
    @property
    def item_name(self):
        return self._item_name
    
    @property
    def item_id(self):
        return self._item_id