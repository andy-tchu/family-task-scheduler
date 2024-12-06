from marshmallow import Schema, fields, validate

class MemberSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1,max=20,error="Name length from 1 to 20 characters"))
    role = fields.Str(
            required=True,
            validate=validate.OneOf(["adult", "child"]),
        )
    phone = fields.Str(required=True, validate=validate.Length(min=10, max=12, error='Phone number is 10 to 12 lenght'))
    username = fields.Str(required=True, validate=validate.Length(min=1,max=20,error="Username length from 1 to 20 characters"))
    family_name = fields.Str(required=True, validate=validate.Length(min=1,max=20,error=" length from 1 to 20 characters"))
