from marshmallow import Schema, fields

class MeetingPointsSchema(Schema):
    id = fields.Int()
    name = fields.Str(data_key="nombre")
    coordinates = fields.List(fields.Str(), data_key="coordenadas", many=True)
    direction = fields.Str(data_key="direccion")
    state = fields.Bool(data_key="estado")
    telephone = fields.Str(data_key="telefono")
    email = fields.Str(data_key="email")

class MeetingPointsPaginationSchema(Schema):
    page = fields.Int(data_key="pagina")
    total = fields.Function(lambda pagination: len(pagination.items))
    items = fields.Nested(MeetingPointsSchema, many=True, data_key="puntos")