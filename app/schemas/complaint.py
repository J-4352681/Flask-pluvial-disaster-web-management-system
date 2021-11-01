from marshmallow import Schema, fields

class ComplaintSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    coordinates = fields.Dict(required=True)
    author_first_name = fields.Str(required=True)
    author_last_name = fields.Str(required=True)
    author_telephone = fields.Int(required=True)
    author_email = fields.Email(required=True)