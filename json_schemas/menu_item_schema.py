from marshmallow import Schema, fields


class MenuItemSchema(Schema):
    sku = fields.Str()
    name = fields.Str()
    price = fields.Float()
