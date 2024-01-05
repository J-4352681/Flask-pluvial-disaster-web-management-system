from marshmallow import Schema, fields

class StatisticsFetchSchema(Schema):
    id = fields.Int()
    name = fields.Str(data_key="name")
    data = fields.Str(data_key="data")