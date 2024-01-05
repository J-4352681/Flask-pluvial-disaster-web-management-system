from marshmallow import Schema, fields

class CategoryFetchSchema(Schema):
    id = fields.Int()
    name = fields.Str(data_key="name")