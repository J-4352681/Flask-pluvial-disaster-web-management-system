from wtforms import SelectMultipleField, SelectField

class NonValidatingSelectMultipleField(SelectMultipleField):
    """
    Selector de múltiples campos/alternativas sin validación
    de ingreso de datos y carga de datos en dummy funcional 
    """

    def pre_validate(self, form):
        """Hace una prevalidación de los datos ingresados"""
        pass


class NonValidatingSelectField(SelectField):
    """
    Selector de campo/alternativa sin validación
    de ingreso de datos y carga de datos en dummy funcional 
    """

    def pre_validate(self, form):
        """Hace una prevalidación de los datos ingresados"""
        pass