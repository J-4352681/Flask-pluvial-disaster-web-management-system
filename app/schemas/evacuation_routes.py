from marshmallow import Schema, fields

class EvacuationRoutesSchema(Schema):
    id = fields.Int()
    name = fields.Str(data_key="nombre")
    coordinates = fields.List(fields.Dict(), data_key="coordenadas", many=True)
    route_points = fields.List(fields.Dict(), data_key="puntos_ruta", many=True)
    description = fields.Str(data_key="descripcion")

class EvacuationRoutesPaginationSchema(Schema):
    page = fields.Int(data_key="pagina")
    total = fields.Function(lambda pagination: len(pagination.items))
    items = fields.Nested(EvacuationRoutesSchema, many=True, data_key="rutas")