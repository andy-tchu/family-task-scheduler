from marshmallow import Schema, fields, validate

class TaskSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1,max=40,error="Title length from 1 to 40 characters"))
    description = fields.Str(required=True, validate=validate.Length(min=1,max=200,error="Desctioption length from 1 to 200 characters"))
    assignedTo = fields.List(fields.Str(), required=True)
    familyId = fields.Str(required=True)
    dateTime = fields.DateTime()
    priority = fields.Str(required=True, validate=validate.OneOf(["low", "medium", "high"]))
    status = fields.Str(required=True, validate=validate.OneOf(["pending", "completed"]))
    notes = fields.Str(validate=validate.Length(max=200,error="Note max length 200 characters"))

class TaskUpdateSchema(Schema):
    title = fields.Str(required=True, validate=validate.Length(min=1,max=40,error="Title length from 1 to 40 characters"))
    description = fields.Str(required=True, validate=validate.Length(min=1,max=200,error="Desctioption length from 1 to 200 characters"))
    dateTime = fields.DateTime()
    priority = fields.Str(required=True, validate=validate.OneOf(["low", "medium", "high"]))
    status = fields.Str(required=True, validate=validate.OneOf(["pending", "completed"]))
    notes = fields.Str(validate=validate.Length(max=200,error="Note max length 200 characters"))