from marshmallow import Schema, fields

class ColorSchema(Schema):
    value = fields.Str()

class FloodZoneSchema(Schema):
    id = fields.Int()
    name = fields.Str(data_key="nombre")
    coordinates = fields.List(fields.Dict(), data_key="coordenadas", many=True)
    # color = fields.Pluck(ColorSchema, "value")
    color = fields.Str()

class FloodZonePaginationSchema(Schema):
    page = fields.Int(data_key="pagina")
    total = fields.Function(lambda pagination: len(pagination.items))
    items = fields.Nested(FloodZoneSchema, many=True, data_key="zonas")

flood_zones_schema = FloodZoneSchema(many=True)
flood_zone_schema = FloodZoneSchema()
flood_zone_pagination_schema = FloodZonePaginationSchema()