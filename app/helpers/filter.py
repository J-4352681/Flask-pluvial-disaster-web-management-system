def apply_filter(model, kwargs):
    '''Realiza un filtro de los resultados a mostrar (simil búsqueda)'''
    return model.query.filter(*[getattr(model, k)==v for k, v in kwargs.items()])
