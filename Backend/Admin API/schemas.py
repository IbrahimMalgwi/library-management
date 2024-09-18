from marshmallow import Schema, fields

class AdminUserSchema(Schema):
    id = fields.Str(dump_only=True)
    firstname = fields.Str(required=True)
    lastname = fields.Str(required=True)
    email = fields.Str(required=True)
    borrowed_books = fields.List(fields.Str())

class AdminBookSchema(Schema):
    id = fields.Str(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    publisher = fields.Str()
    category = fields.Str()
    is_available = fields.Bool()
    borrowed_until = fields.DateTime()
