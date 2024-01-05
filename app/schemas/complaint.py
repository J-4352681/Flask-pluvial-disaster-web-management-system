from marshmallow import Schema, fields

class ComplaintSchema(Schema):
    title = fields.Str(required=True, data_key="titulo")
    category_id = fields.Int(required=True, data_key="categoria_id")
    description = fields.Str(required=True, data_key="descripcion")
    coordinates = fields.List(fields.Dict(), data_key="coordenadas", many=True)
    author_first_name = fields.Str(required=True, data_key="nombre_denunciante")
    author_last_name = fields.Str(required=True, data_key="apellido_denunciante")
    author_telephone = fields.Int(required=True, data_key="telcel_denunciante")
    author_email = fields.Email(required=True, data_key="email_denunciante")

class ComplaintFetchSchema(Schema):
    id = fields.Int()
    title = fields.Str(data_key="titulo")
    creation_date = fields.Date(data_key="fecha_de_creacion")
    category_id = fields.Int(data_key="categoria_id")
    description = fields.Str(data_key="descripcion")
    coordinates = fields.List(fields.Dict(), data_key="coordenadas", many=True)
    author_first_name = fields.Str(data_key="nombre_denunciante")
    author_last_name = fields.Str(data_key="apellido_denunciante")
    author_telephone = fields.Int(data_key="telcel_denunciante")
    author_email = fields.Email(data_key="email_denunciante")
