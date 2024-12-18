from marshmallow import Schema, fields, validate
from models import UserSchema, FamilySchema

class MemberSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1,max=20,error="Name length from 1 to 20 characters"))
    role = fields.Str(
            required=True,
            validate=validate.OneOf(["adult", "child"]),
        )
    phone = fields.Str(required=True, validate=validate.Length(min=10, max=12, error='Phone number is 10 to 12 lenght'))
    userId = fields.Str(required=True)
    familyId = fields.Str(required=True)

class MemberUpdateSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1,max=20,error="Name length from 1 to 20 characters"))
    role = fields.Str(
            required=True,
            validate=validate.OneOf(["adult", "child"]),
        )
    phone = fields.Str(required=True, validate=validate.Length(min=10, max=12, error='Phone number is 10 to 12 lenght'))