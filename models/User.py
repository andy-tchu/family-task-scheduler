from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    username = fields.Str(required=True, validate=validate.Length(min=1,max=20,error="Username length from 1 to 20 characters"))
    password = fields.Str(required=True, validate=validate.Regexp(
        r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,}$',
        error="Password must have at least one lower and upper case letter and one character")
    )
    telegram = fields.Str(required=True, validate=validate.Regexp(
        r'^[A-Za-z\d_]{5,32}$',
        error="Nickname should have only latin charachters and numbers")
    )
    admin = fields.Boolean()

class UserUpdateSchema(Schema):
    telegram = fields.Str(required=True, validate=validate.Regexp(
        r'^[A-Za-z\d_]{5,32}$',
        error="Nickname should have only latin charachters and numbers")
    )
    admin = fields.Boolean()