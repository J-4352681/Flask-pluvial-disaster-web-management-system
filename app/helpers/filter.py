from app.models.role import Role

def apply_filter(model, kwargs):
    """Realiza un filtro de los resultados a mostrar (simil búsqueda)"""
    elements = []
    for k, v in kwargs.items():
        elements += getattr(model, k)(v)
    return elements

# class Filter():
#     def __init__(self, layout_name, element_name, query_function):
#         self._layout_name = layout_name
#         self._element_name = element_name
#         self._query_function = query_function

# class TextFilter(Filter):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._type = "text"

# class DropdownFilter(Filter):
#     def __init__(self, muti = False, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._type = "dropdown"
#         self._multi = multi