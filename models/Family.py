from marshmallow import Schema, fields, validate

class FamilySchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1,max=20,error="Name length from 1 to 20 characters"))
