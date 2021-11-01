from marshmallow import Schema, fields

class ColorSchema(Schema):
    value = fields.Str()

class FloodZoneSchema(Schema):
    code = fields.Int(data_key="codigo")
    name = fields.Str(data_key="nombre")
    coordinates = fields.List(fields.Dict(), data_key="coordenadas", many=True)
    color = fields.Pluck(ColorSchema, "value")

class FloodZonePaginationSchema(Schema):
    page = fields.Int(data_key="pagina")
    pages = fields.Int(data_key="total")
    items = fields.Nested(FloodZoneSchema, many=True, data_key="zonas")

flood_zones_schema = FloodZoneSchema(many=True)
flood_zone_schema = FloodZoneSchema()
flood_zone_pagination_schema = FloodZonePaginationSchema()