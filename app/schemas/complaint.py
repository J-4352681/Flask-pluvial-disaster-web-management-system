from marshmallow import Schema, fields

class ComplaintSchema(Schema):
    title = fields.Str(required=True, data_key="titulo")
    category_id = fields.Int(required=True, data_key="categoria_id")
    description = fields.Str(required=True, data_key="descripcion")
    coordinates = fields.Dict(required=True, data_key="coordenadas")
    author_first_name = fields.Str(required=True, data_key="nombre_denunciante")
    author_last_name = fields.Str(required=True, data_key="apellido_denunciante")
    author_telephone = fields.Int(required=True, data_key="telcel_denunciante")
    author_email = fields.Email(required=True, data_key="email_denunciante")
